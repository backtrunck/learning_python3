#coding=utf-8
#-------------------------------------------------------------------------------
# Name:        ler_pdf_sefip
# Purpose:
#
# Author:      luiscar
#
# Created:     07/03/2018
# Copyright:   (c) luiscar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re, sys,os
import PyPDF2


from pdfminer.layout import LAParams
from pdfminer.converter import PDFResourcerManager, PDFPageAggregator
from pdfminer.pdfpage   import PDFPage
from pdfminer.layout    import LTTextBoxHorizontal

PADRAO_BUSCA = r'(\d){3}\.(\d){5}\.\d\d-\d'

def main():

    if len(sys.argv) < 2:
        print("Sintaxe inválida: usar: ler_pdf_sefip /caminho/arquivo")
        exit(1)

    caminho,nome_arquivo = os.path.split(sys.argv[1])

    #verifica se a diretório exist
    if not os.path.isdir(caminho):
        print("Diretório Não Existe: %s" % caminho)
        exit(1)

    #verifica se o arquivo passado é válido
    if not nome_arquivo :
        print("Arquivo inválido: %s" % sys.argv[1])
        exit(1)

    try:
        arquivo_pdf = open(os.path.join(caminho,nome_arquivo),'rb')

    except Exception as e:
        print("Erro ao abrir arquivo: %s" % e.__class__.__name__)
        exit(e.errno)

    pdf_reader = PyPDF2.PdfFileReader(arquivo_pdf)

    num_pages = pdf_reader.getNumPages()

    print("Numero de Páginas: %d" % num_pages )
    print("")
    dados_funcionarios = []
    for num_page in range(num_pages):
        page = pdf_reader.getPage(num_page)
        itens_texto = page.extractText().split('\n')
        for indice,item_texto in enumerate(itens_texto):
       	    if re.match(PADRAO_BUSCA,item_texto):
                dados_funcionario = []

                for j in range(12):
                    dados_funcionario.append(itens_texto[indice + j])
                dados_funcionarios.append(dados_funcionario)

    for dado_funcionario in dados_funcionarios:
        print(dado_funcionario)
    arquivo_pdf.close()

def main2():
    if len(sys.argv) < 2:
        print("Sintaxe inválida: usar: ler_pdf_sefip /caminho/arquivo")
        exit(1)
        caminho,nome_arquivo = os.path.split(sys.argv[1])

    #verifica se a diretório exist
    if not os.path.isdir(caminho):
        print("Diretório Não Existe: %s" % caminho)
        exit(1)

    #verifica se o arquivo passado é válido
    if not nome_arquivo :
        print("Arquivo inválido: %s" % sys.argv[1])
        exit(1)

    try:
        arquivo_pdf = open(os.path.join(caminho,nome_arquivo),'rb')

    except Exception as e:
        print("Erro ao abrir arquivo: %s" % e.__class__.__name__)
    exit(e.errno)



if __name__ == '__main__':
    main()
