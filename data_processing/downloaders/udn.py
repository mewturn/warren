## UDN

import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
	
	output_path = "UDN/"
	processed_count = 0
	
	with open("links.txt", "r") as url_list:
		for url in url_list:
			output_file = "%s%s.txt" % (output_path, processed_count)
	
			try:
				temp = urllib.request.urlopen(url).read()
				with open(output_file, "w", encoding="utf-8") as outp:
					outp.write(BeautifulSoup(temp, "html.parser").text)
								
					processed_count += 1
				
			except Exception as e:
				print (e)
				
			else:
				print (processed_count, "completed.")