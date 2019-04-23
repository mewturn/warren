import urllib.request
from bs4 import BeautifulSoup
import time

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def getURL():
    pre = "http://www.etnet.com.hk/www/tc/stocks/ci_ipo_info.php?page="
    with open("url.txt", "w") as outp:
        try:
            outp_links = set()
            for page in range(1, 12): 
                opener = AppURLopener()
                url = pre + str(page)
                resp = opener.open(url)
                web = resp.read()
                soup = BeautifulSoup(web, "lxml")
                content = soup.find("div", {"class": "DivFigureContent"})
                links = content.findAll('a')
                
                for link in links:
                    href = link.get("href")
                    if not href == None and not "page" in href:
                        outp_links.add(href)
                
                for i in outp_links:
                    outp.write(i + "\n")
                    
        except Exception as e:
            print(e)
    
    return 

def getText(url, lang):
    opener = AppURLopener()
    resp = opener.open(url)
    web = resp.read()
    soup = BeautifulSoup(web, "lxml")
    #content = soup.findAll("div", {"class" : "DivArticleList", "class" : "dotLine"})
    #content = soup.findAll("div", {"class" : "ipoColumnBlock"})
    content = soup.findAll("div", {"class" : "DivArticleList"})
    outp = []
    
    if lang == "en":
        phrase = "<p>"
    elif lang == "zh":
        phrase = "<p>"
    
    #if lang == "en":
    #    phrase = "USE OF PROCEEDS"
    #elif lang == "zh":
    #    phrase = "售股所得款項用途"
    
    for i in content:
    
        if phrase in str(i):
            _ = i.text.split(phrase)
            
            return _[-1].replace("\n", "")
    return
    
def getData():
    pre = "http://www.etnet.com.hk/www/eng/stocks/"
    i = 0
    dir = "temp/"
    processed = set()
    with open("url.txt", "r") as inp:
        for link in inp:
            try:
                code = link.replace("ci_ipo_detail.php?code=", "").replace("&type=listed\n", "")
                if code in processed:
                    print ("Stock", code, "already processed.")
                    continue
                else:
                    processed.add(code)
                    
                    
                url = pre + link 
                url2 = url.replace("eng", "tc")
                
                with open(dir + str(i) + ".txt", "w", encoding='utf-8') as outp:
                    outp.write(getText(url, "en"))
                    print ("File",i,"created (English).")
                                    
                with open(dir + str(i) + "_C.txt", "w", encoding='utf-8') as outp:
                    outp.write(getText(url2, "zh"))
                    print ("File",i,"created (Chinese).")
                
            except Exception as e:
                print(e)
            
            finally:
                i += 1  
    return

if __name__ == "__main__":
    # getURL()
    getData()
    