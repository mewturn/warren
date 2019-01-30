import os

def accountingSearch(files, names):
    stock_codes = []
    acc_firm_names = []
    out_file = "out.txt"
    
    for filename in files:
        with open(filename, "r", encoding="utf-8") as inp:
            stock_code = filename.split("_")[1]
            content = inp.read()
            
            for name in names:
                if name in content:
                    print (stock_code, name)
                    stock_codes.append(stock_code)
                    acc_firm_names.append(name)
                    break

    with open(out_file, "w", encoding="utf-8") as outp:
        for i in range(len(stock_codes)):
            outp.write(f"{stock_codes[i]}   {acc_firm_names[i]} \n")
            
if __name__ == "__main__":
   names = ["資誠", "勤業眾信", "安永", "安侯建業", "正風", "國富浩華", "立本台灣"]
   files = [i for i in os.listdir() if ".txt" in i] 
   accountingSearch(files, names)