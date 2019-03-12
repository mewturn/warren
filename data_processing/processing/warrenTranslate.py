from askWarren import askWarren
import sys
import json

if __name__ == "__main__":
    filename = sys.argv[1]
    output_file = sys.argv[2]
        
    with open(output_file, "w", encoding="utf-8") as g:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line)
                res = askWarren(line)
                print(res)
                t = json.loads(res)['translatedText'].replace("\n", "").strip() 
                print(t)
                g.write(t + "\n")