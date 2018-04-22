# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:29:23 2018

@author: luiscar
"""
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBox,LTTextLine,LTTextBoxHorizontal,LTPage,\
                            LTChar,LTAnno

from collections import defaultdict

#formato da lista de conteúdo de cada pagina pdf
NUM_PAGINA,POS_X,POS_Y,TAM_X,TAM_Y,TEXTO = range(6)



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
class CoordenadasInvalidas(Exception):
    pass

class BancoPaginaTexto():
    
    def __init__(self,texto_paginas):
        self.texto_paginas = texto_paginas
        
        #criando conjunto {pagina , coordenada_y} onde será possível saber 
        #quantas linhas distintas tem cada página
        mapa_de_linhas = set()
        
        self.paginas = defaultdict(list)
        
        for pagina, coord_x, coord_y,tam_x,tam_y,texto in texto_paginas:
            
            mapa_de_linhas.add((pagina,coord_y,))
            
            self.paginas[pagina].append((coord_x,coord_y,tam_x,tam_y,texto,))
            
        #criando lista ordenada a partir do conjunto {pagina , coordenada_y}
        
        self.__mapa_de_linhas = sorted(list(mapa_de_linhas),key=lambda x: (x[0],-x[1]))
        
    def get_coordenada_relativa(self,num_pagina,num_coordenada,deslocamento):
        """ obtem a proxima coordenada relativa ao deslocamento. Ex: Se 
        deslocamento = 2, pega a coordenada duas posições a frente de
        num_coordenada. Retorna -1 se não for encontrada a coordenada """
        try:
            indice = self.__mapa_de_linhas.index((num_pagina, num_coordenada, ))
            indice += deslocamento
            return self.__mapa_de_linhas[indice][1]
        except ValueError:
            return -1
        pass
        
    def get_pagina(self,num_pagina):
        """Obtem uma lista com todos os objetos num determinada pasta """
        return self.paginas[num_pagina]
    
    def get_coordenada(self,num_pagina,num_linha):        
        """obtem uma tupla do tipo (num_pagina,coordenada) a partir do numero 
        da pagina passada e do número relativo a linha da página), 
        faz a conversão de linha para coordenada dentro da pagina
        parâmetros:
            num_pagina (int) numero da pagina
            num_linha (int) número da linha que se quer resgatar
        retorno (tupla) (num_pagina,num_coordenada)
        """
    def get_objeto_texto(self,num_pagina,coordenada):
        linhas = [texto for coord_x,coord_y,tam_x,tam_y,texto\
                      in self.get_pagina(num_pagina)
                      if coord_x == coordenada[0] and 
                         coord_y == coordenada[1]]
        if len(linhas) == 1:
            return linhas[0]
        elif len(linhas) == 0:
            return ""
        else:
            raise CoordenadasInvalidas( \
              "Não foi possível encontrar objeto {}:{} na página {}".format(\
                            coordenada[0],coordenada[1],num_pagina))
        
        #obtem todas as coordenadas_y da pagina passada(num_pagina)
        linhas_pagina = [l for l 
                             in self.__mapa_de_linhas 
                             if l[0] == num_pagina]
        
        #pega a pagina e a coordenada e passa para a função que irá retornar a linha
        return (num_pagina,linhas_pagina[num_linha][1])
        
    def get_linha_texto(self,num_pagina, coordenada_y):
        """obtem uma lista com os textos dos objetos que estão na mesma 
            coordenada_y (mesma linha) passada. 
        parâmetros:
            num_pagina (int) numero da pagina
            coordenada_y (int) similar ao número da linha
        retorno (list) todos os texto presentes naquela coordenada (linha)
        """
        
        return [linha[TEXTO] for linha in self.get_linhas(num_pagina,coordenada_y)]
    
    def get_linhas(self,num_pagina,coordenada_y1,coordenada_y2=-1):
        """obtem uma lista com os objetos em determinada linha (coordenada y)
        parâmetros:
            num_pagina (int) numero da pagina
            coordenada_y1 (int) similar ao número da linha
            coordenada_y2 (int) utilizada qdo se quer obter linhas de uma 
            determinada faixa entre coordenada_y1 e coordenada_y2
        retorno (list) todos os texto presentes naquela coordenada (linha) ou 
        algumas lista de texto dentro da faixa.
        """
        if coordenada_y1 > coordenada_y2:
            raise CoordenadasInvalidas("Faixa de captura inválida")
        
        if y2 == -1:
            return [linha for linha in self.texto_paginas if
                          linha[NUM_PAGINA] == num_pagina and \
                          linha[POS_Y] == coordenada_y1 ]
        else:
            return [linha for linha in self.texto_paginas if
                          linha[NUM_PAGINA] == num_pagina and \
                          linha[POS_Y] >= coordenada_y1 and
                          linha[POS_Y] <= coordenada_y2]
            
    def get_paginas(self):
        for i in range(len(self.paginas.keys())):
            yield self.paginas[i]

class AutenticadorPagina():
    """ Classe que verifica se a pagina atende aos critérios preestabelecidos """
    def __init__(self):
        self.campos = []
        
    def incluir_criterio(self,coordenadas_campo,valor_campo):
        """ inclui um critério a ser testado qdo for autenticar uma pagina. 
        A verificação consiste em verificar se determinado campo da pagina 
        contém determinado valor """
        self.campos.append((coordenadas_campo,valor_campo,))
        
    def retirar_criterio(self,coordenada):
        """ Retira um critério a ser testado qdo for autenticar uma pagina. 
        A verificação consiste em verificar se determinado campo da pagina 
        contém determinado valor """
        
        #Gera lista somente com as coordenadas dos critérios
        coordenadas = [coord for coord,valor in self.campos]
        try:
            #Pega o índice da coordenada passada
            indice = coordenadas.index(coordenada)
        except ValueError:
            indice = -1
        
        if indice != -1:
            self.campos.pop(indice)
        
    def autenticar(self,pagina):
        """ Verificar se os campos que definem os critérios estão presentes na 
        páginas e se seus valores são iguais """
        
        #cria lista só com as coordenadas dos objetos da pagina
        coordenadas_pagina = [(x,y,) for x,y,tam_x,tam_y,texto in pagina]
        #Loop nos campos autenticadores
        for coordenadas,valor in self.campos:
            try:
                #obtem indice do campo autenticador na página
                indice = coordenadas_pagina.index(coordenadas)
                #o valor do campo autenticador é igual ao campo da página?
                if pagina[indice][TEXTO-1] != valor:
                    return False
            except ValueError:
                #se não encontrou o campo autenticado na página
                return False
        return True
    
class ExtratorTexto():
    
    def __init__(self):
        self.campos_principais = []
        self.grupo_secundario = []
        
    def inserir_campo_principal(self,coordenada_x,coordenada_y):
        """Inserir os campos principais que vão ser extraidos de cada página"""
        coordenada = (coordenada_x,coordenada_y,)
        #já possui a coordenada?
        if coordenada not in self.campos_principais:
            self.campos_principais.append(coordenada)
            
    def retirar_campo_principal(self,coordenada_x,coordenada_y):
        """Retira o campo do rol de campos principias que vão ser extraídos"""
        coordenada = (coordenada_x,coordenada_y,)
        try:
            #encontra em que indice esta a coordenada
            indice = self.campos_principais.index(coordenada)
            #retira coordenada
            self.campos_principais.pop(indice)
        except ValueError:
            pass
    def criar_grupo_secundario(self,faixa,qt_linhas_registro):
        
        campos_secundarios = {}
        campos_secundarios["faixa"] = faixa
        campos_secundarios["campos"] = []
        campos_secundarios["qt_linhas_registro"] = qt_linhas_registro
        self.grupo_secundario.append(campos_secundarios)
        return (len (self.grupo_secundario)-1)
    
    def obter_textos_campos_principais(self,pagina,banco_pg_texto):
        textos = []
        for i in self.campos_principais:
            textos.append(banco_pg_texto.get_objeto_texto(pagina,i))
            
        return textos
    
    def obter_textos_campos_secundarios(self,pagina,banco_pg_texto,num_grupo):
        linha_texto = []
        linhas_textos = []
        campos_secundarios = self.grupo_secundario[num_grupo]
        linha_superior = campos_secundarios["faixa"].obter_linha_superior()
        linha_inferior = campos_secundarios["faixa"].obter_linha_inferior()
        
        while(linha_superior >= linha_inferior):
            for campo in campos_secundarios["campos"]:
                x, y = campo
                y = banco_pg_texto.get_coordenada_relativa(pagina,linha_superior,y)
                linha_texto.append(banco_pg_texto.get_objeto_texto(pagina,(x,y,)))
            linhas_textos.append(linha_texto)
            linha_superior -=campos_secundarios["qt_linhas_registro"]
            
        return linhas_textos
    
    def inserir_campo_secundario(self,indice,linha,coordenada):
        campos = self.grupo_secundario[indice]["campos"]
        campo = (coordenada,linha)
        if campo not in campos:
            campos.append(campo)
            
    def retirar_campo_secundario(self,indice,linha,coordenada):
        campos = self.grupo_secundario[indice]["campos"]
        campo = (linha,coordenada,)
        try:
            indice = campos.indice(campo)
            campos.pop(indice)
        except ValueError:
            pass
        
class FaixaPDF():
    
    def obter_linha_superior():
        pass
    
    def obter_linha_inferior():
        pass

class FaixaLinhasLimites(FaixaPDF):
    
    def __init__(self,linha_superior,linha_inferior):
        self.linha_superior = linha_superior 
        self.linha_inferior = linha_inferior
        
    def obter_linha_superior(self):
        return self.linha_superior
    
    def obter_linha_inferior(self):
        return self.linha_inferior


def main():
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
        
        paginas,geometria = leitor.get_texto_pagina([0,1,2,3,4,5],6)
        
        banco_paginas = BancoPaginaTexto(paginas)
        
        autenticador = AutenticadorPagina()
        autenticador.incluir_criterio((266.0,500.254,),\
         'RELAÇÃO DOS TRABALHADORES CONSTANTES NO ARQUIVO SEFIP')
        autenticador.incluir_criterio((223.0,490.254,),\
         'MODALIDADE : "BRANCO"-RECOLHIMENTO AO FGTS E DECLARAÇÃO À PREVIDÊNCIA')
        autenticador.retirar_criterio((266.0,500.254,))
        
        extrator =  ExtratorTexto()
        extrator.inserir_campo_principal(37.0, 530.254)
        extrator.inserir_campo_principal(683.0, 512.254)
        extrator.inserir_campo_principal(683.0, 512.254)
        extrator.inserir_campo_principal(724.0, 512.254)
        extrator.inserir_campo_principal(677.0, 430.254)
        faixa = FaixaLinhasLimites(354.254,75.254)
        num_grupo = extrator.criar_grupo_secundario(faixa,2)
        extrator.inserir_campo_secundario(num_grupo,0,41.0)
        extrator.inserir_campo_secundario(num_grupo,0,320.0)
        extrator.inserir_campo_secundario(num_grupo,1,93.0)
        
        
        num_pag = 0
        for pag in banco_paginas.get_paginas():
            num_pag += 1
            if autenticador.autenticar(pag):
                print("Pagina - {0}".format(num_pag))
                print(extrator.obter_textos_campos_principais(num_pag-1,banco_paginas))
                print(extrator.obter_textos_campos_secundarios(num_pag-1,banco_paginas,num_grupo))
                
        pass
                
    #    paginas = leitor.get_paginas_numeradas(pagenos = {1,}, maxpages = 1)
        
    #    for num_pagina,pdf_page in paginas:
    #        print(pdf_page.mediabox)
    #        campos_valores = leitor.get_campos_pagina(pdf_page,480,531,\
    #                                                      campos_alvo)
    #        for ch,vl in campos_valores.items():
    #            print("campo {}:{}".format(ch,vl))
    #exit(0)
        
if __name__ == "__main__":
        main()
