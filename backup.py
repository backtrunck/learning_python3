# encoding: utf-8
import os
import  re
import shutil
from utilitarios.terminal import ProgressMeter
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
            return [os.path.join(self.caminho,arq) for arq in \
                    os.listdir(self.caminho)]
        else:
            return[]

    def obter_lista_arquivos(self):
        """ Retorna somente os arquivos dentro da pasta"""
        if os.path.exists(self.caminho):
            return [arq for arq in self.obter_lista_conteudo() \
                    if os.path.isfile(arq)]
        else:
            return []

    def obter_lista_sub_pastas(self):
        """ Retorna somente as subpastas dentro da pasta"""
        ##TO DO: não retornar links para arquivos
        if os.path.exists(self.caminho):
            return [arq for arq in self.obter_lista_conteudo() \
                    if not os.path.isfile(arq)]
        else:
            return[]

class Backup():
    #operacoes_copiar: lista de tuplas do tipo (arquivo,pasta_origem,
    #pasta_destino)
    #este atributo estatico conterá os dados necessários para realizar o backup
    #cp pasta_origem/arquivo pasta_destino/arquivo"
    operacoes_copiar = []
    operacoes_criar_pastas = []

    def __init__(self,pasta_origem,pasta_destino):
        self.pasta_origem = pasta_origem
        self.pasta_destino = pasta_destino
        #self.sub_pastas_finalizadas = []
        self.sub_pastas_nao_finalizadas = pasta_origem.obter_lista_sub_pastas()
        
    def obter_pastas_inexistentes_no_destino(self):
        """Obtem as pastas que devem ser criadas na pasta de destino """
        
        #laço em todas as subpasta da pasta de origem
        for pasta in self.sub_pastas_nao_finalizadas:
            
            #forma um path da pasta de destino com a subpasta da vez
            pasta_destino = os.path.join(self.pasta_destino.obter_caminho(),\
                                         os.path.basename(pasta))
            
            #verifica se a pasta de destino já existe, senão existir, inclui
            #na lista da operações para criação futura.
            if not os.path.exists(pasta_destino):
                self.__class__.operacoes_criar_pastas.append(pasta_destino)

    def analisa_backup(self):
        """ Verifica quais arquivos da pasta_origem e respectivas 
            subpastas precisam ser copiados para pasta_destino nas respectivas
            subpastas"""
        #obtem as pastas que precisam ser criadas na pasta de destino    
        self.obter_pastas_inexistentes_no_destino()
        
        #enquanto existir subpasta na pasta atual, faça backup recursivo
        while(self.sub_pastas_nao_finalizadas):
            
            #pega ultima pasta da lista
            sub_pasta = self.sub_pastas_nao_finalizadas[-1]
            
            #cria um objeto backup, a partir da criação de um objeto pasta 
            #(com base na subpasta de origem) e de uma sub_pasta de mesmo nome
            #na pasta de destino não é necessário que esta subpasta, na pasta 
            #de destino exista. Após a criação do objeto Backup, chama-se o 
            #método analisa_backup, que por meio de recursão varre todas as 
            #subpastas verificando a necessidade de backup
            Backup(Pasta(sub_pasta),Pasta(os.path.join(self.pasta_destino.obter_caminho(),os.path.basename(sub_pasta)))).analisa_backup()
            
            #subpasta finalizada, retira a mesma da lista
            self.sub_pastas_nao_finalizadas.pop()

        #Pega somente o nome do arquivo a partir de uma lista com os caminhos 
        #absolutos de cada arquivo
        arquivos_origem = [os.path.basename(arq) \
                        for arq in self.pasta_origem.obter_lista_arquivos()]
        
        arquivos_destino = [os.path.basename(arq) \
                        for arq in self.pasta_destino.obter_lista_arquivos()]

        for arquivo_origem in arquivos_origem:
            
            #Verifica se o arquivo de origem esta na pasta de destino, 
            #caso não esteja, deve ser feito o backup"
            if arquivo_origem not in arquivos_destino:
            
                #insere na lista operacao, um tupla (arquivo,pasta_origem,
                #pasta_destino) de modo a que no final o backup seja realizado"
                self.__class__.operacoes_copiar.append(\
                                        (arquivo_origem,\
                                         self.pasta_origem.obter_caminho(),\
                                         self.pasta_destino.obter_caminho())\
                                                      )

    def obter_operacoes_copiar(self):
        """Retorna as operacoes necessárias para realizar o backup, deve-se 
            previamente ter executado self.analisa_backup"""
        #retorna uma lista de strings do tipo "pasta_origem/arquivo 
        #pasta_destino/arquivo
        return self.__class__.operacoes_copiar

    def obter_operacoes_criar_pastas(self):
        return self.__class__.operacoes_criar_pastas
    
    def obter_qt_bytes(self):
        """Retorna a quantidade de bytes necessárias para realizar o backup"""
        total_bytes = 0
        for operacao in self.__class__.operacoes_copiar:
            total_bytes = os.path.getsize(\
                                         os.path.join(operacao[1],operacao[0]))

        return total_bytes
    
    def obter_qt_arquivos(self):
        """Retorna a quantidade de arquivos que vão ser copiados da pasta 
            de origem para pasta de destino"""
        return len(self.__class__.operacoes_copiar)

    def obter_qt_arquivos_por_sub_pasta(self):
        """Retorna a quantidade de arquivos que vão ser copiados por subpasta
        de origem para pasta de destino"""
        sub_pastas = {}

        for operacao in self.__class__.operacoes_copiar:
            if operacao[1] not in sub_pastas.keys():
                sub_pastas[operacao[1]] = 1
            else:
                sub_pastas[operacao[1]]+=1

        return sub_pastas
    
    def criar_novas_pastas(self):
        """ Cria as novas pastas na pasta de destino """
        for pasta in self.__class__.operacoes_criar_pastas:
            os.makedirs(pasta)
            
    def copiar_arquivos(self):
        
        qt_copias  = len(self.__class__.operacoes_copiar)
        
        p = ProgressMeter(valor_maximo=qt_copias)
        
        #mostar o progress meter vazio no terminal
        p.update_progress(0)
        
        for i, (arquivo,pasta_origem,pasta_destino) in \
            enumerate(self.__class__.operacoes_copiar):
                shutil.copy2(os.path.join(pasta_origem,arquivo),\
                             os.path.join(pasta_destino,arquivo))
                p.update_progress(i + 1)
        
