from pdfminer.pdfinterp import PDFResourceManager
#, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from urllib.request import urlopen

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

#pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
pdfFile = open('/home/lcreina/Documentos/programacao/python3/ConsultaPagamentoRel.sao.felix.2017.pdf')
outputString = readPDF(pdfFile)
for linha in outputString:
	print(linha)
	i = input("digite")
#print(outputString)
pdfFile.close()
