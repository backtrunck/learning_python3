# encoding: utf-8
import os, sys, re

from unicodedata import normalize
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

def test_backup():
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

def obter_nome_normalizado(arquivo, caracter_substitutivo='.'):
    """"Pega um nome de arquivo e retorna um nome de arquivo normalizado ou seja troca espaços por um ponto, retira caracteres não ascii, 
                troca caracteres acentuados por não acentuados
                Parâmetros:
                arquivo: caminho para o arquivo que vai ser renomeado
                caracter_substitutivo: (string) o caracter que vai substituir os espaços,'-' e '_' no nome do arquivo final
                
                retorno: (string) o novo nome do arquivo com seu caminho completo, para se utilizado numa operação de renomeação
    """
    
    caminho = os.path.normpath(arquivo)
    #se o arquivo não existir retorna erro
    if  not os.path.exists(caminho):
        raise FileNotFoundError
    else:
        #pega somente o nome do arquivo
        nome_base_arquivo = os.path.basename(caminho)
       
       #pega somente o caminho do arquivo
        caminho_arquivo = os.path.dirname(caminho)        
        
        #coloca o nome em letras minusculas e troca espaços por pontos        
        nome_base_arquivo = nome_base_arquivo.lower()
        
        nome_base_arquivo = re.sub(r'[\s\-]', caracter_substitutivo, nome_base_arquivo)
        
        #retira caracteres não ascii e retira os acentos
        nome_base_arquivo = normalize('NFKD', nome_base_arquivo).encode('ASCII', 'ignore').decode('ASCII')
      
        #troca tudo que não for letras,numeros, ponto ou traços por string vazia  
        nome_base_arquivo = re.sub(r'[^a-zA-Z0-9_\.]', '', nome_base_arquivo)
        
        #troca as repetições de pontos por um ponto
        nome_base_arquivo = re.sub(r'\.+', '.', nome_base_arquivo)
        
        #se o caracter substitutivo for diferente de '.', troca este carater pelo caracter substitutivo
        if caracter_substitutivo != '.':
            nome_base_arquivo = re.sub(r'\.', caracter_substitutivo, nome_base_arquivo)
        
        return os.path.join(caminho_arquivo, nome_base_arquivo)

def normalizar_arquivo(arquivo,  caracter_substitutivo='.'):
    """"Normaliza (renomeia) o nome do arquivo ou seja troca espaços por um ponto, retira caracteres não ascii, 
                    troca caracteres acentuados por não acentuados"""
    #pega o nome do arquivo normalizado
    arquivo_normalizado = obter_nome_normalizado(arquivo, caracter_substitutivo)
    #se o nome antigo é diferente do novo, o arquivo pode ser renomeado
    if arquivo_normalizado != arquivo:
        #verifica se o arquivo renomeado já existe na pasta (desnecessário renomear)
        if  not os.path.isfile(arquivo_normalizado):
            os.rename(arquivo, arquivo_normalizado)

def normalizar_pasta(pasta, recursivo = False, operacoes = [], caracter_substitutivo='.'):
    """Normaliza todos os arquivos de uma  pasta 
            Parâmetros:
                pasta: Pasta onde se encontram os arquivos a serem renomeados
                recursivo: (True/False) Se vai renomear as subpastas
                operacoes: (lista) com tuplas de strings do tipo (caminho,nome_arquivo_velho, nome_arquivo_novo), 
                                    utilzada para realizar as operações de renomeações
                caracter_substitutivo: (string) o caracter que vai substituir os espaços, '-' e '_' no nome do arquivo final
                
                retorno:   sem retorno, utilizar o parametro operações para realizar as renomeações posteriormente
    """            
    #pasta ou arquivo existe?
    if os.path.exists(pasta):
        #Não é um arquivo? (ou é uma pasta?)
        pasta = os.path.abspath(pasta)
        if not os.path.isfile(pasta):
           
            #é uma pasta. Percorre subpastas e arquivos desta pasta
            for arq in os.listdir(pasta): 
                #é um arquivo?
                if os.path.isfile(os.path.join(pasta, arq)):
                    #obtem o nome normalizado
                    nome_novo = os.path.basename(obter_nome_normalizado(os.path.join(pasta, arq), caracter_substitutivo))
                    #nome novo é diferente do antigo. Se forem iguais não precisa renomear
                    if arq !=nome_novo:
                        #guarda para posterior operação de renomeação
                        operacoes.append((pasta, arq,nome_novo))                    
                else:
                    #não é um arquivo é uma subpasta
                    #verifica se é um link de uma subpasta.
                    if not os.path.islink(os.path.join(pasta, arq)):
                        #caso não seja um link de pasta e a opção recursivo for True, entra na subpasta para renomear
                        if recursivo:
                                #chamada recursiva para renomear todos os arquivos e subpasta da pasta atual
                                normalizar_pasta(os.path.join(pasta, arq), recursivo, operacoes, caracter_substitutivo)
                        #Após renomear todos os arquivos da pasta atual, renomeia a pasta atual        
                        nome_novo = os.path.basename(obter_nome_normalizado(os.path.join(pasta, arq), caracter_substitutivo))
                        #nome novo é diferente do antigo. Se forem iguais não precisa renomear
                        if arq !=nome_novo:
                            #guarda para posterior operação de renomeação
                            operacoes.append((pasta, arq,nome_novo))
                            
