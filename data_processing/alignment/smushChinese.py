from smush import chinese_smush
import sys
from opencc import OpenCC

if __name__ == "__main__":
    cc = OpenCC('s2twp')
    with open(sys.argv[1], "r", encoding="utf-8") as inp:
        with open(sys.argv[2], "w", encoding='utf-8') as outp:
            
            if sys.argv[3] == "sc":      
                print ("Converting simplified Chinese to traditional Chinese.")
                for line in inp:
                    line = line.replace("\n", "")
                    if line == "":
                        continue
                    outp.write(chinese_smush(cc.convert(line)) + "\n")
            else:
                print ("Already traditional Chinese, no conversion required.")
                for line in inp:
                    line = line.replace("\n", "")
                    if line == "":
                        continue
                    outp.write(chinese_smush(line) + "\n")