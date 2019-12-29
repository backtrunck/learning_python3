from tkinter import * 
#COR_DE_FUNDO = "gray9"
COR_DE_FUNDO = "gray25"
COR_DA_FONTE = "IndianRed2"

class LabelV1(Frame):
        def __init__(self, parent = None,labelSup="Label Superior", **config):
                #background = 
                Frame.__init__(self,parent,relief=SOLID,bg=COR_DE_FUNDO,**config)
                self.textLabelSuperior = labelSup 
                self.labelSuperior = Label(self,text=self.textLabelSuperior,\
                                           fg=COR_DA_FONTE,\
                                           bg=COR_DE_FUNDO,\
                                           justify=RIGHT)

                self.labelSuperior.pack(side=TOP,anchor=W)
                self.labelInferior = Label(self,text="-",\
                                           fg=COR_DA_FONTE,\
                                           bg=COR_DE_FUNDO,\
                                           font=("Helvetica", 20),\
                                           justify=RIGHT)

                self.labelInferior.pack(side=RIGHT,anchor=E)

        def setLabelInferior(self,txtLabel):
                self.labelInferior.config(text=txtLabel)

        def setLabelSuperior(self,txtLabel):
                self.labelSuperior.config(text=txtLabel)

                


if __name__ == '__main__':
        root = Tk()
        root.configure(bg=COR_DE_FUNDO)

        frm1 = Frame(root)
        frm1.pack(side=TOP)
        frm2 = Frame(root)

        lblTemperatura = LabelV1(frm1,labelSup="Temperatura")
        lblTemperatura.setLabelInferior("27°")
        lblTemperatura.pack(side=LEFT,anchor=E)

        lblUmidade = LabelV1(frm1,labelSup="Umidade")
        lblUmidade.setLabelInferior("95%")
        lblUmidade.pack(side=LEFT,anchor=E)

        lblUmidade = LabelV1(frm1,labelSup="Umidade Solo")
        lblUmidade.setLabelInferior("1000")
        lblUmidade.pack(side=LEFT,anchor=E)

        lblUmidade = LabelV1(frm1,labelSup="Luminosidade")
        lblUmidade.setLabelInferior("120LUX")
        lblUmidade.pack(side=LEFT,anchor=E)
        
        btSair = Button(frm2,\
                        text="Sair",\
                        bg="gray23",\
                        activebackground="gray23",\
                        highlightbackground="gray23",\
                        font=("Helvetica", 23),\
                        relief=FLAT,\
                        foreground="white")
        #btSair = Button(frm2,\
        #                text="Sair",\
        #                bg="gray16",\
        #                activebackground="gray15",\
        #                highlightbackground="IndianRed2",\
        #                foreground="IndianRed2")

        btSair.pack(side=RIGHT,anchor=E)
        frm2.pack(side=RIGHT)
        root.mainloop()


