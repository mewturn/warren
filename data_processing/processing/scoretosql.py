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
    logfile = "log.txt"
    count = 1
    with open(infile, "r", encoding="utf-8") as inp:
        with open(logfile, "w", encoding="utf-8") as log:
            for line in inp:
                try:
                    query = "INSERT INTO askwarren_scored VALUES(%s, '%s', '%s', %s, %s, '%s')"
                    line = [i.replace("'", "''").replace("\n", "") if i != "" else "-" for i in line.split("\\t")]
                    query = query % tuple(line)
                    print("QUERY #%s: %s" % (count, query))
                    mycursor.execute(query)
                    mydb.commit()
                    count += 1
                except Exception as e:
                    print(e)
                    log.write("%s: %s\n" % (count, e))