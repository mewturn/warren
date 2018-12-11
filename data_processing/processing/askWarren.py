import urllib.request
import urllib.parse
import sys

def askWarren(content):
    url = "http://104.199.227.39/translate?"
    params = {"q" : content, "model" : "7787"}
    try:        
        params = urllib.parse.urlencode(params)
        # print(url+params)
        web = urllib.request.urlopen(url + params).read().decode('utf-8')
        return web
        
    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, "r", encoding="utf-8") as inp:
        with open(output_file, "w", encoding="utf-8") as outp:
            for segment in inp:
                try:
                    output = askWarren(segment)
                    print(output)
                    outp.write(output)
                except Exception as e:
                    print(e)