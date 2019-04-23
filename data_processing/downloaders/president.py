import urllib.request
from bs4 import BeautifulSoup
import time   
        
if __name__ == "__main__":
    en_output = "president_en/en_%s.txt"
    zh_output = "president_zh/zh_%s.txt"
    log_file = "error_log.txt"
    
    for code in range(1, 9999):
        if code < 1923:
            continue
        
        base_url = "http://www2.afe.com.hk/AFEWebService/Fundamental/getCompProfile?culture=%s&companyID=President&itemcode=%s&selectType=1&Type=0"
        en_url = base_url % ("en", code)
        zh_url = base_url % ("zh-tw", code)
        
        try:
            # English
            en_resp = urllib.request.urlopen(en_url)
            en_resp_content = en_resp.read()
            en_soup = BeautifulSoup(en_resp_content, "lxml")
            
            # Chinese
            zh_resp = urllib.request.urlopen(zh_url)
            zh_resp_content = zh_resp.read()
            zh_soup = BeautifulSoup(zh_resp_content, "lxml")           


            with open(en_output % code, "a", encoding="utf-8") as outp:                
                for content in en_soup.findAll("td", {"class":"cell_body"}):
                    for br in content.findAll("br"):
                        br.replace_with("\n")
                    outp.write(content.text + "\n")
            
            with open(zh_output % code, "w", encoding="utf-8") as outp:
                for content in zh_soup.findAll("td", {"class":"cell_body"}):
                    for br in content.findAll("br"):
                        br.replace_with("\n")
                    outp.write(content.text + "\n")                
            
            print ("Stock code", code, "completed.")
            
        except Exception as e:
            print(e)
            with open(log_file, "a", encoding="utf-8") as log:
                log.write(str(code) + ": Error\n")
            