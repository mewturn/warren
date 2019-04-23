import mysql.connector

def createsql(mydb):
    english_file = "output_en.txt"
    chinese_file = "output_zh.txt"
    output_file = "output2.txt"
    en_list = []
    zh_list = []
    query = set()
    count_en, count_zh = 0,0 
    with open(english_file, "r", encoding="utf-8") as en:
        with open(chinese_file, "r", encoding="utf-8") as zh:
            default = "INSERT INTO temp_ar VALUES(default, '%s', '%s');"
            for _ in en:
                en_list.append(_)
                if count_en % 10000 == 0:
                    print("Writing English File #", count_en)
                count_en += 1
                
            for _ in zh:
                zh_list.append(_)                
                if count_zh % 10000 == 0:
                    print("Writing Chinese File #", count_zh)
                count_zh += 1
                
            for i in range(len(en_list)):
                try:
                    this_query = default % (en_list[i], zh_list[i])
                    this_query = this_query.replace("\n", "")
                    executesql(mydb, this_query)
                except Exception as e:
                    print(e)
                


def executesql(mydb, query):
    mycursor = mydb.cursor()
    print(query)
    mycursor.execute(query)
    mydb.commit()
            
if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="milton_corpus",
    )
    
    createsql(mydb)
    #executesql()