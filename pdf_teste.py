from pdfminer.layout import LAParams
from pdfminer.converter import PDFResourceManager, PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

document = open('/home/lcreina/Documentos/programacao/python3/ConsultaPagamentoRel.sao.felix.2017.pdf', 'rb')

#Create resource manager
rsrcmgr = PDFResourceManager()

# Set parameters for analysis.
laparams = LAParams()

# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.get_pages(document):
	interpreter.process_page(page)
	# receive the LTPage object for the page.
	layout = device.get_result()
	for element in layout:
		if instanceof(element, LTTextBoxHorizontal):
			print(element.get_text())
			input('Digite')
