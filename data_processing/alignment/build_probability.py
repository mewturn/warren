from smush import find_characters, load_file
import sys

def count_transitions(line, language, n=2):
    if language == "en":
        characters = line.split()

    elif language == "zh":
        characters = list(line)
    
    else:
        return {}  
    
    dict_list = []
    
    for gram in range(2, n+1):    
        dict = {}
        for i in range(len(characters) - gram):
            grams = []
            for j in range(gram):
                curr_char = characters[i+j]
                if not find_characters(curr_char, language):
                    break
                grams.append(curr_char)
            else:
                if language == "en":
                    word = " ".join(grams)
                elif language == "zh":
                    word = "".join(grams)
                else:
                    word = " ".join(grams)
                
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1
                
        dict_list.append(dict)
    
    return dict_list
    
if __name__ == "__main__":
    '''
        Argument 1 : Input File
        Argument 2 : Output File
        Argument 3 : Language
        Argument 4 : value of n
    '''
    print ("Processing", sys.argv[1], ", Language:", sys.argv[3], ", n:", sys.argv[4])
    
    source = load_file(sys.argv[1])
    transitions = {}
    threshold = 25
    
    if sys.argv[4] == None:
        grams = 2
    else:
        grams = int(sys.argv[4])
        
    print ("Counting transitions")    
    for sentence in source:
        dict_list = count_transitions(sentence, sys.argv[3], grams)
        for dict in dict_list:
            for key in dict:
                if key in transitions:
                    transitions[key] += dict[key]
                else:
                    transitions[key] = dict[key]
    
    print ("Writing to file...")
    with open(sys.argv[2], "w", encoding="utf-8") as outp:
        for key, value in sorted(transitions.items(), key=lambda kv: kv[1], reverse=True):
            if value > threshold:
                outp_str = key + " | " + str(value) + "\n"
                outp.write(outp_str)