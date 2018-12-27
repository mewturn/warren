import time
import mysql.connector
import os

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="milton_corpus",
)
mycursor = mydb.cursor()
    
if __name__ == "__main__":    
    db = "warren_align"
    
    for i in os.listdir('.'):
        count = 0
        print("Processing file: ", i)
        with open(i, "r", encoding="utf-8") as inp:
            for i in inp:
                i = i.split("\t")
                if (not i[0] == '' and not i[1] == '' and not i[0].isspace() and not i[1].isspace()):
                    count += 1
                    if (not count%100):
                        print("Processing line #", count)
                        
                    # Important to escape characters
                    query = "INSERT INTO %s VALUES(default, '%s', '%s', default);" % (db, i[0].replace("'", "\\'"), i[1].replace("'", "\\'"))
                    
                    mycursor.execute(query)
                    mydb.commit()
            