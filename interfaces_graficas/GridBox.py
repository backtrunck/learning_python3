#coding=utf-8
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      luiscar
#
# Created:     05/03/2018
# Copyright:   (c) luiscar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *

class GridBox(Frame):

    def __init__(self,master,linhas=2,colunas=2,tem_cabecalho=NO,dados=None,**kw):
        self.__grade = []
        self.__cabecalho = []
        self.__frame_cabecalhos = None
        self.__frame_grade = None

        self.tem_cabecalho = tem_cabecalho
        super().__init__(master,**kw)
        frame_pai = master

        if self.tem_cabecalho:
            self.frame_cabecalhos = Frame(self)
            self.frame_cabecalhos.pack(side=TOP,expand=YES,fill=X)

            self.__criar_cabecalho(['1','2'])

        for i in range(linhas):
            coluna = []
            self.__frame_grade = Frame(self)
            self.__frame_grade.pack(side=TOP,expand=YES,fill = X)
            for j in range(colunas):
                e = Entry(self.__frame_grade)
                e.pack(side=LEFT,expand=YES,fill = X)
                coluna.append(e)

            self.__grade.append(coluna)

    def __criar_cabecalho(self,titulos_colunas):
        """ criar um cabecalho novo
            Parâmetros:
                titulos_colunas (list) lista com os titulos(string) das colunas
            Retorno:
                None: Sem retorno"""
        if self.tem_cabecalho:
            for i,titulo in enumerate(titulos_colunas):
                l = Label(self.frame_cabecalhos,border=1,borderwidth=1,relief=RIDGE,text = titulo)
                l.pack(side=LEFT,expand=YES,fill = X)
                self.__cabecalho.append(l)

    def preencher_cabecalho(self,lista_cabecalho):
        """ Preenche os titutos do cabecalho
            Parâmetros:
                lista_cabecalho (list) lista com os titulos (string) das colunas)
        """
        if self.tem_cabecalho:
            if len(self.__cabecalho) != len(lista_cabecalho):
                raise CabecalhoIndexError('Erro - Números de Cabeçalhos inválidos')

            for index,titulo in enumerate(lista_cabecalho):
                self.__cabecalho[index].config(text = titulo)

    def preencher_grade(self,conteudo):
        pass

    def __limpar_cabecalho(self):

        if self.tem_cabecalho:
            if self.__cabecalho:
                for label in self.__cabecalho:
                    label.destroy()
                self.__cabecalho = []

    def limparGrade(self,limpa_cabecalho=NO):
        """ Limpa todo o grid box, retirando todas as linhas e colunas
            Parametros:
                limpa_cabecalho (BOOLEAN) YES/NO, informa se vai limpar o
                cabeçalho
            Retorno:
                Sem retorno """


        linhas = len(self.__grade)
        if linhas:
            colunas = len(self.__grade[0])

        for i in range(linhas):
            for j in range(colunas):
                self.__grade[i][j].destroy()

        if limpa_cabecalho:
            self.__limpar_cabecalho()

        self.__grade = []

class CabecalhoIndexError(Exception):
    pass

def main():

    root = Tk()

    g = GridBox(root,tem_cabecalho=NO)
    g.pack(side=TOP)

    g.preencher_cabecalho(['primeiro','segundo'])

    bt = Button(root,text="Limpar")
    bt.pack(side=TOP,expand=YES,fill=X)
    bt.bind('<ButtonRelease-1>',g.limparGrade)

    root.mainloop()

if __name__ == '__main__':
    main()
