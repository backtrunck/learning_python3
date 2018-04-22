# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:29:23 2018

@author: luiscar
"""
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBox,LTTextLine,LTPage,\
                            LTChar,LTAnno



class PDFPageDetailedAggregator(PDFPageAggregator):
    def __init__(self, rsrcmgr, pageno=1, laparams=None):
        PDFPageAggregator.__init__(self, rsrcmgr, pageno=pageno, laparams=laparams)
        self.rows = []
        self.pages_geometry = []
        self.page_number = 0
    def receive_layout(self, ltpage):        
        def render(item, page_number):
            if isinstance(item, LTPage) or isinstance(item, LTTextBox):
                if isinstance(item,LTPage):
                    self.pages_geometry.append(item.bbox)
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


class LeitorPDF():
    
    def __init__(self,pdf_arquivo):
        """ 
        parâmetros:
            pdf_page (objeto PDFPage) uma pagina de um arquivo pdf
            campos (dict) dicionario com o formato 'nome_do_campo:coordenada_
                   do_campo', utilizado para ler locais específicos da página 
                   do pdf
        """                     
        self.pdf_arquivo = pdf_arquivo
        
        self.rscrmgr = PDFResourceManager()
     
        self.laparams = LAParams()
     
        self.device = PDFPageDetailedAggregator(self.rscrmgr,\
                                                laparams=self.laparams)
     
        self.interpreter= PDFPageInterpreter(self.rscrmgr, self.device)
    
    
    def get_texto_pagina(self,pagenos=None, maxpages=0):
        """
        Obtem um lista com todas os textos e suas respectivas posições relati-
        vas nas paginas procuradas (pagenos)
        parametros:
            pagenos (set) conjunto de paginas a ser procurada
            maxpages (int) quantidade de páginas máximas a ser procurada
        retorno (lista) Lista com o seguinte formato (num_pagina,x0,y0,x1,y1
                ,texto)
                (lista) Geometria da página no formato(num_pagina,x,y,
                        dimx,dimy)
        """
        pages_geometry = []
        
        paginas = self.get_pages(pagenos,maxpages)
        
        if paginas:
            rscrmgr = PDFResourceManager()
     
            laparams = LAParams()
     
            device = PDFPageDetailedAggregator(rscrmgr, laparams=laparams)
     
            interpreter= PDFPageInterpreter(rscrmgr, device)
        
        for pagina in paginas:
            
            interpreter.process_page(pagina)
            
        for i,g in enumerate(device.pages_geometry):
            
            pages_geometry.append((pagenos[i],g[0],g[1],g[2],g[3],))
            
        return ([(pagenos[i],j,k,l,m,n) for (i,j,k,l,m,n) in device.rows],\
                pages_geometry,)
        
        
    def ler_pagina_tabular(self,num_pages,linha_inicio_leitura,\
                           linha_fim_leitura,campos_alvo):
        """
        parâmetros:
            num_page (int) número da página a ser lida
            linha_inicio_leitura (int) linha onde deve começar a leitura
            linha_fim_leitura (int) linha onde deve terminar a leitura
            campos_alvo (dict) dicionario com o formato 
              'nome_do_campo:coordenada_do_campo', utilizado para ler 
              locais específicos da página do pdf
        retorno (dict) dicionario com as chaves constantes em campos_alvo
        e os valores extraídos do pdf
        """
        paginas = []
        
        pdf_pages = self.get_pages(num_pages,1)
        
        for num_page in num_pages:
            
            campos_pagina = get_campos_pagina(num_page,\
                                              linha_inicio_leitura,\
                                              linha_fim_leitura,\
                                              campos_alvo)
            paginas.append(num_page,campos_pagina)
            
            return paginas
        
    def get_paginas_numeradas(self,pagenos=None, maxpages=0, password='',
                  caching=True, check_extractable=True):
        
        # Create a PDF parser object associated with the file object.
        parser = PDFParser(self.pdf_arquivo)
        
        # Create a PDF document object that stores the document structure.
        doc = PDFDocument(parser, password=password, caching=caching)
        
        # Check if the document allows text extraction. If not, abort.
        if check_extractable and not doc.is_extractable:
            raise PDFTextExtractionNotAllowed('Text extraction is not allowed: %r' % fp)
       
        # Process each page contained in the document.
        for (pageno, page) in enumerate(PDFPage.create_pages(doc)):
            if pagenos and (pageno not in pagenos):
                continue
            
            yield (pageno,page)
            
            if maxpages and maxpages <= pageno+1:
                break
        return
    
    def get_pages(self,numeros_paginas=set(),qt_maxima_paginas=0):
        """
        Obtem determinadas páginas de um pdf
        parâmetros: 
            numeros_paginas (set) lista com as paginas a serem recupera-
                            das.
            qt_maxima_paginas (int) Quantidade máxima de paginas, 0 para
                              recuperar todas.
        """
        
        pdf_pages = PDFPage.get_pages(self.pdf_arquivo,\
                                      pagenos = numeros_paginas,\
                                      maxpages = qt_maxima_paginas)
        return pdf_pages
        
    
    def get_campos_pagina(self,pdf_page,linha_inicio_leitura,\
                           linha_fim_leitura,campos_alvo):
        
           campos_valores = {}
        
           self.interpreter.process_page(pdf_page)
        
           #obtem o LTPage
           
           linhas = self.device.rows
            
           for nm_campo,coordenada in campos_alvo.items():
                if coordenada[1] >= linha_inicio_leitura and \
                   coordenada[1] <= linha_fim_leitura:
                       for linha in linhas:
                          texto = self.get_text_coordenada(linha,coordenada)
                          if texto:
                              campos_valores[nm_campo] = texto
                
           return campos_valores
                                        
    def get_text_coordenada(self,objeto,coordenada,):
        
        texto = ''
        
        if objeto[1] == coordenada[0] and objeto[2] == coordenada[1]:
            texto = objeto[5]
        
        return texto
                       
class LeitorTabularPaginaPDF():
        """ Classe para ler paginas pdf que estejam em formato tabular """
        
        def __init__(pdf_page,campos,inicio_leitura,\
                 linhas_por_registros):
            """
            parametros:
                inicio_leitura (int) linha onde devem ser iniciadas as leituras
                linhas_por_registro (int) informa se cada registro esta em uma
                                    ou mais linhas de informação
            """
            
            super.__init__(pdf_page,area_leitura)
            
        def obterProximaLinha():
            pass

if __name__ == "__main__":
    
    campos_alvo = {"DATA_RELATORIO"     :(719.0, 530.254),
                   "VERSAO_SEFIP"       :(113.0, 521.254),
                   "VERSAO_TABELA"      :(254.0, 521.254),
                   "HORA_RELATORIO"     :(729.0, 521.254),
                   "PAGINA"             :(724.0, 512.254),
                   "TIPO_PAGINA_1_1"    :(266.0, 500.254),
                   "TIPO_PAGINA_1_2"    :(223.0, 490.254),
                   "TIPO_ARQUIVO_2_1"   :(281.0, 490.254),
                   "TIPO_ARQUIVO_2_2"   :(223.0, 480.254)}
    
    with open('sefip.pdf','rb') as fp:
        #obtendo paginas do pdf
        leitor = LeitorPDF(fp)
        
        leitor.get_texto_pagina([1,],1)
    #    paginas = leitor.get_paginas_numeradas(pagenos = {1,}, maxpages = 1)
        
    #    for num_pagina,pdf_page in paginas:
    #        print(pdf_page.mediabox)
    #        campos_valores = leitor.get_campos_pagina(pdf_page,480,531,\
    #                                                      campos_alvo)
    #        for ch,vl in campos_valores.items():
    #            print("campo {}:{}".format(ch,vl))
    #exit(0)
        
        
