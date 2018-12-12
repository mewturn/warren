import sys
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="milton_corpus",
)

mycursor = mydb.cursor()

if __name__ == "__main__":
    id_file = sys.argv[1]
    score_file = sys.argv[2]
    count = 1
    table = "askwarren"
    
    with open(id_file, "r", encoding="utf-8") as source:
        id_lines = source.read().splitlines()
        with open(score_file, "r", encoding="utf-8") as scores:
            score_lines = scores.read().splitlines()            
            for id, score in zip(id_lines, score_lines):
                try:
                    query = "UPDATE askwarren set score = %s WHERE id = %s" % (score, id)
                    print(query)
                    mycursor.execute(query)
                except Exception as e:
                    print(e)

                finally:
                    if not (count % 1000):
                        mydb.commit()
                    count += 1
                