def renomear_arquivos(pasta, recursivo = False, operacoes = [], caracter_substitutivo='.'):
    """ Renomeia (normaliza) todos os arquivos de uma pasta. 
            Parâmetros:
                pasta: Pasta onde se encontram os arquivos a serem renomeados
                recursivo: (True/False) Se vai renomear as subpastas
                operacoes: (lista) com tuplas de strings do tipo (caminho,nome_arquivo_velho, nome_arquivo_novo), 
                                    utilzada para realizar as operações de renomeações
                caracter_substitutivo: (string) o caracter que vai substituir os espaços,'-' e '_' no nome do arquivo final
    """
    
    
    normalizar_pasta(pasta, recursivo, operacoes, caracter_substitutivo)
    
    #usado para a impressão da barra de hashes
    i=0
    #loop em operações para realizar as renomeações de cada arquivo
    for caminho, nome_antigo, nome_novo in operacoes:
        #print(os.path.join(caminho, nome_antigo), os.path.join(caminho, nome_novo))
        #shutil.move(os.path.join(caminho, nome_antigo), os.path.join(caminho, nome_novo))
        i+=1
        print_hash_bar(i, len(operacoes))
        
    
    
def teste_normalizar_pasta(pasta, recursivo = False, operacoes = [], caracter_substitutivo='.'):
    #normaliza a pasta
    normalizar_pasta(pasta, recursivo, operacoes, caracter_substitutivo)
    #imprime saida
    for i in operacoes:
        print("Pasta: {}, Arq. Origem: {}, Arq. Destino: {}".format(i[0], i[1], i[2]))

def print_hash_bar(item_atual, qt_itens, max=50):
    """ Imprime uma barra de #'s indicando o progresso de uma operação: 
    Parametros:
        item_atual: indice do item que esta sendo processado
        qt_itens: quantidade de itens a serem processados
        max: quantidade de hashes a serem visualizados quando a operação chegar em 100%"""
   
   #Calcula modulo.
    modulo = qt_itens / max
   #calcula a quantidade hashes a serem visualizados neste momento
    qt_hash = int(item_atual /modulo)
    #inicializa hashes
    hashes = ''
    
    #Coloca qt_hashes (#) em hashes
    while (qt_hash > 0 ):
        if (len(hashes) <= max):
            hashes +='#'
        qt_hash-=1
            
    # impressão da barra de hashes
    print('[', end='')
    #Todo, ver uma forma de gerar o formato de maneira dinâmica ({}) qdo max mudar alterar 
    #o espaçamento do formato
    formato = '{:50}'.format(hashes)
    print(formato, end='')
    print(']', end='')
    
    #fim da impressão de hashes
    #volta o cursor 50 vezes, para que na proxima impressão, dê a impressa de que a barra de hash
    #está aumentando
    #TODO: quando se colocar o formato dinâmica colocar "range(max)"
    for i in range(50):
        print('\r', end='')
    #se for o ultimo item a ser impresso (100%), quebra a linha no final da barra.    
    if item_atual >= qt_itens :
        print('')
    
if __name__ == "__main__":
    
   renomear_arquivos("/media/lcreina/afrodite/teste_python", recursivo=True, caracter_substitutivo='.')
   #renomear_arquivos("/media/lcreina/afrodite/x", caracter_substitutivo='.')
   #renomear_arquivos(".")
    #renomear_arquivos("arquivos_testes")
    #renomear_arquivos("..")
