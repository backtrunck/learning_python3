#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#parametros de teste
#C:\projetos\test\arquivos_testes\workspace_origem C:\projetos\test\arquivos_testes\workspace_destino R


import sys
import os

caminho_base = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0,os.path.join(caminho_base , '..'))

caminho_base,pasta_atual = os.path.split(caminho_base)

from backup import renomear_arquivos,  normalizar_pasta

def teste_normalizar_pasta(pasta, recursivo = False, operacoes = [], \
                           caracter_substitutivo='.'):
    #normaliza a pasta
    normalizar_pasta(pasta, recursivo, operacoes, caracter_substitutivo)
    #imprime saida
    for i in operacoes:
        print("Pasta: {}, Arq. Origem: {}, Arq. Destino: {}".format(i[0], \
              i[1], i[2]))
 

def teste_renomear_arquivos():
    
    qt_argumentos = len(sys.argv)
    if qt_argumentos < 2 or qt_argumentos > 3:
        print("A sintaxe do comando está incorreta, informe a pasta " + \
               "cujos nomes de arquivo devem ser normalizados")
        print("Ex: renomear_arquivos <pasta> <recursão>")
        exit(1)
        
    pasta = sys.argv[1]
    if not os.path.exists(pasta):
        print("Pasta inexistente {}".format(sys.argv[1]))
        exit(1)
    
    if os.path.isfile(pasta) or os.path.islink(pasta):
        print("renomear_arquivo espera receber uma pasta. {} não é uma pasta"\
                    .format(pasta))
        exit(1)
    if len(sys.argv) == 3:
        recursao  = sys.argv[2]
    
        if recursao.upper() == 'R':
            renomear_arquivos(pasta, True)
        else:
            print("Opção inválida: {}. Use 'R' para renomear recursivamente"\
                        .format(recursao))
    else:
            renomear_arquivos(pasta)

if __name__ == '__main__':
    teste_renomear_arquivos()
