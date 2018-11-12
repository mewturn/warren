import urllib.request
from bs4 import BeautifulSoup
import time

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def getURL():
    pre = "http://www.imf.org/zh/News/Search?type=News+Article&category&datefrom=1994-01-01&dateto=2018-09-05&page="
    with open("url_imf_news.txt", "w") as outp:
        try:
            outp_links = set()
            for page in range(1, 36): 
                
                opener = AppURLopener()
                url = pre + str(page)
                
                print("Processing URL", url)
                
                resp = opener.open(url)
                web = resp.read()
                soup = BeautifulSoup(web, "lxml")
                content = soup.findAll("div", {"class": "result-row"})
                
                for _ in content:
                    link = _.find("a").get("href")
                    if not link == None and "Article" in link:
                        outp_links.add(link)

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
    content = soup.find_all("p")
    
    str = "".join([i.text + "\n" for i in content])
    if "xref" in str:
        return ""
    return str
    
def getData():
    # pre = "http://www.etnet.com.hk/www/eng/stocks/"
    i = 0
    dir = "temp_imf/"
    processed = set()
    with open("url_imf_news.txt", "r") as inp:
        for link in inp:
            try:
                url = link 
                url2 = url.replace("zh", "en")
                
                with open(dir + str(i) + "_C.txt", "w", encoding='utf-8') as outp:
                    text = getText(url, "zh")
                    if text == "":
                        break
                    outp.write(text)
                    print ("File",i,"created (Chinese).")
                                    
                with open(dir + str(i) + ".txt", "w", encoding='utf-8') as outp:
                    outp.write(getText(url2, "en"))
                    print ("File",i,"created (English).")
                
            except Exception as e:
                print(e)
            
            finally:
                i += 1  
    return

if __name__ == "__main__":
    getURL()
    getData()
    