def obter_nome_normalizado(arquivo, caracter_substitutivo='.'):
    """"Pega um nome de arquivo e retorna um nome de arquivo normalizado 
        ou seja troca espaços por um ponto, retira caracteres não ascii, 
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
        
        nome_base_arquivo = re.sub(r'[\s\-_]', caracter_substitutivo, \
                                   nome_base_arquivo)
        
        #retira caracteres não ascii e retira os acentos
        nome_base_arquivo = normalize('NFKD', \
                                      nome_base_arquivo).encode('ASCII', 'ignore').decode('ASCII')
      
        #troca tudo que não for letras,numeros, ponto ou traços 
        #por string vazia  
        nome_base_arquivo = re.sub(r'[^a-zA-Z0-9\.]', '', nome_base_arquivo)
        
        #troca as repetições de pontos por um ponto
        nome_base_arquivo = re.sub(r'\.+', '.', nome_base_arquivo)
        
        #se o caracter substitutivo for diferente de '.', 
        #troca este carater pelo caracter substitutivo
        if caracter_substitutivo != '.':
            nome_base_arquivo = re.sub(r'\.', caracter_substitutivo, \
                                       nome_base_arquivo)
        
        return os.path.join(caminho_arquivo, nome_base_arquivo)

def normalizar_arquivo(arquivo,  caracter_substitutivo='.'):
    """"Normaliza (renomeia) o nome do arquivo ou seja troca 
        espaços por um ponto, retira caracteres não ascii, 
        troca caracteres acentuados por não acentuados"""
    #pega o nome do arquivo normalizado
    arquivo_normalizado = obter_nome_normalizado(arquivo, \
                                                 caracter_substitutivo)
    #se o nome antigo é diferente do novo, o arquivo pode ser renomeado
    if arquivo_normalizado != arquivo:
        #verifica se o arquivo renomeado já existe na pasta (desnecessário 
        #renomear)
        if  not os.path.isfile(arquivo_normalizado):
            os.rename(arquivo, arquivo_normalizado)

def normalizar_pasta(pasta, recursivo = False, operacoes = [], \
                      caracter_substitutivo='.'):
    """Normaliza todos os arquivos de uma  pasta 
            Parâmetros:
                pasta: Pasta onde se encontram os arquivos a serem renomeados
                recursivo: (True/False) Se vai renomear as subpastas
                operacoes: (lista) com tuplas de strings do tipo 
                                   (caminho,nome_arquivo_velho, 
                                    nome_arquivo_novo), 
                                    utilzada para realizar as operações 
                                    de renomeações
                caracter_substitutivo: (string) o caracter que vai substituir
                                          os espaços, '-' e '_' no nome do 
                                          arquivo final
                
                retorno:   sem retorno, utilizar o parametro operações 
                            para realizar as renomeações posteriormente
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
                    nome_novo = os.path.basename(obter_nome_normalizado(\
                                                    os.path.join(pasta,\
                                                    arq), \
                                                    caracter_substitutivo))
                    #nome novo é diferente do antigo. Se forem iguais 
                    #não precisa renomear
                    if arq !=nome_novo:
                        #guarda para posterior operação de renomeação
                        operacoes.append((pasta, arq,nome_novo))   
                else:
                    #não é um arquivo é uma subpasta
                    #verifica se é um link de uma subpasta.
                    if not os.path.islink(os.path.join(pasta, arq)):
                        #caso não seja um link de pasta e a opção recursivo 
                        #for True, entra na subpasta para renomear
                        if recursivo:
                                #chamada recursiva para renomear todos os 
                                #arquivos e subpasta da pasta atual
                                normalizar_pasta(os.path.join(pasta, arq), \
                                                 recursivo, operacoes, \
                                                 caracter_substitutivo)
                        #Após renomear todos os arquivos da pasta atual, 
                        #renomeia a pasta atual        
                        nome_novo = os.path.basename(\
                                                obter_nome_normalizado( \
                                                    os.path.join(pasta, arq),\
                                                    caracter_substitutivo))
                        #nome novo é diferente do antigo. Se forem iguais 
                        #não precisa renomear
                        if arq !=nome_novo:
                            #guarda para posterior operação de renomeação
                            operacoes.append((pasta, arq,nome_novo))
    
