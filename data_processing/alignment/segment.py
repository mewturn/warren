## Segment Chinese text & sentences into phrases for Machine Translation training
## Requires 'jieba'

import jieba
import sys
import re

def slice(inp, outp):
    ''' Slice the text in the input file 'inp' and writes it to an output file 'outp' '''
    jieba.load_userdict("milton_dict.txt")
    r = re.compile("([a-zA-Z]+)([0-9]+)")
    s = {'｟','｠','：'}
    with open(inp, "r", encoding="utf-8") as f:
        with open(outp, "w", encoding="utf-8") as g:      
            for line in f:
                seg_list = jieba.cut(line)
                #print(list(seg_list))
                output = "".join(["" if i.isspace() else i + " " if not i in s else i for i in seg_list])
                
                g.write(output + '\n')

if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    slice(input_filename, output_filename)

