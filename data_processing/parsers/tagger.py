import re
import time

def get_segments(file):
	with open(file, "r", encoding="utf-8") as inp:
		return inp.read()

if __name__ == "__main__":
	file = "URL testing.txt"
	segments = get_segments(file)
	
	url_re = "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"
	
	url_re2 = "(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:\'\".,<>?«»“”‘’]))?"
	
	# Modify Glossary
	glossary = ["duckling"]
	
	# Name List
	namelist = []

	url_sub = "｟URL：%s｠" 
	glossary_sub = "｟Glossary：%s｠" 

	for token in segments.split():
		# print (segment)
		
		# Sub with glossary
#		if line in glossary:
#			line = glossary_sub % (line)
#			print (line)
				
		if re.search(url_re2, token):
			#line = url_sub % (line)
			print (token)
		
		#elif re.search(