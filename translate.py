import os
import subprocess
import time
import json
import jieba
from flask import jsonify
import smushChinese as sc
import re

# APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # Application top
NMT_ROOT = os.path.join(APP_ROOT, "OpenNMT")

shell_trans = os.path.join(APP_ROOT, "trans.sh")
improve_trans = os.path.join(APP_ROOT, "improve.sh")
milton_dict = os.path.join(APP_ROOT, "milton_dict.txt")

def improve(en, zh, improved):
    try:
        subprocess.check_output([improve_trans, en, zh.encode("utf-8"), improved])
    except Exception as e:
        return "Error."

def _translate(content, model):
    outp = []
    try:
        content = content.split("\n")
        
        for text in content:
            sent_list = text.split("。")
            sent_list = [sent_list[i] + "。" for i in range(len(sent_list)-1)] + [sent_list[-1]]
            for sent in sent_list:
                sent = sc.smushText(sent, "sc")
                num = re.findall(r'\d+', sent)
                processed_num = ["{:,}".format(eval(i)) if len(i) > 4 and i[0] != "0" and eval(i) > 2100 else i for i in num]
                for i in range(len(processed_num)):
                    sent = sent.replace(num[i], processed_num[i])

                if sent.isspace() or len(sent)==0:
                    continue
                else:
                    if model ==  "7788":
                        jieba.load_userdict(milton_dict)
                        sent = " ".join(jieba.cut(sent)).replace("｟ ","｟").replace(" ｠","｠")
                        #return text
                    outp.append(json.loads(subprocess.check_output([shell_trans, sent.encode("utf-8"), model]).decode())[0][0]["tgt"] + " ")
            outp.append("\n")
        # et = time.time() - st
        # return "OK"
        return json.dumps({"originalText": "\n".join(content), "message": "success", "translatedText": "".join(outp)})
        #return "%s\n\nElapsed time: %ss" % ("".join(outp), round(et,3))    

    except Exception as e:
        return json.dumps({"originalText": "\n".join(content), "message": "翻譯時出現一些問題, 請再嘗試一次\nError Details - %s." % (e), "translatedText": ""})

def translate(content, model):
    # st = time.time()
    outp = []
    try:
        content = content.split("\n")
        
        for text in content:
            sent_list = text.split("。")
            sent_list = [sent_list[i] + "。" for i in range(len(sent_list)-1)] + [sent_list[-1]]
            for sent in sent_list:
                sent = sc.smushText(sent, "sc")
                num = re.findall(r'\d+', sent)
                processed_num = ["{:,}".format(eval(i))  if len(i) > 4 and eval(i) > 2100 else i for i in num]
                for i in range(len(processed_num)):
                    sent = sent.replace(num[i], processed_num[i])

                if sent.isspace() or len(sent)==0:
                    continue
                else:
                    if model ==  "7788":
                        jieba.load_userdict(milton_dict)
                        sent = " ".join(jieba.cut(sent)).replace("｟ ","｟").replace(" ｠","｠")
                        #return text
                    outp.append(json.loads(subprocess.check_output([shell_trans, sent.encode("utf-8"), model]).decode())[0][0]["tgt"] + " ")
            outp.append("\n")
        # et = time.time() - st
        return "".join(outp)
        #return "%s\n\nElapsed time: %ss" % ("".join(outp), round(et,3))    

    except Exception as e:
        return "翻譯時出現一些問題, 請再嘗試一次\nError Details - %s." % (e)