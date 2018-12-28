import urllib.request
import urllib.parse
import sys
import mysql.connector
from nltk.metrics import edit_distance
import json

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="milton_corpus",
)
mycursor = mydb.cursor()
    

def askWarren(content):
    url = "http://104.199.227.39/translate?"
    params = {"q" : content, "model" : "7787"}
    try:        
        params = urllib.parse.urlencode(params)
        # print(url+params)
        web = urllib.request.urlopen(url + params).read().decode('utf-8')
        return web
        
    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    # Get last index
    table = "warren_retrain"
    query = "SELECT `id` FROM `%s` ORDER BY (`id`) DESC LIMIT 1;" % (table)
    mycursor.execute(query)
    last_index = mycursor.fetchone()[0]
    
    # Split into n sets
    n = 50
    interval = int(last_index/n)

    for i in range(n):
        print("Processing batch #", i+1)
        try:
            # Initialize boundaries
            if i == 0:
                lower_bound = 1
                upper_bound = interval

            # Set upper limit
            if i == n-1:
                upper_bound = last_index

            # Get segments which are not processed
            query = "SELECT `id`, `en`, `zh-hant` FROM `%s` WHERE score = -1 AND `id` BETWEEN %s AND %s;" % (table, lower_bound, upper_bound)

            mycursor.execute(query)
            segments = mycursor.fetchall()

            for segment in segments:                
                try:
                    id, en, q = segment[:3]
                    res = askWarren(q)
                    t = json.loads(res)['translatedText'].replace("\n", "").strip() # Process the output text
                    score = edit_distance(en.lower(), t.lower()) # Convert to lowercase, we just care about whether the characters met -> useful for titles
                    max_length = max(len(en), len(t))
                    sim = round(100 * (1 - score/max_length), 1)
                    print(en, t, sim)
                    query = "UPDATE `%s` set `en_warren` = '%s', `score` = %s WHERE `id` = %s" % (table, t.replace("'", "\\'"), sim, id)
                    mycursor.execute(query)
                    mydb.commit()

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

        finally:
            lower_bound = upper_bound + 1
            upper_bound = upper_bound + interval
            