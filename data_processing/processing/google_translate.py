import requests
import json
from apiclient.discovery import build
import sys

def translate(q, source="en", target="zh-TW"):
	# Translate text, default: zh-TW to en
	
	key = '''ENTER KEY HERE'''
	service = build("translate", "v2", developerKey=key)

	collection = service.translations()

	request = collection.list(q=q, target=target, source=source)

	response = request.execute()

	response_json = json.dumps(response)

	#ascii_translation = ((response['translations'][0])['translatedText']).encode('utf-8').decode('ascii', 'ignore')

	utf_translation = ((response['translations'][0])['translatedText']).encode('utf-8').decode()
	print ("Source: %s\nTranslation: %s" % (q, utf_translation))
	
	return utf_translation

	
	
	
if __name__ == "__main__":
	input = sys.argv[1]
	output = sys.argv[2]
	
	with open(input, "r") as inp:
		with open(output, "w", encoding="utf-8") as outp:
			for text in inp:
				if len(text) == 0 or text == "\n" or text == " ":
					continue
				outp.write(translate(text))
				outp.write("\n")