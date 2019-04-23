import sys
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="milton_corpus",
)
mycursor = mydb.cursor()

def getSegments(en, zh):
    query = "SELECT `id`, `en`, `zh-hant` FROM %s WHERE `en` LIKE '%%s%' AND `zh-hant` LIKE '%%s%';" % (table, en, zh)
    
    mycursor.execute(query)
    return mycursor.fetchall()
    
if __name__ == "__main__":
    input_file = sys.argv[1]
    
    with open(input_file, "r", encoding="utf-8") as inp:
        for line in inp:
            en, zh = line.split("\t")
            