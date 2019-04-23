'''
Pseudo-code:

== English ==
1. Find title or honorific (e.g. Mr., Dr., ...)

2. Find verb
2a. If not verb AND not apostrophe + "s": Add to name
3a. If sentence ends (no next word): Return name

2b. If verb OR apostrophe + "s": Return name


== Chinese ==
1. Find surname (rule-based)
2. Find title or honorific (e.g. 先生, 博士, ...)

Potential for Chinese verbs here but it is hard ... or we need to find a rule-based approach
'''

import nltk
import string
import sys


def findEnglishNames(sentence):
    # Pre-defined
    englishTitles = ["Mr.", "Dr.", "Prof.",
                     "Mrs.", "Ms.", "Mdm.", "Miss.", "Messrs."]
    foundName = False
    curr_name = ""
    curr_count = 0
    
    names = set()
    
    
    text = nltk.word_tokenize(sentence)
    poslist = nltk.pos_tag(text)

    for word, pos in poslist:
        word = word.replace(" ", "")
        curr_count += 1
        if curr_count % 2500 == 0:
            print("Processing sentence number", curr_count)
            
        if foundName == True:
            if "V" in pos or "'s" in word or word in englishTitles or word in string.punctuation:
                foundName = False
                names.add(curr_name)
                curr_name = ""

            else:
                curr_name += " %s" % word

                if word == poslist[-1][0]:
                    names.add(curr_name)

        if word in englishTitles:
            foundName = True
            continue

    return names

def findChineseNames(sentence):
    chineseTitles = ["博士", "女士", "小姐", "先生", "太太"]
    
    curr_name = ""
   
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2] 
    language = sys.argv[3]
    
    if language == "en":
        with open(input_file, "r", encoding="utf-8") as inp:
            names = findEnglishNames(inp.read())

    elif language == "zh":
        with open(input_file, "r", encoding="utf-8") as inp:
            names = findChineseNames(inp.read())
        
    else:
        names = {}
        
    with open(output_file, "w", encoding="utf-8") as outp:
        for name in names:
            outp.write(name + "\n")