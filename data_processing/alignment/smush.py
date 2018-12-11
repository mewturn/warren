import sys
import re


def istitle(wordslist):
    return wordslist[0][-1] != "." and wordslist[1][0].isupper() and wordslist[2][0].isupper()

# Remove empty fields in a list


def remove_spaces(lines):
    return list(filter(lambda a: a != "", lines))

# Returns True if the text has the characters it is looking for


def find_characters(line, language="enzh"):
    if language == "enzh":
        regex = "[a-zA-Z\u4e00-\u9fff]"
    elif language == "en":
        regex = "[a-zA-Z]"
    elif language == "zh":
        regex = "[\u4e00-\u9fff]"
    return not re.findall(regex, line) == []

# Check if a word uses only the English alphabets


def is_english(word):
    try:
        return word.encode('ascii').isalpha()
    except:
        return False

# Build dictionary of Chinese words that should be merged back


def build_dict(file):
    _dict = {}
    for _ in load_file(file):
        try:
            if _[-1] in _dict:
                _dict[_[-1]].add(_[0])
            else:
                _dict[_[-1]] = set(_[0])
        except Exception as e:
            print(e)
    return _dict

# Build dictionary of Chinese transitions probabilities


def build_transitions(file):
    _dict = {}
    for _ in load_file(file):
        try:
            _ = _.split(" | ")
            _dict[_[0]] = int(_[-1])
        except Exception as e:
            print(e)

    return _dict

# Remove spaces between Chinese words


def chinese_smush(line):
    characters = [""] + list(line) + [""]
    for index in range(len(characters)):
        if characters[index].isspace() and (not is_english(characters[index-1]) and not is_english(characters[index+1])) and not characters[index-1] == "." and not characters[index-1] == ")" and not characters[index-1].isdigit():
            characters[index] = ""
    return "".join(remove_spaces(characters))

# Check common word pairing which gets broken up accidentally


def check_word_pair(dict, prev_line, curr_line, special_words_left, special_words_right, symbols, transitions):
    try:
        curr_first_char, prev_last_char = curr_line[0], prev_line[-1]
        prev_characters = list(prev_line)
        curr_characters = list(curr_line)
        phrase = prev_last_char + curr_first_char
        threshold = 250

        return curr_first_char in dict and prev_last_char in dict[curr_first_char] \
            or curr_characters[0] == "」" or curr_characters[0] == "）" \
            or prev_characters[-1] == "「" or prev_characters[-1] == "（" \
            or prev_last_char in special_words_left \
            or (curr_first_char in special_words_right and prev_last_char not in symbols) \
            or (phrase in transitions and transitions[phrase] > threshold)
        # or prev_last_char == "："
    except Exception as e:
        pass
# Check exceptions to merge back to the previous sentence based on the last words of the previous line
# Backward Pass


def backward_pass(prev_line, curr_line, special_words_left, special_words_right, symbols, transitions):
    first_char, last_char = curr_line[0], curr_line[-1]
    curr_split, prev_split = curr_line.split(), prev_line.split()
    threshold = 250

    try:
        curr_first_word = curr_split[0]
        curr_first_word_last_char = curr_first_word[-1]
        prev_last_word = prev_split[-1]
        prev_last_char = prev_line[-1]
        phrase = curr_first_word + " " + prev_last_word

    #print (special_words_left)
    #print (prev_last_word, prev_last_word in special_words_left, curr_first_word in special_words_right and prev_last_char not in symbols)

    # Bunch of if/else return statements
        #print (curr_line, prev_last_word in special_words_left, (curr_first_word in special_words_right and prev_last_char not in symbols), (prev_last_char == ":" and prev_line[-2].isnumeric()), (curr_first_word.islower() and not ";" in prev_last_word), (last_char == "." or last_char == ":" or last_char == ";") and first_char.islower())
        return prev_last_word in special_words_left \
            or (curr_first_word in special_words_right and prev_last_char not in symbols) \
            or (prev_last_char == ":" and prev_line[-2].isnumeric())  \
            or ((curr_first_word.islower() and curr_first_word[0] != "(") and not ";" in prev_last_word) \
            or (last_char == "." or last_char == ":" or last_char == ";") and first_char.islower() \
            or (phrase in transitions and transitions[phrase] > threshold)

    except Exception as e:
        pass
    # or curr_line.islower()
    # or (len(curr_split) == 1) and (curr_line.islower() or curr_first_word_last_char == ")" or curr_first_word_last_char == ".") \
    # or (len(prev_split) == 1) and (prev_last_char == ".")
    # or ")" in curr_first_word \

