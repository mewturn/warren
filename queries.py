import pymysql
# import log

def saveFeedback(en, zh_hant, modified_en, rating="default"):
    table = "suggestion"
    query = "INSERT INTO %s VALUES(default, '%s', '%s', %s, '%s')" % (table, en, zh_hant, rating, modified_en)

    try:
        # Database settings, change this!
        mydb = pymysql.connect(host="localhost", user="warren", passwd="Writepath123", db="milton_corpus")
        mycursor = mydb.cursor()
        #log.writeLog(query)
        mycursor.execute(query)
        mydb.commit()

    except Exception as e:
        print(e)
        #log.writeLog(str(e))

    else:
        print(query, "executed successfully!")

    finally:
        if mydb.open:
            mydb.close()
