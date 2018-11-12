''' Removes punctuations and other special characters (numbers) from the data set '''

import sys

def removePunctuation(input_string, deltab=r'`~!@#$%^&*()-_=+{}[];:\\\",<.>?/\|0123456789。，—：；、‘’？“”…（）《》「」'):
    trantab = input_string.maketrans('','', deltab)
    return input_string.translate(trantab)
    
    
    
if __name__ == "__main__":
    if len(sys.argv) > 2:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]  
    
        with open(input_filename, "r", encoding="utf-8") as f:
            with open(output_filename, "w", encoding="utf-8") as g:      
                for line in f:
                    print ("Processing", line)
                    g.write(removePunctuation(line))    
    else:
        print ("Insufficient variables ...")
        
    # Tests
    # my_string = 't!h@i#s$ %i^s& a* s(t)r\\7in9g'
    # my_chinese_string = '当 我们 说 ： “ 救救 海洋 ， 给 海洋 治 治病 吧 。 ” 说 的 就是 这 金字塔ss8276108 。 '
    # print (removePunctuation(my_string))
    # print (removePunctuation(my_chinese_string))
