# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:16:30 2018

@author: luiscar
"""

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import  PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal,LTPage,LTTextBox,\
            LTTextLine,LTChar,LTAnno





def uso_basico():
    # Open a PDF file.
    fp = open('sefip.pdf', 'rb')
    # Create a PDF parser object associated with the file object.
    parser = PDFParser(fp)
    # Create a PDF document object that stores the document structure.
    doc = PDFDocument(parser)
    # Connect the parser and document objects.
    parser.set_document(doc)
    #doc.set_parser(parser)
    # Supply the password for initialization.
    # (If no password is set, give an empty string.)
    #doc.initialize(password)
    # Check if the document allows text extraction. If not, abort.
    #if not doc.is_extractable:
    #    raise PDFTextExtractionNotAllowed
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    # Create a PDF device object.
    device = PDFDevice(rsrcmgr)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in doc.get_pages():
        interpreter.process_page(page)

def analisar_layout():
    
    
    document = open('sefip.pdf','rb')
    rscrmgr = PDFResourceManager()
    laparams = LAParams()
    
    device = PDFPageAggregator(rscrmgr,laparams = laparams)
    interpreter = PDFPageInterpreter(rscrmgr,device)
    #para cada PDFPage
    for page in PDFPage.get_pages(document):
        
        interpreter.process_page(page)
        #obtem o LTPage
        layout = device.get_result()
        
        #para cada element em LTPage
        tabela = {}
        
        for element in layout:
            if isinstance(element,LTTextBoxHorizontal):
                lista = tabela.get(element.bbox[0],[])
                print(element.x0,element.y0,element.get_text())
                if not lista:
                    tabela[element.bbox[0]] = lista    
                lista.append(element.get_text())
                
                #print(element.get_text())
        #for index in sorted(tabela.keys()):
        #    print(index,tabela[index])
            #print(tabela[index])
            #print(index," ".join(tabela[index]))
        return
    document.close()

    #def preencher_tabela(lt_page):
class PDFPageDetailedAggregator(PDFPageAggregator):
    def __init__(self, rsrcmgr, pageno=1, laparams=None):
        PDFPageAggregator.__init__(self, rsrcmgr, pageno=pageno, laparams=laparams)
        self.rows = []
        self.page_number = 0
    def receive_layout(self, ltpage):        
        def render(item, page_number):
            if isinstance(item, LTPage) or isinstance(item, LTTextBox):
                for child in item:
                    render(child, page_number)
            elif isinstance(item, LTTextLine):
                child_str = ''
                for child in item:
                    if isinstance(child, (LTChar, LTAnno)):
                        child_str += child.get_text()
                child_str = ' '.join(child_str.split()).strip()
                if child_str:
                    row = (page_number, item.bbox[0], item.bbox[1], item.bbox[2], item.bbox[3], child_str) # bbox == (x1, y1, x2, y2)
                    self.rows.append(row)
                for child in item:
                    render(child, page_number)
            return
        render(ltpage, self.page_number)
        self.page_number += 1
        self.rows = sorted(self.rows, key = lambda x: (x[0], -x[2]))
        self.result = ltpage

        
def pdf_to_text(filename):
    
    cvpage = []
    
    fp = open(filename, 'rb')
    
    parser = PDFParser(fp)
    
    doc = PDFDocument(parser)
    
    rsrcmgr = PDFResourceManager()
    
    laparams = LAParams()
    
    device = PDFPageDetailedAggregator(rsrcmgr, laparams=laparams)
    
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    for page in PDFPage.create_pages(doc):
    
        interpreter.process_page(page)
        
        cvpage.append(device.rows)
    
    return cvpage

def gerar_log(funcionarios):
    
    f = open("exemplo_pdf.txt","w")
    
    for i,funcionario in enumerate(funcionarios):
        f.writelines("#" * 80)
        f.writelines("\n")
        f.writelines("Pagina: {}".format(i + 1))
        f.writelines("\n")       
        f.writelines("\n")
        for ch,vl in funcionario.items():
            f.writelines("{} - {}".format(ch,vl))
            f.writelines("\n")
    
    f.close()

def get_rows_page(rows,num_page):
    return [ row for row in rows if row[0] == num_page]

def gerar_log_layout(rows):
    
    row_atual = -1
    
    f = open("exemplo_pdf_layout.txt","w")
    
    for row in rows:
        
        if row[0] > row_atual:
            row_atual = row[0]
            f.writelines("#" * 80 )
            f.writelines("Linha {}".format(row_atual + 1))
            f.writelines("\n")
        
        if row[0] == row_atual:
            f.writelines(row.__repr__())
            f.writelines("\n")
        
            
    f.close()
  
    
layout_pg_relacao_trabalhadores = {(683.0, 530.254):"DATA_RELATORIO",
                                   (113.0, 521.254):"VERSAO_SEFIP",
                                   (254.0, 521.254):"VERSAO_TABELA",
                                   (729.0, 521.254):"HORA_RELATORIO",
                                   (724.0, 512.254):"PAGINA",
                                   (266.0, 500.254):"TIPO_PAGINA_1_1",
                                   (223.0, 490.254):"TIPO_PAGINA_1_2",
                                   (281.0, 490.254):"TIPO_ARQUIVO_2_1",
                                   (223.0, 480.254):"TIPO_ARQUIVO_2_2"}
funcionarios = []    
funcionario = {}
        
if __name__ == '__main__':
    
    #cvpage = pdf_to_text('sefip.pdf')
    cvpage = []
    
    
    fp = open("sefip.pdf", 'rb')
    
    
    parser = PDFParser(fp)
    
    doc = PDFDocument(parser)
    
    
    rsrcmgr = PDFResourceManager()
    
    
    laparams = LAParams()
    
    
    device = PDFPageDetailedAggregator(rsrcmgr, laparams=laparams)
        
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    lt_pages = PDFPage.create_pages(doc)
    
    #num_paginas = len(lt_pages)
    
    for page in lt_pages:
    
        interpreter.process_page(page)
        
        cvpage.append(device.rows)
    
    #print(doc.g)
    
    pagina = -1
        
    for paginas in cvpage:      
        gerar_log_layout(paginas)
        for row in paginas:           
            if pagina < row[0]:
                pagina = row[0]
                
                if funcionario:                   
                    funcionarios.append(funcionario)
                    funcionario = {}
            if pagina == row[0]:                    
                indice = (row[1],row[2])
                if layout_pg_relacao_trabalhadores.get(indice):
                    funcionario[layout_pg_relacao_trabalhadores[indice]] = row[5]
     
    gerar_log(funcionarios)
    print("execução finalizada")
    