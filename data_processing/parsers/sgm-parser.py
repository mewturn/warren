import sys
from bs4 import BeautifulSoup

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(output_file, "w", encoding="utf-8") as outp:
        with open(input_file, "r", encoding="utf-8") as inp:
            for i in BeautifulSoup(inp.read(), "lxml").findAll("seg"):
                outp.write(i.get_text() + "\n"  )
            