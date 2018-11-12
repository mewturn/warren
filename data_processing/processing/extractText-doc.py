import docx2txt
import os
from nltk.tokenize import sent_tokenize

for filename in os.listdir(os.getcwd()):
# extract text
	if ".docx" in filename:
		print("Processing %s" % (filename))
		try:
			text = docx2txt.process(filename)
			with open (filename[:-5] + "-p.txt", "w", encoding="utf-8") as file :
				file.write(sent_tokenize(text))
		except Exception as e:
			print (e)
			
		finally:
			print ("Completed.")