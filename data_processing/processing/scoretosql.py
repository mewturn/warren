# \t-separated file: to convert text-based format into SQL queries and execute the queries
import sys
import mysql.connector

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="milton_corpus",
    )
    mycursor = mydb.cursor()
    infile = sys.argv[1]

    with open(infile, "r", encoding="utf-8") as inp:
        for line in inp:
            query = "INSERT INTO askwarren_scored VALUES(%s, %s, %s, %s, %s, %s)"
            line = tuple(line.split("\t"))
            query = query % line
            print(query)
            mycursor.execute(query)
            mydb.commit()
