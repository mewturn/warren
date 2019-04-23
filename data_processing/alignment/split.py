from smush import find_characters, load_file
import sys
import re

if __name__ == "__main__":
    inp = load_file(sys.argv[1])
    file_en, file_zh = "temp_en.txt", "temp_zh.txt"
    temp_en, temp_zh = [], []
    en_reg = "[a-zA-Z]"
    zh_reg = "[\u4e00-\u9fff]"
    
    for i in inp:
        if not find_characters(i, "enzh"):
            continue
        elif find_characters(i, "zh") and not find_characters(i, "en"):
            temp_zh.append(i)
        elif find_characters(i, "en") and not find_characters(i, "zh"):
            temp_en.append(i)
        else:
            if len(re.findall(en_reg, i)) > len(re.findall(zh_reg,i)):
                temp_en.append(i)
            else:
                temp_zh.append(i)
            
            
            
    with open(file_en, "w", encoding="utf-8") as f:
        [f.write(i + "\n") for i in temp_en]
        
    with open(file_zh, "w", encoding="utf-8") as g:
        [g.write(i + "\n") for i in temp_zh]