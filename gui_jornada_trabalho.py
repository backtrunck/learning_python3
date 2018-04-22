#coding=utf-8

import datetime
from tkinter import *
from tkinter import messagebox
from interfaces_graficas.quitter import Quitter
from jornada_trabalho import verificar_horario,tempo_registrar_volta_almoco\
                            ,obter_hora_saida

fields = 'Entrada Manhã', 'Saída Manhã', 'Entrada Tarde'

def calculo_automatico(entries):
    """
    Calcula e mostra todos os horarios (considerando uma jornada de 7h:20min
    a partir do horario de entrada da manhã e preenche todos os campos de
    horários da tela, considerandos o horário de saída da manhã como 4 horas
    após o horário de entrada e o horário de entrada da tarde a partir de 1 hora
    do horário de sáida da manhã.
    ##################################################################
    parametros:
        - entries (lista) , Lista de tkinter.entry mais um tkinter.label cons-
        tantes da janela principal.
    retorno:
        -  Sem retorno. Preenche as entry de horários (sáida manhã e entrada
        tarde, bem com as label que informam as previsões de horário de modo
        a totalizar 7h:20min de jornada.
    ##################################################################
    """
    resultado = verificar_horario(entries[0].get())
    if not resultado[0]:
        messagebox.showerror("Erro","Horário Inválido % s"\
                                             % entries[0].get())
    else:
        hrs = []
        hrs.append(resultado[1])
        #hrs[1] = hrs[0] + 4 horas (saida para almoço)
        hrs.append(hrs[0] + datetime.timedelta(seconds=14400))
        #hrs[2] = hrs[1] + 1 hora (entrada do almoço)
        hrs.append(hrs[1] + datetime.timedelta(seconds=3600))

        #obtem a hora de saída
        hrs.append(obter_hora_saida(*hrs))
        entries[1].delete(0,END)
        entries[1].insert(0,hrs[1].strftime("%H:%M"))
        entries[2].delete(0,END)
        entries[2].insert(0,hrs[2].strftime("%H:%M"))

        altera_label_horario(entries[3],entries[4],hrs)





def fetch(entries):
    #lista para guardar os horarios [entrada_manha,saida_manha,entrada_tarde]
    hrs = []
    #loop pelos widget da janela
    for entry in entries:
        #print('Input =>"%s"' % entry.get())
        #se for caixa de texto, verifica se o horario foi corretamente digitado
        if type(entry) is Entry:
            if entry.get():
                resultado = verificar_horario(entry.get())
                if not resultado[0]:
                    messagebox.showerror("Erro","Horário Inválido % s"\
                                             % entry.get())
                    #limpa os labels
                    entries[3].config(text=" ")
                    entries[4].config(text=" ")
                    return 1
                else:
                    hrs.append(resultado[1])
            else:
                messagebox.showerror("Erro","Horários devem ser preenchidos")
                #limpa os labels
                entries[3].config(text=" ")
                entries[4].config(text=" ")
                return 1

    hrs.append(obter_hora_saida(*hrs))

    altera_label_horario(entries[3],entries[4],hrs)



def altera_label_horario(lbl1,lbl2,hrs):
    #altera o label de horário
    lbl1.config(text="%s - %s / %s - %s" % \
                            (hrs[0].strftime("%H:%M"),\
                             hrs[1].strftime("%H:%M"),\
                             hrs[2].strftime("%H:%M"),\
                             hrs[3].strftime("%H:%M")))

    #pega mensagem com o tempo que falta para registro após almoço
    msg = tempo_registrar_volta_almoco(hrs[1])

    if msg:
        lbl2.config(text = msg)
    else:
        lbl2.config(text = " ")

    #messagebox.showinfo("Horário",msg)


def make_form(root,fields):
    entries = []
    #criação dos textBox e labels a partir da lista fields
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text= field)
        ent = Entry(row)
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT,expand=YES,fill=X)
        #lab.pack(side=LEFT)
        #ent.pack(side=RIGHT,expand=YES,fill=X)
        entries.append(ent)
    row = Frame(root)
    #label para os horários
    labHorario = Label(row,text=" ")

    row.pack(side=TOP,fill=X)

    labHorario.pack(side=LEFT,fill=X)

    entries.append(labHorario)

    row = Frame(root)
    #label para o informar tempo restante
    labTempoRestante = Label(row,text=" ")
    row.pack(side=TOP,fill=X)
    labTempoRestante.pack(side=LEFT,fill=X)
    entries.append(labTempoRestante)
    entries[0].focus_set()
    return entries


if __name__ == '__main__':
    root = Tk()
    root.title("Cálculo Horários")
    root.iconbitmap('xclock.ico')
    ents = make_form(root,fields)
    #root.bind('<Return>',(lambda event:fetch(ents)))
    ents[0].bind('<Return>',(lambda event:calculo_automatico(ents)))
    Button(root,text='Calcular',command=(lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()

