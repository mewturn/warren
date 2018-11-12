import sys

def calculate_distribution(inp, outp):
    output = {}
    
    with open(inp, "r", encoding="utf-8") as f:
        with open(outp, "w", encoding="utf-8") as g:
            print ("Reading words...")
            for line in f:
                words = line.split(" ")
                for word in words:
                    if word in output:
                        output[word] += 1
                    else:
                        output[word] = 1
            print ("Writing to file...")
            for key, value in sorted(output.items(), key=lambda kv: kv[1], reverse=True):
                g.write(key + " | " + str(value) + "\n")

if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    calculate_distribution(input_filename, output_filename)