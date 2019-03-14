def get_idle_translators(cases, translators, output):
    with open(cases, "r", encoding='utf-8') as inp:
        with open(translators, "r", encoding='utf-8') as inp2:
            cases = set()
            translators = set()
            for i in inp:
                try:
                    cases.add(int(i.replace("\n", "")))
                except Exception as e:
                    print (i, e)
                    continue
                    
            for j in inp2:
                try:
                    translators.add(int(j.replace("\n", "")))
                except Exception as e:
                    print(e)
                    continue
            print ("Finished mapping cases and translators.")
            
        with open(output, "w", encoding='utf-8') as outp:
            for i in translators:
                if i not in cases:
                    outp.write(str(i) + "\n")
        print ("Completed.")  

        
def map_langs_to_user(langs, translators, output):
    with open(langs, "r", encoding='utf-8') as inp:
        with open(translators, "r", encoding='utf-8') as inp2:
            dict = {}
            settings_size = 14
            input = [i.replace("\n", "") for i in inp]
            input2 = [i.replace("\n", "") for i in inp2]
            for i in input2:
                dict[i] = [0]*settings_size

            print (input)
            for i in range(len(input)):
                    dict[input2[i]][int(input[i])-1] = 1
            
            print ("Finished merging the data.")
            
            with open(output, "w", encoding='utf-8') as outp:
                for key, value in dict.items():
                    suff = ""
                    for v in value:
                        suff += "|"+str(v)
                    outp.write(str(key) + suff + "\n")
            print ("Completed.")        
if __name__ == "__main__":
    cases = "cases.txt"
    translators = "translators.txt"
    output = "output_cats.txt"
    langs, lang_id = "lang_id_langs.txt", "lang_id.txt"
    cats, cat_id = "cat_id_cats.txt", "cat_id.txt"
    
    #get_idle_translators(cases, translators, output)
    map_langs_to_user(cats, cat_id, output)