import sys
import os

def compareFiles(en, zh):
    with open(en, "r", encoding="utf-8") as en_in:
        english_content = en_in.readlines()
    
    with open(zh, "r", encoding="utf-8") as zh_in:
        chinese_content = zh_in.readlines()

    similar = 0
    
    e_len = len(english_content)
    c_len = len(chinese_content)
    diff = abs(e_len - c_len)
    
    # If the length of both differ significantly, most likely misaligned
    if diff > c_len or diff > e_len:
        return False
    
    #print(english_content)
    #print(chinese_content)

    for i in range(min(len(english_content), len(chinese_content))):
        # If more than x number of lines are similar = determine that the documents are the same
        if english_content[i] != '\n' and chinese_content[i] != '\n' and english_content[i] == chinese_content[i]:
            similar += 1 

        if similar > 100:
            return True
        
    return False



if __name__ == "__main__":
    output = sys.argv[1]
    en_folder = os.path.join(os.getcwd(), "EN_txt")
    en_dir = "EN_txt/"
    zh_dir = "CHI_txt/"

    with open(output, "w", encoding="utf-8") as outp:
        en_files = os.listdir(en_folder)
        
        for en_filename in en_files:
            try:
                en_str = en_filename[11:].replace(".txt", "")
                zh_num = int(en_str) + 1
                if zh_num < 1000:
                    zh_str = "0" * (3 - len(str(zh_num))) + str(zh_num)
                else:
                    zh_str = str(zh_num)
                zh_str = zh_str + "_C"
                zh_filename = en_filename.replace(en_str, zh_str)
                print("Processing %s, %s" % (en_filename, zh_filename))
                
                if (not compareFiles(en_dir + en_filename, zh_dir + zh_filename)):
                    print("Found match %s, %s" % (en_filename, zh_filename))
                    outp.write("%s%s | %s%s\n" % (en_dir, en_filename, zh_dir, zh_filename))

            except Exception as e:
                print(e)