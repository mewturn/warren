import urllib.request
from bs4 import BeautifulSoup
import time
from selenium import webdriver

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def getURL():
    pre = "http://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=1&sc_lang=en"
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
    content = soup.findAll("div", {"class" : "company_txt"})
    #content = soup.findAll("div", {"class" : "ipoColumnBlock"})
    #content = soup.find_all("p")
    
    str = "".join([i.text + "\n" for i in content])
    if "xref" in str:
        return ""
    return str
    
def getData():
    

    link = "http://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=%s&sc_lang=en"
    dir = "temp_hkex/"
    processed = set()
    for i in range(1, 2):
        try:
            url = link % (i)
            print (url)
            url2 = url.replace("en", "zh-HK")
            print (url2)
            browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
            #print(browser.find_element_by_css_selector('div.company_txt.col_summary'))
            browser.get(url)
            #print(browser.page_source)
                     
            
            with open(dir + str(i) + "_C.txt", "w", encoding='utf-8') as outp:
                #text = getText(url, "en")
                outp.write(browser.page_source)
                print ("File",i,"created (English).")
            return                    
            with open(dir + str(i) + ".txt", "w", encoding='utf-8') as outp:
                outp.write(getText(url2, "zh"))
                print ("File",i,"created (Chinese).")
            
        except Exception as e:
            print(e)
        
    return

if __name__ == "__main__":
    # getURL()
    getData()
    