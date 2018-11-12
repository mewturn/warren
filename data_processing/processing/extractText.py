"""
Extract PDF text using PDFMiner. Adapted from
http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from io import StringIO
import os

def pdf_to_text(pdfname):

    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()

    # Cleanup
    device.close()
    sio.close()

    return text
    
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
    for filename in namelist:
        if filename in txtlist:
            print("Already existing file.")
            continue
        else:
            print("Processing", filename)
            try:
                with open(filename + '.txt', 'w', encoding='utf-8') as output:
                    output.write((pdf_to_text(filename + ".pdf")))
            except Exception as e:
                print(e)