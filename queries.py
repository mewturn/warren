import pymysql
import datetime
import log
import re

def saveFeedback(en, zh_hant, modified_en, rating="default"):
    table = "suggestion"
    query = "INSERT INTO %s VALUES(default, '%s', '%s', %s, '%s')" % (table, en, zh_hant, rating, modified_en)

    try:
        # Database settings, change this!
        mydb = pymysql.connect(host="localhost", user="warren", passwd="Writepath123", db="milton_corpus")
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()

    except Exception as e:
        print(e)
        log.writeLog(str(e))

    else:
        print(query, "executed successfully!")

    finally:
        if mydb.open:
            mydb.close()

def countUsage(user, sentence):
    table = "translation_usage"
    datestring = datetime.datetime.now().strftime("%d-%m-%y")
    words = countWords(sentence)

    try:
        query = "SELECT * FROM `%s` WHERE `user` = '%s' AND `datestring` = '%s'" % (table, user, datestring)
        mydb = pymysql.connect(host="localhost", user="warren", passwd="Writepath123", db="milton_corpus")
        mycursor = mydb.cursor()
        mycursor.execute(query)
        exists = mycursor.fetchone()

        if exists == None:
            query = "INSERT INTO `%s` VALUES(default, '%s', '%s', %s)" % (table, datestring, user, words)

        else:
            query = "UPDATE `%s` SET `words` = `words` + %s WHERE `user` = '%s' AND `datestring` = '%s'" % (table, words, user, datestring)
        log.writeLog(query)
        mycursor.execute(query)
        mydb.commit()

    except Exception as e:
        print(e)
        log.writeLog(str(e))

    else:
        print(query, "executed successfully!")

    finally:
        if mydb.open:
            mydb.close()


def countWords(sentence):
    return sum([len(i) for i in re.findall(r'[\u4e00-\u9fff]+', sentence)])

def getUsage():
    query = "SELECT sum(`words`) FROM `translation_usage`; "
    try:
        mydb = pymysql.connect(host="localhost", user="warren", passwd="Writepath123", db="milton_corpus"
        mycursor = mydb.cursor()
        mycursor.execute(query)
        count = mycursor.fetchone()
        if count == None:
            return 0
        return count[0]

    except Exception as e:
        print(e)
        log.writeLog(str(e))

    else:
        print(query, "executed successfully!")

    finally:
        if mydb.open:
            mydb.close()
