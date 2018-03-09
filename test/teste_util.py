import sys 
import os 

caminho_base = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0,os.path.join(caminho_base , '..'))

caminho_base,pasta_atual = os.path.split(caminho_base)


from util import converte_monetario_float,eh_valor_monetario,formata_nome_empresa 

def teste_eh_valor_monetario():
    print("Teste valor monetario")
    print("abrindo arquivo: %s " % os.path.join(caminho_base,'arquivos_testes/teste_monetario'))

    arquivo = open(caminho_base + '/arquivos_testes/teste_monetario')
    for linha in arquivo:
        lista = linha.strip().split()
        if eh_valor_monetario(lista[0]) != int(lista[1]):
            print("Erro -> {}".format(lista[0]))
        else:
            print("Ok -> {}".format(lista[0]))
            if int(lista[1]) == 1:
                print(converte_monetario_float(lista[0], "Real"))


def teste_nome_empresa():
    print("Teste nome empresa")
    print("abrindo arquivo: %s " % os.path.join(caminho_base,'arquivos_testes/teste_monetario'))

    arquivo = open(caminho_base + '/arquivos_testes/teste_nome_empresa.txt')
    for linha in arquivo:
        lst = linha.split(";")
        print("linha->", lst[0].strip())
        print("formata_nome_empres->", formata_nome_empresa(lst[0]))
if __name__ == '__main__':

    teste_eh_valor_monetario()
    teste_nome_empresa()
