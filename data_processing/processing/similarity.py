import sys
from nltk.metrics import *

if __name__ == "__main__":
    source_file = sys.argv[1]
    predict_file = sys.argv[2]
    output = "score.txt"
    
    with open(source_file, "r", encoding="utf-8") as source:
        source_lines = source.read().splitlines()
        with open(predict_file, "r", encoding="utf-8") as predict:
            predict_lines = predict.read().splitlines()
            with open(output, "w", encoding="utf-8") as outp:
                #scores = [edit_distance(source_lines[i], predict_lines[i]) for i in range(len(predict_lines))]
                for i in range(len(predict_lines)):
                    score = edit_distance(source_lines[i], predict_lines[i])
                    print (score)
                    outp.write(str(score) + "\n")
                
                #max_diff = "Biggest difference:" + str(max(scores)) + "\n"
                #min_diff = "Smallest difference:" + str(min(scores)) + "\n"
                #avg_diff = "Average difference:" + str(sum(scores)/len(scores)) + "\n"
                    
                #outp.write(max_diff)
                #outp.write(min_diff)
                #outp.write(avg_diff)
                