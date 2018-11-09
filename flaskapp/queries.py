import mysql.connector
import log

# Database settings, change this!
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="milton_corpus",
)

mycursor = mydb.cursor()

def saveFeedback(en, zh_hant, modified_en, rating="default"):
    table = "warren_evaluation"
    query = "INSERT INTO %s VALUES(default, '%s', '%s', %s, '%s')" % (table, en, zh_hant, rating, modified_en)
    
    try:
        log.writeLog(query)
        mycursor.execute(query)
        mydb.commit()
    
    except Exception as e:
        print(e)
        log.writeLog(str(e))
        
    else:
        print(query, "executed successfully!")
        