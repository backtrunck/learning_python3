# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 08:57:27 2018

@author: luiscar
"""


from tkinter import *
from pdf_tools import LeitorPDF, BancoPaginaTexto

class LabelXY(Label):
    def __init__(self,pos_x, pos_y,**kargs):
        
        super().__init__(**kargs)
        self.pos_x = pos_x
        self.pos_y = pos_y
        
class FramePDF(Frame):
     def __init__(self,pag_texto,parent=None):
        super().__init__(parent)
        self.pag_texto = pag_texto
        


def converte_coordenadas(x,y,max_x,max_y):
    return (int(x),int(max_y + 9 - y),)

def on_left_click(event):
    print("Got left mouse")
    show_pos_event(event)

def show_pos_event(event):
    
    pg_txt = event.widget.master.pag_texto
    
    linha = pg_txt.get_linha_texto(0,event.widget.pos_y)
    
    janela = Toplevel(event.widget.master)
    
    for i in linha:
        Label(janela,text = i,borderwidth = 1,relief =  SOLID).pack(side = LEFT )
    
    #for i in range(10):
    #    pagina, coordenada_y = pg_txt.get_pagina_coordenada(0,i)
    #    print(pg_txt.get_linha_coordenada(pagina,coordenada_y))
    print(pg_txt.paginas[0])
    
    
    
        
    
    
    print(linha)
    

if __name__ == '__main1__':
    
    root = Tk()
    frame1 = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
    frame1.pack()
    frame1.pack_propagate(False)
    
    Entry(frame1).pack()
    
    
    frame2 = Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=100, height=100, bd= 0)
    frame2.pack()
    frame2.pack_propagate(False)
    
    Entry(frame2).pack()
    
    root.mainloop()
    
    
    
if __name__ == '__main__':
    
    root = Tk()
    
    root.title("Teste PDF TextBoxs")
    
    
    with open('sefip.pdf','rb') as fp:
        
        #obtendo paginas do pdf
        leitor = LeitorPDF(fp)
        
        paginas,geometria = leitor.get_texto_pagina([0,],1)
        
        max_x = geometria[0][3]
        
        max_y = geometria[0][4]
        
        root.geometry("{}x{}".format(max_x + 200,max_y + 200))
        
        
        linha1 = FramePDF(BancoPaginaTexto(paginas),root)
        #linha1 = Frame(root)
        #linha1.pack(fill=BOTH,expand = 1)
        linha1.config(height = max_x + 200, width=max_y + 200,relief=SUNKEN)
        linha1.place(x=0,y=0)
        bt_proximo = Button(linha1,text="proximo", width = 10) #,height=1,width=10    
        
        bt_anterior = Button(linha1,text="anterior", width = 10) #,height=1,width=10    
        
        max_x += 15
        
        #max_y += 85
        
        bt_proximo.place(x = max_x - 200, y = max_y - 20)
        
        bt_anterior.place(x = max_x - 400, y = max_y - 20)
        
        for pagina in paginas:
            posx,posy=converte_coordenadas(pagina[1],pagina[2],max_x,max_y)
            widget = LabelXY(pagina[1],pagina[2],master=linha1,text= pagina[5],relief=SOLID,bd=1,font=("Helvetica", "5"),\
                  padx=0,pady=0)
            widget.place(x=posx,y=posy)
            widget.bind('<Button-1>',on_left_click)
                          
        
        root.mainloop()


    