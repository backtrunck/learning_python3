#coding=utf-8

import datetime

def obter_horario(mensagem):
   """
   Obtem, do terminal, um horario no formato hora:minuto. Ex. 15:30
   ##################################################################
   parametros:
       - mensagem (string), mensagem a ser mostrada no terminal solicitando o
       horário.
   retorno:
       -  horario (datetime) horário informado.
   ##################################################################
   """
   horario_ok = False
   #loop até obter um horário válido
   while(not horario_ok):
        str_horario = input(mensagem)
        try:
            #horário no formato HH:MM
            horario = datetime.datetime.strptime(str_horario,"%H:%M")
        except ValueError:
            print("Horário inválido")
        else:
            horario_ok = True
   return horario

def verificar_horario(horario):
    """
    Verifica se uma string passada está no formato hora:minuto. Ex. 15:30, caso
    esteja uma lista com um boolean informando que é um horário True e a string
    transformada num datetime. Ex (True,datetime)
    ##################################################################
    parametros:
        - horario (string), horário
    retorno:
        -  (Boolean,datetime) (lista) lista informando no primeiro item
            se foi passado um horário válido e no segundo item o horário ou
            um None
    ##################################################################
    """
    try:
        #converte uma string num horário no formato HH:MM
        hr = datetime.datetime.strptime(horario,"%H:%M")
    except ValueError:
        #se horario inválido, retorna falso e um objeto Nulo
        return(False,None)
    else:
        #se horário válido, retorna True e um objeto DateTime
        return (True,hr)

def obter_qt_horas_minutos(qt_segundos):
    """
    Obtem, a quantidade de horas, minutos e segundos a partir de uma quantidade
    de segundos passasda.
    ##################################################################
    parametros:
        - qt_segundos (int), quantidade de segundos.
    retorno:
        -  (horas,minutos,segundos) (lista) Lista com a quantidade horas,
        minutos e segundos.
    ##################################################################
    """
    horas = qt_segundos // 3600
    segundos_restantes = qt_segundos % 3600
    minutos = segundos_restantes // 60
    qt_segundos = segundos_restantes % 60

    return (horas,minutos,qt_segundos,)

def obter_qt_horas_minutos_str(qt_segundos):
    """
    retorna a quantidade minutos constantes da quantidade de segundos passada.
    ##################################################################
    parametros:
        - qt_segundos (int), quantidade de segundos
    retorno:
        - qt_str (string) quantidade de minutos formatado
    ##################################################################
    """

    qt = obter_qt_horas_minutos(qt_segundos)
    qt_str = ''
    if qt[0]:
        qt_str = 'Horas %d ' % qt[0]
    if qt[1]:
        if qt[2]:
            qt_str += "%d minutos" % qt[1]
        else:
            qt_str += "%d minutos" % qt[1] + 1
    else:
        qt_str += "%d segundos" % qt[2]

    return qt_str

def obter_hora_saida(hr_ent_man,hr_sai_man,hr_ent_tar):
    """
    retorna o horario de saída mínimo de modo a totalizar 7h e 20min,
    a partir das informações passadas sobre horario de entrada e saída
    da manhã e entrada da tarde
    ##################################################################
    parametros:
        - hr_ent_man (datetime), horario entrada manhã
        - hr_sai_man (datetime), horario saída manhã
        - hr_ent_tar (datetime), horario entrada tarde
    retorno:
        - horario de saída (datetime) horário de saída da tarde
    ##################################################################
    """
    #intervalo (timedelta) entre a hora de entrada e saída da manhã
    qt_tempo = hr_sai_man - hr_ent_man
    #diferença entre 8h(26400s) e o tempo trabalhado na manhã. -> (tempo restante)
    tempo_restante = datetime.timedelta(seconds=26400) - qt_tempo
    #tempo restante mais hora de entrada da tarde para ter o horário de saída
    return hr_ent_tar + tempo_restante

def tempo_registrar_volta_almoco(hr_saida_almoco):
    """
    Retorna a quantidade de minutos mínimos que faltam para se registrar
    o horário de entrada do almoço
    ##################################################################
    parametros:
        - hr_saida_almoco (datetime), horario saída manhã
    retorno:
        - horario de saída (string) horário de saída da tarde
    ##################################################################
    """
    #soma a saída do almoço mais uma hora
    hr_entrada = hr_saida_almoco + datetime.timedelta(hours=1)
    #combina a data de hoje com a hora de entrada informada para ter um datetime que vai ser subtraido da data e hora atual
    if datetime.datetime.combine(datetime.datetime.today(),hr_entrada.time()) > datetime.datetime.now():
        intervalo =  (datetime.datetime.combine(datetime.datetime.today(),hr_entrada.time()) - datetime.datetime.now()).total_seconds()
    else:
        intervalo = 0

    if intervalo:
        return obter_qt_horas_minutos_str(intervalo)
    else:
        return ""


if __name__ == '__main__':

    opcao = 'n'
    while opcao.upper() != 'S':
        hr_entrada_manha = obter_horario('Horário de entrada - Manhã: ')
        hr_saida_manha = obter_horario('Horário de saída - Manhã: ')
        hr_entrada_tarde = obter_horario('Horário de entrada - Tarde: ')
        #qt_tempo = hr_saida_manha - hr_entrada_manha

        #tempo_restante = datetime.timedelta(seconds=26400) - qt_tempo

        #hr_saida_tarde = hr_entrada_tarde + tempo_restante

        hr_saida_tarde = obter_hora_saida(hr_entrada_manha,\
                        hr_saida_manha,hr_entrada_tarde)

        print(tempo_registrar_volta_almoco(hr_saida_manha))

        print("%s - %s / %s - %s" % (\
                hr_entrada_manha.strftime("%H:%M"),\
                hr_saida_manha.strftime("%H:%M"),\
                hr_entrada_tarde.strftime("%H:%M"),\
                hr_saida_tarde.strftime("%H:%M")))

        opcao = input("Deseja sair (S/N)?")


