if __name__ == "__main__":
    import sys
    import mysql.connector
    import buildGlossary
    
    input_file = sys.argv[1]
    
    mydb = mysql.connector.connect(
    host = "127.0.0.1",
    port = "3306",
    database = "milton_corpus",
    user = "root",
    passwd = ""
    )
    mycursor = mydb.cursor()
    count = 1
    d = {}
    
    with open(input_file, "r", encoding="utf-8") as inp:
        for line in inp:
            try:
                line = buildGlossary.processChinese(line)
                line = line.split()
                for i in line:
                    if i in d:
                        d[i] += 1
                    else:
                        d[i] = 1
                            
            except Exception as e:
                print(e)
                
            finally:
                if not count % 500:
                    print ("Processing line #", count)
                    for i in d:
                        buildGlossary.updateDB(d, "zh-hant", "chinese_terms")
                        d = {}
                count += 1