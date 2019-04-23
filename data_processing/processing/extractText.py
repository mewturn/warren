"""
Extract PDF text using PDFMiner. Adapted from
http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from threading import Timer
from io import StringIO

import os
import time

def pdf_to_text(pdfname):

    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    count = 1
    # Extract text
    fp = open(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        print(f"Processing page {count}.")
        count += 1
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()

    # Cleanup
    device.close()
    sio.close()

    return text
    
def timeout(curr):
    print (curr, "minutes have passed...")
    t = Timer(60, timeout, [curr+1]).start()
    
if __name__ == "__main__":
    namelist = []
    txtlist = []
    
    # Gets the current list of PDFs to process
    for file in os.listdir(os.getcwd()):
        if "pdf" in file or "PDF" in file:
            namelist.append(file[:-4])
        elif "txt" in file:
            txtlist.append(file[:-4])

    # Converts each PDF in namelist to a TXT file
    timeout(0)
    
    for filename in namelist:
        if filename in txtlist:
            print("Already existing file.")
            continue
        else:
            print("Processing", filename)
            try:
                with open(filename + '.txt', 'w', encoding='utf-8') as output:
                    print("Writing to file...")
                    output.write((pdf_to_text(filename + ".pdf")))
                    print("Completed!")
            except Exception as e:
                print(e)