from bs4 import BeautifulSoup
import urllib.request
import re


if __name__ == "__main__":
	''' Processing the URLs '''
	links = "tpt_links_processed.txt"
	output_path = "TPT/"
	processed_count = 0
	with open(links, "r") as inp:
		for url in inp:
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
	
	''' Obtaining the URLs '''
	# output = "tpt_links.txt"
	# skip = ["EVERYDAY ENGLISH", "BUSINESS ENGLISH", "Business English"]
	# count = 1


	# while True:
		# try:
			# html_page = urllib.request.urlopen("http://www.taipeitimes.com/News/list?section=lang&mode=2&month1=1&day1=1&year1=1999&month2=6&day2=4&year2=2018&page=%s" % (count))
			# soup = BeautifulSoup(html_page)
	

			# with open(output, "a+", encoding="utf-8") as outp:
				# for link in soup.findAll('a', attrs={'href': re.compile("^News/lang/")}):
					# if link.text not in skip:
						# outp.write("%s | %s \n" % (link.get('href'), link.text))
						# print (link.text)
		
		
		# except Exception as e:
			# print (e)
			
		
		# finally:
			# print ("Completed iterations: %s" % (count))
			# count += 1