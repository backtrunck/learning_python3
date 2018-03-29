#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#parametros de teste
#C:\projetos\test\arquivos_testes\workspace_origem C:\projetos\test\arquivos_testes\workspace_destino R


import sys,os
import datetime

(ESQUERDA,CENTRO,DIREITA) = range(3)


caminho_base = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0,os.path.join(caminho_base , '..'))

caminho_base,pasta_atual = os.path.split(caminho_base)

from backup import Pasta,Backup

def teste_backup():

    if len(sys.argv) < 4:
        print("A sintaxe do comando está incorreta, informe a pasta de " + \
               "origem, pasta de destino e tipo da operação")
        print("Ex: backup <origem> <destino> <tipo de operação>")
        print("\n\t<origem> = 'caminho para a pasta onde se encontram os " +  \
              "arquivos a serem copiados'")
        print("\t<destino> = 'caminho para a pasta que vai receber a " + \
              "copia dos arquivos'")
        print("\t<tipo de operação> = \t'R' -> 'Relatório', gera um " + \
              "relatório do que vai ser feito caso se execute a operação " + \
              "com os parãmetros passados")
        print("\t\t\t\t'E' -> 'Executar', executa o backup da pasta " + \
              " <origem> na pasta <destino>")
    else:
        #Pega o caminho de origem passado
        caminho_pasta_origem = sys.argv[1]
        #Pega o caminho de destino passado
        caminho_pasta_destino = sys.argv[2]
        #Pega o tipo da operação
        tipo_operacao = sys.argv[3]

        if not os.path.exists(caminho_pasta_origem):
            print("Caminho para pasta de origem inválido: ", \
                  caminho_pasta_origem)
        elif not os.path.exists(caminho_pasta_destino):
            print("Caminho para pasta de destino inválido: ", \
                  caminho_pasta_destino)
        elif tipo_operacao.upper() != 'E' and tipo_operacao.upper() != 'R':
            print("Tipo de Operação inválida, digite: ")
            print("\t'R' para 'Relatório',  ou 'E' -> 'Executar'")
        else:
            
            sufixo_data = datetime.datetime.now().strftime("%Y_%m_%d")
            
            f = open("teste_backup_%s.%s" % (sufixo_data,"txt"),"w")
            
            escrever_cabecalho(" Teste Backup ",f)
            
            msg = "Pasta de Origem"
            
            f.writelines(linha_log(msg,caracter='',alinhamento=ESQUERDA))
            
            pasta_origem = Pasta(sys.argv[1])
            
            msg = pasta_origem.obter_caminho()
            
            f.writelines(linha_log(msg,caracter='',alinhamento=ESQUERDA))
           
            msg = "Pasta de Destino"
            
            f.writelines(linha_log(msg,caracter='',alinhamento=ESQUERDA))
            
            pasta_destino = Pasta(sys.argv[2])
            
            msg = pasta_destino.obter_caminho()
            
            f.writelines(linha_log(msg,caracter='',alinhamento=ESQUERDA))
            
            novo_backup = Backup(pasta_origem,pasta_destino)
            
            novo_backup.analisa_backup()
            
            if tipo_operacao == 'R':
                
                escrever_cabecalho(" Pastas a serem criadas ",f)
                pastas = novo_backup.obter_operacoes_criar_pastas()
                
                if pastas:
                    for pasta in pastas:
                        f.writelines(linha_log(pasta,caracter='',\
                                                        data_hora=True,\
                                                        alinhamento=ESQUERDA))
                        f.writelines("\n")
                else:
                    msg = "Nenhuma Pasta a ser criada"
            
                    f.writelines(linha_log(msg,caracter='',\
                                           alinhamento=ESQUERDA))
                    
                escrever_cabecalho(" Operacoes de cópia",f)
                
                for operacao in novo_backup.obter_operacoes_copiar():
                    
                    f.writelines(\
                                 linha_log(\
                                        operacao[2] + \
                                        " <-\t\t" + operacao[0],\
                                        caracter='',\
                                        data_hora=True,\
                                        alinhamento=ESQUERDA))
                    
                escrever_cabecalho(" Resumo",f)
                   
                msg = "Quantidade de bytes necessários no destino: {}".\
                                       format(novo_backup.obter_qt_bytes())
                
                f.writelines(linha_log(msg,alinhamento=ESQUERDA,\
                                       caracter=''))
                
                msg = "Quantidade de arquivos a serem copiados: {}".\
                                       format(novo_backup.obter_qt_arquivos())
                
                f.writelines(linha_log(msg,alinhamento=ESQUERDA,\
                                       caracter=''))
                
                msg = "Relatório de arquivos por pasta"
                
                f.writelines(linha_log(msg,alinhamento=ESQUERDA,\
                                       caracter=''))
                
                for (chave,valor) in novo_backup.\
                        obter_qt_arquivos_por_sub_pasta().items():
                    f.writelines(linha_log("{} - {}".format(chave,valor)\
                                           ,alinhamento=ESQUERDA,\
                                           caracter=''))
            else:
                
                msg = "Criando Pastas"
            
                f.writelines(linha_log(msg,caracter='',data_hora=True,\
                                       alinhamento=ESQUERDA))
            
                novo_backup.criar_novas_pastas()
                
                msg = "Pastas Criadas"
            
                f.writelines(linha_log(msg,caracter='',data_hora=True,\
                                       alinhamento=ESQUERDA))
                                       
                msg = "Copiando Arquivos"
            
                f.writelines(linha_log(msg,caracter='',data_hora=True,\
                                       alinhamento=ESQUERDA))
                
                novo_backup.copiar_arquivos()
                
                msg = "Arquivos Copiados"
            
                f.writelines(linha_log(msg,caracter='',data_hora=True,\
                                       alinhamento=ESQUERDA))
                          
            f.close()        
            
def linha_log(msg='',tam_linha=100,caracter='*',\
                       quebra_linha = True,alinhamento=CENTRO,data_hora=False):
    """ Gera um linha formatada para inserção em arquivos
        parametros:
            msg (string) mensagem a ser formatada
            tam_linha (inteiro) tamanho da linha
            alinhamento (inteiro) Alinhamento a Esquerda, Direita,Centro
            data_hora (boolean) Informa se a mensagem da linha será precedida
                      pela data hora atual
        retorno (string) linha formatada.
        
        Ex: linha_log('teste',tam_linha=9,caracter='#',alinhamento=CENTRO),
            resulta em: '##teste##' """
    
    if alinhamento == CENTRO:
        alin = '^'
    elif alinhamento == DIREITA:
        alin = '>'
    else:
        #ESQUERDA
        alin = '<'
        
    frt = "{:" + caracter + alin + str(tam_linha) + "}"
    
    if data_hora:
        dt_hr = "[" +  datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%f") + "]"
        msg = dt_hr + " " + msg
            
            
    if quebra_linha:
        return frt.format(msg) + "\n"
    else:
        return frt.format(msg) 

def escrever_cabecalho(msg,arquivo):
    arquivo.writelines(linha_log())
    arquivo.writelines(linha_log(msg))
    arquivo.writelines(linha_log())

    

if __name__ == '__main__':
    teste_backup()
