import configparser
import json
import mysql.connector
import pinyin
import requests
import sys
from apiclient.discovery import build
from bs4 import BeautifulSoup
from nltk.metrics import edit_distance


# Global variables
config_file = "config.ini"
log_file = "error.log"
google_api_key = '''ENTER KEY HERE'''

# Error logging
def logError(err):
    print(err)
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"{err}\n")

# Data Processing
def removePunctuations(s, deltab=r'`~!@#$%^&*()-_=+{}[];:\\\",<.>?/\|0123456789。，—：；、‘’？“”…（）《》「」'):
    '''Removing punctuations and other symbols from the input string. Returns a string.'''
    trantab = s.maketrans("", "", deltab)
    return s.translate(trantab)

def removeHTML(s):
    '''Removes HTML from the input string. Returns a string.'''
    soup = BeautifulSoup(s)
    return soup.get_text()
    
def convertName(name, target="pinyin"):
    '''Converts names to a target form.'''
    try: 
        if target == "pinyin":
            converted = pinyin.get(name, format="strip", delimiter=" ").split(" ")

        # 2-character name
        if len(converted) == 2:
            last_name = converted[0]
            first_name = converted[1]

        # 3-character name
        elif len(converted) == 3:
            last_name = converted[0]
            first_name = "".join(converted[1:])

        # 4-character name (e.g. 歐陽, 司馬, 司徒, ...)
        else:
            last_name = "".join(converted[0:2])
            first_name = "".join(converted[2:])

        # Capitalize last name
        last_name = last_name.capitalize()
        first_name = first_name.capitalize()
        return "%s %s" % (last_name, first_name)    
    
    except Exception as e:
        logError(e)
        
# Other Tools
def googleTranslate(q, source="zh-TW", target="en"):
    '''Translate text, default setting: zh-TW to en. Returns a string.'''
	key = google_api_key
    
	try:
        service = build("translate", "v2", developerKey=key)
        collection = service.translations()
        request = collection.list(q=q, target=target, source=source)
        response = request.execute()
        response_json = json.dumps(response)
        utf_translation = ((response['translations'][0])['translatedText']).encode('utf-8').decode()
        
        return utf_translation
        
    except Exception as e:
        logError(e)

def calculateSimilarity(source, target):
    '''Calculate Levenshtein distance between items of th esame index in both source and target. Returns a list of scores.'''
    ns, nt = len(source), len(target)
    assert ns == nt, f"The source file and target file should have an equal number of segments. \nSource sentences: {ns}\nTarget sentences: {nt}"
            
    score = []
    for i in range(ns):
        try:
            diff = edit_distance(source[i], target[i])
            max_length = max(len(source[i]), len(target[i]))
            score = round(100 * (1 - (diff / max_length)), 1)
            scores.append(score)
        
        except Exception as e:
            logError(e)
            outp.append(-1)
    
    return scores

def generateQuery(task, d):
    '''General mySQL query string from a task string and a data dictionary. Returns a string.'''
    query = ""
    err = "Insufficient data to generate the required query."
    
    try:
        if task == "updateScoreWithId":
            assert d["table"] != None \
            and d["score"] != None \
            and d["id"] != None, err
            query = "UPDATE `{d['table']}` SET `score` = {d['score']} WHERE `id` = {d['id']};" 
    
    except Exception as e:
        logError(e)
        
    return query

def readConfig(config_file, section="mysql"):
    '''Parse a config file to get connection details. Returns a dictionary.'''
    try:
        config = configparser.ConfigParser()
        config.read(config_file)
        return dict(config[section])
    
    except Exception as e:
        logError(e)
        
    

# Connection to DB
# mydb = mysql.connector.connect(**readConfig(config_file, "mysql"))

if __name__ == "__main__":
    print(generateQuery("updateScoreWithId", {"table": "askwarren", "id": "2", "score": 93.0}))
    #print(calculateSimilarity([1,2,3],[2,4]))
    print(removePunctuations('当 我们 说 ： “ 救救 海洋 ， 给 海洋 治 治病 吧 。 ” 说 的 就是 这 金字塔ss8276108 。 '))