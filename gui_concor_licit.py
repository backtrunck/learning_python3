#coding=utf-8
#-------------------------------------------------------------------------------
# Name:        gui_licit_concor
# Purpose:
#
# Author:      luiscar
#
# Created:     27/02/2018
# Copyright:   (c) luiscar 2018
# Licence:     Livre
#-------------------------------------------------------------------------------
from utilitarios.terminal import ProgressMeter
from tkinter import *
from interfaces_graficas.ListBoxFeeder import ListBoxFeeder
from interfaces_graficas.GridBox import GridBox
from tkinter.messagebox import showinfo
import tkinter.ttk as ttk

from interfaces_graficas.quitter import Quitter
from utilitarios.validadores import validar_cnpj
import concor_licit

class TelaConcorLicit:
    def __init__(self,conexao):
        self.conexao = conexao
        self.lst_box_feeder1 = None
        self.lst_box_feeder2 = None
        self.progrees_bar = None

    def make_form(self,root):

        linha1 = Frame(root,bg="green")
        coluna1 = Frame(linha1)
        coluna2 = Frame(linha1)
        fbotoes1 = Frame(coluna1)
        fbotoes2 = Frame(coluna2)

        linha1.pack(side = TOP,  fill = BOTH)
        coluna1.pack(side = LEFT,fill = BOTH,expand=YES)
        coluna2.pack(side = LEFT,fill = BOTH,expand=YES)

        #coluna1
        lbl_frm = LabelFrame(coluna1,text='Cnpjs Principais ')
        lbl_frm.pack(side=TOP,fill = BOTH, expand=YES,padx=5,pady=5)
        lista1 = ['teste','teste']
        self.lst_box_feeder1 = ListBoxFeeder(lbl_frm,list_content = [])
        self.lst_box_feeder1.pack(side=LEFT)

        #coluna2
        lbl_frm = LabelFrame(coluna2,text='Cnpjs Secundários')
        lbl_frm.pack(side=TOP,fill = BOTH,padx=5,pady=5)
        lista2 = ['bora bora','bora bora']
        self.lst_box_feeder2 = ListBoxFeeder(lbl_frm,list_content = [])
        self.lst_box_feeder2.pack(side=LEFT)

        #botao de execução
        lbl_frm = Frame(root)
        lbl_frm.pack(side = TOP, fill = BOTH)
        lbl_frm_execucao = LabelFrame(lbl_frm,text='Progresso')
        lbl_frm_execucao.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
        self.progrees_bar = ttk.Progressbar(lbl_frm_execucao, orient='horizontal', mode='determinate')
        self.progrees_bar.pack(fill=BOTH,expand=YES,padx=5,pady=5)

        bt_executar = Button(lbl_frm,text="Executar") #,height=1,width=10
        bt_executar.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)

        bt_executar.bind('<ButtonRelease-1>',self.__executar)

        #Grid
        lbl_frm = Frame(root)
        lbl_frm.pack(side = TOP,  fill = BOTH,expand=YES)
        self.grid_resultados = GridBox(lbl_frm,linhas=8,colunas=8)
        self.grid_resultados.pack(side=TOP,expand=YES,fill=BOTH)

        #outras linhas
        linha3 = Frame(root,bg="blue")
        linha3.pack(side = TOP,  fill = BOTH)
        Label(linha3,text='Exportar').pack(side=TOP)

        #for verify the value of entry box (CNPJ)
        self.lst_box_feeder1.validator = lambda x:self.validar_cnpj_empresa(x)
        self.lst_box_feeder2.validator = lambda x:self.validar_cnpj_empresa(x)

    def __executar(self,event):

        cnpjs_principais = self.lst_box_feeder1.get_all_keys()
        if not cnpjs_principais:
            showinfo(title='Aviso', message= "Ao menos informe o(s) CNPJ(s) Principa(is)!")
        else:
            #p = ProgressMeter()
            self.progrees_bar["value"] = 0
            #p.progress_bar = self.progrees_bar
            cnpjs_secundarios = self.lst_box_feeder2.get_all_keys()

            if cnpjs_secundarios:
                if len(cnpjs_principais) == 1:
                    concor_licit.obter_licitacoes_um_pra_muitos(self.conexao,cnpjs_principais,cnpjs_secundarios,self.progrees_bar)
                else:
                    cnpjs_principais.extend(cnpjs_secundarios)
                    resultset = concor_licit.obter_licitacoes_muitos_pra_muitos(self.conexao,cnpjs_principais,self.progrees_bar)
                    if resultset:
                        licitacoes = resultset.fetchall()
                        self.grid_resultados.preencher_grade(licitacoes)

            else:
                if len(cnpjs_principais) > 1:
                    concor_licit.obter_licitacoes_muitos_pra_muitos(self.conexao,cnpjs_principais,self.progrees_bar)
                else:
                    pass
                    #TODO - consultar licitações de um único cnpj

    def validar_cnpj_empresa(self,cnpj):

            if not cnpj:
                showinfo(title = 'Aviso',message='Digite o Cnpj!')
                return False

            else:

                if not validar_cnpj(cnpj):
                    showinfo(title = 'Aviso',message='Cnpj inválido!')
                    return False

            return True

def main():

    root = Tk()
    #root.geometry("600x400")
    root.title("Concorrentes em Licitação")
    conexao = concor_licit.obter_conexao(concor_licit.HOST,concor_licit.PORTA,concor_licit.BANCO_DADOS,'luiscar','#qoataqfdsj33')
    tela = TelaConcorLicit(conexao)
    tela.make_form(root)
    Quitter(root).pack(side=RIGHT)

    root.mainloop()

    conexao.close

if __name__ == '__main__':
    main()
