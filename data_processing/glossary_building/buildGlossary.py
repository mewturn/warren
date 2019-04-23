import jieba
import sys
import mysql.connector
import time
import re
from nltk.corpus import stopwords

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    port = "3306",
    database = "milton_corpus",
    user = "root",
    passwd = ""
)
mycursor = mydb.cursor()

def updateDB(d, lang, table="glossary_building"):
    for k, v in d.items():
        try:
            k = (k.replace('\'', '"').replace('\n', ''))
            q = "SELECT `id`, `count` FROM `%s` WHERE `content` = '%s';" % (table, k)
            mycursor.execute(q)
            row = mycursor.fetchone()
            if row is None:
                q = "INSERT INTO `%s` VALUES(default, '%s', '%s', '%s');" % (table, k, v, lang)
            else:
                new_count = row[1] + v
                q = "UPDATE `%s` SET `count` = '%s' WHERE `id` = '%s' AND `lang` = '%s';" % (table, new_count, row[0], lang)
            mycursor.execute(q)
            mydb.commit()


        except Exception as e:
            print(e)

# Remove non-English elements in the string
def processEnglish(t):
    return re.sub("[^A-Za-z ]+", "", t)

# Remove non-Chinese elements in the string
def processChinese(t):
    return re.sub("[^\u4e00-\u9fff]+", "", t)

if __name__ == "__main__":
    english_dict = {}
    chinese_dict = {}
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Initialize variables EN: 1, 4-gram | ZH: 2, 7-gram (arbitrary, inclusive)
    min_en_gram, max_en_gram = 1, 4
    min_zh_gram, max_zh_gram = 2, 7
    threshold = 1_000
    curr = 0

    with open(input_file, "r", encoding="utf-8") as inp:
        for _ in inp:
            try:
                if _.isspace() or len(_) == 0:
                    continue
                en, zh = _.split("\t")

                # Processing the n-grams
                for lang in ["en", "zh-hant"]:
                    # Language-dependent settings
                    if lang == "en":
                        min_gram, max_gram = min_en_gram, max_en_gram
                        # data = [word for word in processEnglish(en).split() if word not in stopwords.words("english")]
                        data = processEnglish(en).split()
                        joiner = " "
                        data_dict = english_dict

                    elif lang == "zh-hant":
                        min_gram, max_gram = min_zh_gram, max_zh_gram
                        data = processChinese(zh)
                        joiner = ""
                        data_dict = chinese_dict

                    for i in range(min_gram, max_gram+1):
                        for j in range(len(data)):
                            ngram = data[j:j+i]
                            if len(ngram) == i:
                                _ = joiner.join(ngram)
                                if _ in data_dict:
                                    data_dict[_] += 1
                                else:
                                    data_dict[_] = 1  

            except Exception as e:
                print(e)

            finally:
                if not curr % threshold:
                    print("Updating DB, line #", curr)
                    updateDB(english_dict, "en")
                    updateDB(chinese_dict, "zh-hant")
                    english_dict = {}
                    chinese_dict = {}

                curr += 1

            
