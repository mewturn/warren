import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="milton_corpus",
)
mycursor = mydb.cursor()

def getWarren():
    zh = "`zh-hant`"
    en = "`en`"
    query = f"SELECT DISTINCT {zh} FROM warren;"
    print ("Fetching data from warren...")
    mycursor.execute(query)
    return mycursor.fetchall()

def getData(table):
    zh = "`zh-hant`"
    en = "`en`"
    query = f"SELECT DISTINCT {zh}, {en} FROM {table}"
    print (f"Fetching data from {table}...")
    mycursor.execute(query)
    return mycursor.fetchall()

def saveLines(table, lines):
    print("Saving data...")
    for line in lines:
        try:
            zh_content = line[0].replace("\n", "").replace("\r", "").replace("'", '"')
            en_content = line[1].replace("\n", "").replace("\r", "").replace("'", '"')    
            query = f"INSERT INTO {table} VALUES(default, '{en_content}', '{zh_content}');"
            mycursor.execute(query)
            mydb.commit()
        except Exception as e:
            print(e)

def linesToQuery(table, file):
    zh = "`zh-hant`"
    en = "`en`"
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                line = line.split("\\t")
                zh_content = line[1].replace("\n", "").replace("\r", "").replace("'", '"')    
                en_content = line[0].replace("\n", "").replace("\r", "").replace("'", '"')    
                query = f"INSERT INTO {table} VALUES('{zh_content}', '{en_content}');"
                mycursor.execute(query)
                mydb.commit()
            
            except Exception as e:
                print(e)
            
if __name__ == "__main__":
    warren = getWarren()
    source_table = "sheet1"
    source_file = "transperfect__.txt"
    print("Saving text to file...")
    linesToQuery(source_table, source_file)
    data = getData(source_table)
    table = "transperfect"
    unique = []
    #print(warren)
    
    print("Calculating...")
    for line in data:
        if line[0] == "":
            continue
            
        for wline in warren:
            if line[0] == wline[0]:
                break

        else:
            print(f"Found new unique segment: {line[0]}")
            unique.append(line)
            
    saveLines(table, unique)