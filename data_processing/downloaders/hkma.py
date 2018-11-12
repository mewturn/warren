import urllib.request
from bs4 import BeautifulSoup
import time

def getURL():
    pre = "https://www.hkma.gov.hk/eng/key-information/press-releases/"
    with open("url.txt", "w") as outp:
        try:
            for year in range(1997, 2019):
                if year < 2012:
                    suff = str(year)
                else:
                    suff = str(year) + ".shtml"
                
                url = pre + suff
                web = urllib.request.urlopen(url).read().decode('utf-8')
                soup = BeautifulSoup(web, "lxml")
                content = soup.find("div", {"class": "prContent"})
                links = content.findAll('a')
                
                for link in links:
                    href = link.get("href")
                    outp.write(href + "\n")
                    print (href)
                print ("Year",year,"completed.")
                    
        except Exception as e:
            print(e)
    
    return 

def getText(url):
    web = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(web, "lxml")
    content = soup.find("div", {"class": "item"}).text
    
    return content
    
def getData():
    pre = "https://www.hkma.gov.hk"
    i = 0
    
    with open("url.txt", "r") as inp:
        for link in inp:
            
            if "press-releases/" in link and ".shtml" in link:
                try:
                    url = pre + link 
                    url2 = url.replace("eng", "chi")
                    
                    with open(str(i) + ".txt", "w", encoding='utf-8') as outp:
                        outp.write(getText(url))
                        print ("File",i,"created (English).")
                                        
                    with open(str(i) + "_C.txt", "w", encoding='utf-8') as outp:
                        outp.write(getText(url2))
                        print ("File",i,"created (Chinese).")
                    
                except Exception as e:
                    print(e)
                
                finally:
                    i += 1  
    return

if __name__ == "__main__":
    # getURL()
    getData()
    