# encoding: utf-8
import os
import sys
class Pasta():

    def __init__(self,caminho):
        self.caminho = os.path.abspath(caminho)

    def obter_caminho(self):
        """ Mostra o caminho da pasta"""
        return self.caminho

    def obter_lista_conteudo(self):
        """ Retorna o conteúdo da pasta: subpastas e arquivos"""
        if os.path.exists(self.caminho):
            return [os.path.join(self.caminho,arq) for arq in os.listdir(self.caminho)]
        else:
            return[]

    def obter_lista_arquivos(self):
        """ Retorna somente os arquivos dentro da pasta"""
        if os.path.exists(self.caminho):
            return [arq for arq in self.obter_lista_conteudo() if os.path.isfile(arq)]
        else:
            return []

    def obter_lista_sub_pastas(self):
        """ Retorna somente as subpastas dentro da pasta"""
        ##TO DO: não retornar links para arquivos
        if os.path.exists(self.caminho):
            return [arq for arq in self.obter_lista_conteudo() if not os.path.isfile(arq)]
        else:
            return[]

class Backup():
    #operacoes: lista de tuplas do tipo (arquivo,pasta_origem,pasta_destino)
    #este atributo estatico conterá os dados necessários para realizar o backup
    #cp pasta_origem/arquivo pasta_destino/arquivo"
    operacoes = []

    def __init__(self,pasta_origem,pasta_destino):
        self.pasta_origem = pasta_origem
        self.pasta_destino = pasta_destino
        #self.sub_pastas_finalizadas = []
        self.sub_pastas_nao_finalizadas = pasta_origem.obter_lista_sub_pastas()

    def analisa_backup(self):
        """ Verifica quais arquivos da pasta_origem e respectivas subpastas precisam ser copiados para pasta_destino nas respectivas subpastas"""
        #enquanto existir subpasta na pasta atual, faça backup recursivo
        while(self.sub_pastas_nao_finalizadas):
            #pega ultima pasta da lista
            sub_pasta = self.sub_pastas_nao_finalizadas[-1]
            #cria um objeto backup, a partir da criação de um objeto pasta (com base na subpasta de origem) e de uma sub_pasta de mesmo nome na pasta de destino
            #não é necessário que esta subpasta na pasta de destino exista. Após a criação do objeto Backup, chama-se o método analisa_backup, que por meio de
            #recursão varre todas as subpastas verificando a necessidade de backup
            Backup(Pasta(sub_pasta),Pasta(os.path.join(self.pasta_destino.obter_caminho(),os.path.basename(sub_pasta)))).analisa_backup()
            #subpasta finalizada, retira a mesma da lista
            self.sub_pastas_nao_finalizadas.pop()

        #Pega somente o nome do arquivo a partir de uma lista com os caminhos absolutos de cada arquivo
        arquivos_origem = [os.path.basename(arq) for arq in self.pasta_origem.obter_lista_arquivos()]
        arquivos_destino = [os.path.basename(arq) for arq in self.pasta_destino.obter_lista_arquivos()]

        for arquivo_origem in arquivos_origem:
            #Verifica se o arquivo de origem esta na pasta de destino, caso não esteja, deve ser feito o backup"
            if arquivo_origem not in arquivos_destino:
                #insere na lista operacao, um tupla (arquivo,pasta_origem,pasta_destino) de modo a que no final o backup seja realizado"
                self.__class__.operacoes.append((arquivo_origem,self.pasta_origem.obter_caminho(),self.pasta_destino.obter_caminho()))

    def obter_operacoes_backup(self):
        """Retorna as operacoes necessárias para realizar o backup, deve-se previamente ter executado self.analisa_backup"""
        #retorna uma lista de strings do tipo "pasta_origem/arquivo pasta_destino/arquivo
        return [" ".join((os.path.join(pst_orig,arq),os.path.join(pst_dest,arq)))for (arq,pst_orig,pst_dest) in self.__class__.operacoes]

    def obter_qt_bytes(self):
        """Retorna a quantidade de bytes necessárias para realizar o backup"""
        total_bytes = 0
        for operacao in self.__class__.operacoes:
            total_bytes = os.path.getsize(os.path.join(operacao[1],operacao[0]))

        return total_bytes
    def obter_qt_arquivos(self):
        """Retorna a quantidade de arquivos que vão ser copiados da pasta de origem para pasta de destino"""
        return len(self.__class__.operacoes)

    def obter_qt_arquivos_por_sub_pasta(self):
        """Retorna a quantidade de arquivos que vão ser copiados por subpasta de origem para pasta de destino"""
        sub_pastas = {}

        for operacao in self.__class__.operacoes:
            if operacao[1] not in sub_pastas.keys():
                sub_pastas[operacao[1]] = 1
            else:
                sub_pastas[operacao[1]]+=1

        return sub_pastas




if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("A sintaxe do comando est� incorreta, informe a pasta de origem, pasta de destino e tipo da opera��o")
        print("Ex: backup <origem> <destino> <tipo de opera��o>")
        print("\n\t<origem> = 'caminho para a pasta onde se encontram os arquivos a serem copiados'")
        print("\t<destino> = 'caminho para a pasta que vai receber a copia dos arquivos'")
        print("\t<tipo de opera��o> = \t'R' -> 'Relat�rio', gera um relat�rio do que vai ser feito " +\
              "caso se execute a opera��o com os par�metros passados")
        print("\t\t\t\t'E' -> 'Executar', executa o backup da pasta <origem> na pasta <destino>")
    else:
        #Pega o caminho de origem passado
        caminho_pasta_origem = sys.argv[1]
        #Pega o caminho de destino passado
        caminho_pasta_destino = sys.argv[2]
        #Pega o tipo da opera��o
        tipo_operacao = sys.argv[3]

        if not os.path.exists(caminho_pasta_origem):
            print("Caminho para pasta de origem inv�lido: ", caminho_pasta_origem)
        elif not os.path.exists(caminho_pasta_destino):
            print("Caminho para pasta de destino inv�lido: ", caminho_pasta_destino)
        elif tipo_operacao.upper() != 'E' and tipo_operacao.upper() != 'R':
            print("Tipo de Opera��o inv�lida, digite: ")
            print("\t'R' para 'Relat�rio',  ou 'E' -> 'Executar'")
        else:
            print("Arquivos de Origem")
            pasta_origem = Pasta(sys.argv[1])
            print(pasta_origem.obter_caminho())
            print(pasta_origem.obter_lista_conteudo())


            #print(pasta_origem.obter_lista_arquivos())
            #print(pasta_origem.obter_lista_sub_pastas())

            print("Pasta de Destino")
            pasta_destino = Pasta(sys.argv[2])
            print(pasta_destino.obter_caminho())
            print(pasta_destino.obter_lista_conteudo())
            #print(pasta_destino.obter_lista_arquivos())
            #print(pasta_destino.obter_lista_sub_pastas())

            print("Analise backup")
            novo_backup = Backup(pasta_origem,pasta_destino)
            novo_backup.analisa_backup()
            print(novo_backup.obter_operacoes_backup())
            #print("Quantidade de bytes necessários no destino: ",novo_backup.obter_qt_bytes())
            #print("Quantidade de arquivos a serem copiados: ",novo_backup.obter_qt_arquivos())
            #print("Relatório de arquivos por pasta",novo_backup.obter_qt_arquivos_por_sub_pasta())
