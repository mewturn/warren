import time
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="milton_corpus",
)
mycursor = mydb.cursor()
    
if __name__ == "__main__":
    aligned_txt = "aligned_merged_en_p-merged_zh_p.txt"
    db = "temp_ar2"
    
    with open(aligned_txt, "r", encoding="utf-8") as inp:
        for i in inp:
            i = i.split("\t")
            # Important to escape characters
            query = "INSERT INTO %s VALUES(default, '%s', '%s');" % (db, i[0].replace("'", "\\'"), i[1].replace("'", "\\'"))
            print(query)
            mycursor.execute(query)
            mydb.commit()
            