# Load file to be processed


def load_file(file):
    print("Loading", file, "to be processed...")

    with open(file, "r", encoding="utf-8") as inp:
        outp = inp.read().split("\n")

    return outp

# Write output to file


def write_output(lines, file):
    print("Writing to file...")
    #lines = [line[1:].replace("  ", " ") + "\n" if line[0].isspace() else line.replace("  ", " ") + "\n" for line in lines]
    lines = [line.replace("  ", " ") + "\n" for line in lines]
    lines = purge_noise(lines)
    with open(file, "w", encoding="utf-8") as outp:
        outp.writelines(lines)
        print("Completed.")

# Splitting handler


def split_by(data, symbol):
    output = []
    data = list(filter(None, data))

    if symbol == "\n":
        print("Splitting data by line break")
        for _ in data:
            output.append(_.replace("\n", ""))

    elif symbol == ". ":
        print("Splitting data by full stop")
        for _ in data:
            if symbol in _:
                split = _.split(symbol)
                mylist = [split[i] +
                          "." for i in range(len(split)-1)] + [split[-1]]

                for segment in mylist:
                    output.append(segment)

            else:
                output.append(_)
    else:
        print("Splitting data by ", symbol)
        for _ in data:
            if symbol in _:
                split = _.split(symbol)
                mylist = [split[i] +
                          symbol for i in range(len(split)-1)] + [split[-1]]
                for segment in mylist:
                    output.append(segment)
            else:
                output.append(_)

    return output

# Remove noises


def purge_noise(lines):
    noise_file = "noise.txt"
    noises = [i.replace("\n", "") for i in load_file(noise_file)]
    output = []
    count = 0

    for line in lines:
        if not find_characters(line):
            #print ("Purged: ", line)
            count += 1
            continue
        for noise in noises:
            if not find_characters(line.replace(noise, "")):
                #print ("Purged: ", line)
                count += 1
                break
        else:
            output.append(line)

    print("Purged", count, "number of lines")
    return output


if __name__ == "__main__":
    input_file, output_file, language = sys.argv[1], sys.argv[2], sys.argv[3]
    en_dir, zh_dir = "EN/", "ZH/"
    zh_dict_file = zh_dir + "zh_dict.txt"
    en_transition_file, zh_transition_file = en_dir + \
        "en_transitions.txt", zh_dir + "zh_transitions.txt"
    en_special_word_left, en_special_word_right = en_dir + \
        "special_english_left.txt", en_dir + "special_english_right.txt"
    zh_special_word_left, zh_special_word_right = zh_dir + \
        "special_chinese_left.txt", zh_dir + "special_chinese_right.txt"

    print("Processing file in the following language: ", language)

    # Splitting part
    symbols = {
        "en": {". ", ";", ":", "\n"},
        "zh": {"。", "：", "；", "\n"},
    }

    exceptions = {
        "en": [en_special_word_left, en_special_word_right],
        "zh": [zh_special_word_left, zh_special_word_right],
    }

    data = load_file(input_file)
    lines = data

    for symbol in symbols[language]:
        lines = split_by(lines, symbol)
        lines = remove_spaces(lines)

    special_words_left, special_words_right = load_file(
        exceptions[language][0]), load_file(exceptions[language][1])

    # English
    if language == "en":
        transitions = build_transitions(en_transition_file)
        for index in range(len(lines)-1, 1, -1):
            if backward_pass(lines[index-1], lines[index], special_words_left, special_words_right, symbols[language], transitions):
                lines[index-1] = " ".join([lines[index-1], lines[index]])
                lines[index] = ""

    # Chinese
    elif language == "zh":
        #special_words_left = [i.replace("\n", "") for i in list(load_file(zh_special_word_left))]
        #special_words_right = [i.replace("\n", "") for i in list(load_file(zh_special_word_right))]
        zh_dict = build_dict(zh_dict_file)
        transitions = build_transitions(zh_transition_file)
        # print(transitions)

        # Remove spaces between characters
        for index in range(len(lines)):
            lines[index] = chinese_smush(lines[index])

        for index in range(len(lines)-1, 1, -1):
            if check_word_pair(zh_dict, lines[index-1], lines[index], special_words_left, special_words_right, symbols[language], transitions):
                lines[index-1] = "".join([lines[index-1], lines[index]])
                lines[index] = ""

    write_output(lines, output_file)
