## Xinhua

import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
	
	output_path = "XINHUA/"
	processed_count = 0
	
	with open("xinhua_url.txt", "r") as url_list:
		for url in url_list:
			output_file = "%s%s.txt" % (output_path, processed_count)
	
			try:
				with open("temp.txt", "wb") as out:
					out.write(urllib.request.urlopen(url).read())
				
				writing = False
			
				with open("temp.txt", "r", encoding="utf-8") as file:
					with open(output_file, "w", encoding="utf-8") as outp:
						for line in file:
							if "Arial" in line:
								writing = True
							if "YOU MAY LIKE" in line:
								writing = False
							if writing:
								outp.write(BeautifulSoup(line, "html.parser").text)
								
				processed_count += 1
				
			except Exception as e:
				print (e)
				
			else:
				print (processed_count, "completed.")