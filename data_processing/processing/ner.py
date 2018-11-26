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
2. Find 先生

Potential for Chinese verbs here but it is hard ... or we need to find a rule-based approach
'''

import nltk
import string
import sys


def findEnglishName(sentence):
    englishTitles = ["Mr.", "Dr.", "Prof.",
                     "Mrs.", "Ms.", "Mdm.", "Miss.", "Messrs."]
    foundName = False

    name = ""
    text = nltk.word_tokenize(sentence)
    poslist = nltk.pos_tag(text)

    for word, pos in poslist:
        word = word.replace(" ", "")

        if foundName == True:
            if "V" in pos or "'s" in word or word in englishTitles or word in string.punctuation:
                foundName = False
                print(name)
                name = ""

            else:
                name += " %s" % word

                if word == poslist[-1][0]:
                    print(name)

        if word in englishTitles:
            foundName = True
            continue


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r", encoding="utf-8") as inp:
        findEnglishName(inp)
