## TWSE

import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
	
	output_path = "files/"
	processed_count = 0
	
	for i in range(2518):
		url = "http://cgc.twse.com.tw/pressReleases/promoteNewsArticleCh/%s" % (i)
		output_file = "%s%s.txt" % (output_path, processed_count)

		try:
			temp = urllib.request.urlopen(url).read()
			with open(output_file, "wb") as outp:
				# outp.write(BeautifulSoup(temp, "html.parser").text)
				outp.write(temp)
				processed_count += 1
			
		except Exception as e:
			print (e)
			
		else:
			print (processed_count, "completed.")