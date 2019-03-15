import mysql.connector as mc
from nltk.metrics import edit_distance
import log
import time
import datetime

# Set up connection to database
mydb = mc.connect(option_files='config.ini', option_groups='mysql')
mycursor = mydb.cursor()


def getClientCorpus(client_id, lang_id):
    '''Get the corpus from the client'''
    query = "SELECT `id`, `sourceText`, `"


def getCondensedFuzzy(langID, excluded=None):
    '''Get the source segments from the condensed fuzzy match database.'''
    exclusion = ""
    if excluded != None:
        exclusion = f"AND `id` NOT IN {excluded}"
    query = f"SELECT `id`, `sourceText`, `words` FROM `fuzzy_match` WHERE `langID` = langID {exclusion} ORDER BY `words` "
    try:
        start_time = time.time()
        mycursor.execute(query)
        elapsed_time = time.time() - start_time

        return mycursor.fetchall(), elapsed_time

    except Exception as e:
        print(f"An exception occured. {e}")
        log.log(e, "Exception")


def getRepetitions(case_id):
    '''Get the list of (distinct) repeated segments from the subcase.'''
    query = f"SELECT `segmentCopyToID` FROM `TMrepetitions` WHERE `subCaseID` = '{case_id}' GROUP BY `segmentCopyToID` "
    try:
        start_time = time.time()
        mycursor.execute(query)
        elapsed_time = time.time() - start_time
        reps = [str(rep[0]) for rep in mycursor.fetchall()]

        return reps, elapsed_time

    except Exception as e:
        print(f"An exception occured. {e}")
        log.log(e, "Exception")


def getHundos(case_id):
    '''Get the list of (distinct) 100% match segments from the subcase.'''
    query = f"SELECT `segmentNew` FROM `TMfuzzyMatches` WHERE `subCaseID` = '{case_id}' AND `distance` >= 100 GROUP BY `segmentNew` "
    try:
        start_time = time.time()
        mycursor.execute(query)
        elapsed_time = time.time() - start_time
        hundos = [str(hundo[0]) for hundo in mycursor.fetchall()]

        return hundos, elapsed_time

    except Exception as e:
        print(f"An exception occured. {e}")
        log.log(e, "Exception")


def getSourceSegments(case_id, excluded):
    '''Get the actual source segments which need to be matched.'''
    query = f"SELECT `id`, `sourceText`, `words` FROM `TMsegments` WHERE `subCaseID` = '{case_id}' AND `id` NOT IN {excluded} "
    try:
        start_time = time.time()
        mycursor.execute(query)
        elapsed_time = time.time() - start_time

        return mycursor.fetchall(), elapsed_time

    except Exception as e:
        print(f"An exception occured. {e}")
        log.log(e, "Exception")


def getCaseData(case_id):
    '''Get the attribute of a case.'''


def getQueue():
    '''Get the current cases which are queueing to be matched.'''
    query = "SELECT `id`, `user_id`, `target_lang` FROM `cases` WHERE `status` IN ('incomplete', 'pending', 'claimed', 'review') AND `service` IN (2, 4) AND `tm` = 'on' AND `id` != `master_case` AND `TM_discount_finished` != 0 AND `TM_match_started` = 0 AND `TM_match_finished` = 0 ORDER BY `wordcountFinal` ASC LIMIT 1;"
    mycursor.execute(query)

    return mycursor.fetchone()


def updateDatabase(userID, subCaseID, segmentOld, segmentNew, langID, textOld, textNew, distance):
    '''Insert entry into the `TMfuzzyMatch` database.'''
    query = f"INSERT INTO `TMfuzzyMatches` VALUES(default, {userID}, {subCaseID}, {segmentOld}, {segmentNew}, {langID}, '{textOld}', '{textNew}', '{distance}' "
    try:
        print(query)
        mycursor.execute(query)
        mydb.commit()

    except Exception as e:
        print(f"An exception occured. {e}")
        log.log(e, "Exception")


def changeStatus(event, case_id):
    '''Modify status of a case'''
    # Current events - change a case to TM_match_started and TM_match_finished
    query = ""
    if event == "start":
        query = f"UPDATE `cases` SET `TM_match_started` = 1 WHERE `id` = {case_id} "

    elif event == "finish":
        query = f"UPDATE `cases` SET `TM_match_finished` = 1 WHERE `id` = {case_id} "

    mycursor.execute(query)
    mydb.commit()


if __name__ == "__main__":
    while True:
        try:
            time.sleep(5)
            case_id, user_id, lang_id = getQueue()
            curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"Fuzzy Match process began on: {curr_time}")
            changeStatus("start", case_id)
            print(f"Case #{case_id}")

            # Handling source
            reps, reps_time = getRepetitions(case_id)
            print(
                f"{len(reps)} repeated segments, found in {round(reps_time, 2)} seconds.")

            hundos, hundos_time = getHundos(case_id)
            print(
                f"{len(hundos)} 100% match segments, found in {round(hundos_time, 2)} seconds.")

            excluded = f"({','.join(reps + hundos)})"
            source, source_time = getSourceSegments(case_id, excluded)
            print(
                f"{len(source)} source segments to be matched, found in {round(source_time, 2)} seconds.")

            # Handling target
            target, target_time = getCondensedFuzzy(case_id)
            print(
                f"{len(target)} target segments to be matched, found in {round(target_time, 2)} seconds.")

            # Fuzzy Matching
            lower_bound = 0.75
            upper_bound = 1.5
            print("Starting...")
            fm_start = time.time()

            for i in range(len(source)):
                s_id, s_text, s_words = source[i]
                min_length = int(lower_bound * s_words)  # Round down
                max_length = int(upper_bound * s_words + 0.5)  # Round up
                match_sim = 0
                match_id = None
                match_text = None

                for j in range(len(target)):
                    t_id, t_text, t_words = target[i]
                    # Target was sorted in ascending length order (important to check this!)
                    if t_words < min_length:
                        continue
                    if t_words > max_length:
                        break

                    score = edit_distance(s_text, t_text)
                    base = max(s_words, t_words)
                    sim = round(100 * (1 - score/base))  # Nearest integer

                    if sim > match_sim:
                        match_sim = sim
                        match_id = t_id
                        match_text = t_text

                    # Found a 100% match
                    if match_sim == 100:
                        break

                if match_sim >= 75:
                    updateDatabase(userID=user_id, subCaseID=case_id, segmentOld=s_id, segmentNew=match_id,
                                   langID=lang_id, textOld=s_text, textNew=match_text, distance=match_sim)

            fm_elapsed = time.time() - fm_start
            print(f"Fuzzy Match completed! \nTime taken: "
                  f"{int(fm_elapsed/3600)}h "
                  f"{int(fm_elapsed/60)}m "
                  f"{int(fm_elapsed % 60)}s")
            changeStatus("finish", case_id)

        except Exception as e:
            print(f"An exception occured. {e}")
            log.log(e, "Exception")
