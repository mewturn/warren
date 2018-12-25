import sys

if __name__ == "__main__":
    files_to_process = sys.argv[1]
    output = sys.argv[2]

    with open(files_to_process, "r", encoding="utf-8") as inp:
        with open(output, "w", encoding="utf-8") as outp:
            for line in inp:
                en_file, zh_file = line.split(" | ")
                en_file = en_file.replace("\n", "")
                zh_file = zh_file.replace("\n", "")
                
                # Write smush batch
                # outp.write("python smush.py %s processed_eng/%s en\n" % (en_file, en_file.replace("EN_txt/", "")))
                # outp.write("python smush.py %s processed_chi/%s zh\n" % (zh_file, zh_file.replace("CHI_txt/", "")))

                # Write LFAligner batch
                outp.write("LF_aligner_4.1.exe -f=t -l=en,zh -s=y -r=xn -t=n -i=%s,%s" % (en_file.replace("EN_txt/", "processed_eng/"), zh_file.replace("CHI_txt/", "processed_chi/")))