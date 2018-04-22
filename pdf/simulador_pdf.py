# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 08:57:27 2018

@author: luiscar
"""
def converte_coordenadas(x,y,max_x,max_y):
    return (x,max_y - y,)

from tkinter import *
from pdf_tools import LeitorPDF

if __name__ == '__main__':
    
    import sys 
    
    import os 

    caminho_base = os.path.abspath(os.path.dirname(__file__))

    sys.path.insert(0,os.path.join(caminho_base , '..'))

    caminho_base,pasta_atual = os.path.split(caminho_base)  
    
    root = Tk()
    
    root.title("Teste PDF TextBoxs")
    
    with open('sefip.pdf','rb') as fp:
        #obtendo paginas do pdf
        leitor = LeitorPDF(fp)
        
        paginas,geometria = leitor.get_texto_pagina([1,],1)
        
        max_x = geometria[0][3]
        
        max_y = geometria[0][4]
        
        #root.geometry("{}x{}".format(max_x,max_y))
        frm = Frame(root,bg="green")
        frm.pack()
        LabelFrame(frm,text="teste").pack()
        #for pagina in paginas:
        #    LabelFrame(frm,height=pagina[3] - pagina[1],width = pagina[4] - pagina[2],text= pagina[5]).place()
            
        
        root.mainloop()


    