def renomear_arquivos(pasta, recursivo = False, caracter_substitutivo='.'\
                      ,debug=0):
    """ Renomeia (normaliza) todos os arquivos de uma pasta. 
            Parâmetros:
                pasta: Pasta onde se encontram os arquivos a serem renomeados
                recursivo: (True/False) Se vai renomear as subpastas
                operacoes: (lista) com tuplas de strings do tipo (caminho,
                               nome_arquivo_velho, nome_arquivo_novo), 
                               utilzada para realizar as operações de 
                               renomeações
                caracter_substitutivo: (string) o caracter que vai substituir 
                               os espaços,'-' e '_' no nome do arquivo final
    """
    
    operacoes = []
    operacoes_nao_realizadas = []
    normalizar_pasta(pasta, recursivo, operacoes, caracter_substitutivo)
    
    p = ProgressMeter(valor_maximo = len(operacoes))
    
    p.update_progress(0)
    #loop em operações para realizar as renomeações de cada arquivo
    for i, (caminho, nome_antigo, nome_novo) in enumerate(operacoes):
              
        if debug == 0:
            #verifica se o arquivo novo já existe na pasta, se existir não realiza a operação
            if os.path.exists(os.path.join(caminho, nome_novo)):
                operacoes_nao_realizadas.append(os.path.join(caminho, nome_antigo))
            else:
                shutil.move(os.path.join(caminho, nome_antigo), os.path.join(\
                        caminho, nome_novo))
        else:
                print("Debug")
                
        p.update_progress(i + 1)
    print("{} arquivo(s) renomeados".format(len(operacoes) - \
                                                                            len(operacoes_nao_realizadas)))
    if operacoes_nao_realizadas:    
        
        print("Arquivos não renomeados, por já existirem, na pasta, outros "\
                    + "arquivos com mesmo nome normalizado")
                    
        for i, arquivo in enumerate(operacoes_nao_realizadas):
            print("{} - {}".format(i + 1, arquivo))

        
        

def print_hash_bar(item_atual, qt_itens, max=50):
    """ Imprime uma barra de #'s indicando o progresso de uma operação: 
    Parametros:
        item_atual: indice do item que esta sendo processado
        qt_itens: quantidade de itens a serem processados
        max: quantidade de hashes a serem visualizados quando a 
            operação chegar em 100%"""
   
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
    #Todo, ver uma forma de gerar o formato de maneira dinâmica ({}) 
    #qdo max mudar alterar 
    #o espaçamento do formato
    formato = '{:50}'.format(hashes)
    print(formato, end='')
    print(']', end='')
    
    #fim da impressão de hashes
    #volta o cursor 50 vezes, para que na proxima impressão, dê a impressa 
    #de que a barra de hash
    #está aumentando
    #TODO: quando se colocar o formato dinâmica colocar "range(max)"
    for i in range(50):
        print('\r', end='')
    #se for o ultimo item a ser impresso (100%), quebra a linha no final da
    #barra.    
    if item_atual >= qt_itens :
        print('')
    
if __name__ == "__main__":
    
   renomear_arquivos("/media/lcreina/afrodite/teste_python", recursivo=True, \
                     caracter_substitutivo='.',debug=1)
   #renomear_arquivos("/media/lcreina/afrodite/x", caracter_substitutivo='.')
   #renomear_arquivos(".")
    #renomear_arquivos("arquivos_testes")
    #renomear_arquivos("..")
