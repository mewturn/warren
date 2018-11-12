

if __name__ == "__main__":
	inp = "uncorpora_20090831.tmx"
	outp = "outp"
	lang = "ZH"
	writing = False
	
	with open(inp, "r", encoding="utf-8") as file:
		with open("%s_%s.txt" % (outp, lang), "a", encoding="utf-8") as out: 
			for line in file:
				if '<tuv xml:lang="%s">' % (lang) in line:
					writing = True
					continue
				
				if writing:
					if '</tuv>' in line:
						writing = False
					else:
						out.write(line)
				