import datetime, csv, re
from util import converte_monetario_float, formata_nome_empresa, formatar_numero
from xlrd import open_workbook

padrao_procura_1 = r'(.*)- Banco:(.*)- Ag.:(.*)- Conta:(.*)(Débito :| Cheque :)(.*)'
padrao_procura_2 = r'.*RP:(.*)Contrato:(.*)'
padrao_procura_municipio = r'Prefeitura Municipal de (.*)'


tipos_dados = ('texto','data_hora','monetario','inteiro')

VersoesFormatArq =( \
                    {'encoding':'iso-8859-1',\
                     'separador':';',\
                     'formato_data':'%d/%m/%Y',\
                     'formato_monetario':'Real', \
                     'tem_cabecalho':True,\
                     'campos':(
                         ('municipio','texto'), \
                         ('unidade','texto'),  \
                         ('exercicio_pagamento', 'texto'),  \
                         ('empenho', 'texto'),  \
                         ('dotacao', 'texto'),  \
                         ('processo', 'texto'),  \
                         ('credor', 'texto'),  \
                         ('cpf_cnpj', 'texto'),  \
                         ('data_empenho','data_hora') ,\
                         ('data_pagamento','data_hora'), \
                         ('valor_liquido','monetario'), \
                         ('valor_retencao','monetario'), \
                         ('valor_bruto','monetario'), \
                         ('conta_nome','texto'), \
                         ('banco','texto'), \
                         ('agencia','texto'), \
                         ('numero_conta','texto'), \
                         ('documento','texto'), \
                         ('rp','texto'), \
                         ('contrato','texto'),  \
                         ('licitacao','texto'),  \
                         ('historico','texto'))\
                     }, #formato para ArquivoPagamentoTcmBa
                     {'encoding':'iso-8859-1',\
                     'separador':';',\
                     'formato_data':'%d/%m/%Y',\
                     'formato_monetario':'Real', \
                     'tem_cabecalho':True,\
                     'campos':(
                         ('municipio','texto', None), \
                         ('unidade','texto', None),  \
                         ('exercicio_pagamento', 'texto', None),  \
                         #('nome do campo','tipo do campo','localizacao relativa da celula no xls(linha,coluna)')
                         ('empenho', 'texto', (0,0)),  \
                         ('dotacao', 'texto', (0,4)),  \
                         ('processo', 'texto', (0,8)),  \
                         ('credor', 'texto', (0,11)),  \
                         ('cpf_cnpj', 'texto', (0,15)),  \
                         ('data_empenho','data_hora', (0,18)) ,\
                         ('data_pagamento','data_hora', (0,22)), \
                         ('valor_liquido','monetario', (0,25)), \
                         ('valor_retencao','monetario', (0,29)), \
                         ('valor_bruto','monetario', (0,32)), \
                         ('conta_nome','texto', None), \
                         ('banco','texto', None), \
                         ('agencia','texto', None), \
                         ('numero_conta','texto', None), \
                         ('documento','texto', None), \
                         ('rp','texto', None), \
                         ('contrato','texto', None),  \
                         ('licitacao','texto', (1,25)),  \
                         ('historico','texto', (2, 0)), \
                         ('RP_Contrato', 'texto', (1, 15)), \
                         ('dados_financeiros','texto', (1,0)))
                     },)

def converte_campo(tipo_campo,valor_campo, versao_formato=0):
    if tipo_campo in (tipos_dados):
        if tipo_campo == tipos_dados[0]: #tipo_campo = 'texto'?
            return valor_campo.strip()
        elif tipo_campo == tipos_dados[1]: #tipo_campo = 'data_hora'?
            return datetime.datetime.strptime(valor_campo,VersoesFormatArq[versao_formato]["formato_data"])
        elif tipo_campo == tipos_dados[2]: #tipo_campo = 'monetario'?
            return converte_monetario_float(valor_campo, VersoesFormatArq[versao_formato]["formato_monetario"])
        elif tipo_campo == tipos_dados[3]: #tipo_campo = 'inteiro'?
            return int(valor_campo)
    else:
        raise TipoDadosInvalidoExcp
        

class FormatoArqInvalidoExcp(Exception):
    pass
    
class TipoDadosInvalidoExcp(Exception):
    pass
    
class DadosFinanceirosInvalidosExcp(Exception):
    pass
    
class NomeUnidadeInvalidaExcp(Exception):
    pass
    
class PagamentoMacro:
    """Classe que representa cada pagamento no arquivo de pagamento da macro"""
    def __init__(self, agencia = '', \
                        banco = '', \
                        conta_nome = '', \
                        contrato = '', \
                        cpf_cnpj = '', \
                        credor = '', \
                        data_empenho = '', \
                        data_pagamento = '', \
                        documento = '', \
                        dotacao = '', \
                        empenho = '', \
                        exercicio_pagamento = '', \
                        licitacao = '', \
                        numero_conta = '', \
                        processo = '', \
                        rp = '', \
                        unidade = '', \
                        valor_bruto = 0, \
                        valor_liquido = 0, \
                        valor_retencao = 0, \
                        municipio = '', \
                        historico = '', 
                        versao_formato=0):

             self.agencia = agencia
             self.banco = banco
             self.conta_nome = conta_nome
             self.contrato = contrato
             self.cpf_cnpj = cpf_cnpj
             self.credor = credor
             self.data_empenho = data_empenho
             self.data_pagamento = data_pagamento
             self.documento = documento
             self.dotacao = dotacao
             self.empenho = empenho
             self.exercicio_pagamento = exercicio_pagamento
             self.licitacao = licitacao
             self.numero_conta = numero_conta
             self.processo = processo
             self.rp = processo
             self.unidade = unidade
             self.valor_bruto = valor_bruto
             self.valor_liquido = valor_liquido
             self.valor_retencao = valor_retencao
             self.municipio = municipio
             self.historico = historico
             #define a sequencia de campos, usado em __next__
             self.sequencia_campos = [campo[0] for campo in VersoesFormatArq[versao_formato]['campos']]
             #self.indice utilizado em __next__
             self.indice = 0
             
    def __str__(self):
             texto = "Data Pagamento: " + self.data_pagamento.strftime('%d/%m/%Y')
             texto += "\nMunicipio: " + self.municipio
             texto += "\nUnidade: " + self.unidade
             texto += "\nCredor: " + formata_nome_empresa(self.credor)
             texto += "\nValor Bruto: " + str(self.valor_bruto)
             return texto
             
    def __iter__(self):
        return self
        
    def __next__(self):
        #Pega o proximo campo da sequencia definida pela versao do formato passado no __init__
        if self.indice == len(self.sequencia_campos):
            raise StopIteration()
        self.indice += 1
        valor =  getattr(self, self.sequencia_campos[self.indice -1])
        if isinstance(valor, float):
            return formatar_numero(valor, precision=2,  group_sep='.')
        return valor
             
class ArquivoPagamentoLeitor():
    def __init__(self, caminho_arquivo, versao_formato=0):
        self.arquivo = open(caminho_arquivo, 'r', encoding=VersoesFormatArq[versao_formato]["encoding"])
        
class ArquivoPagamentoMacroEscritor():
        def __init__(self, caminho_arquivo, versao_formato=0, mantem_conteudo=0):
            self.versao_formato = versao_formato
            if mantem_conteudo:
                self.arquivo = open(caminho_arquivo, 'rw', encoding=VersoesFormatArq[versao_formato]["encoding"])
            else:
                self.arquivo = open(caminho_arquivo, 'w', encoding=VersoesFormatArq[versao_formato]["encoding"])
            #cria um escritor de csv
            self.csvWriter = csv.writer(self.arquivo, quoting = csv.QUOTE_ALL, delimiter = VersoesFormatArq[self.versao_formato]['separador'])
            
        def escrever_cabecalho(self):
            
            self.csvWriter.writerow([campo[0] for campo in VersoesFormatArq[self.versao_formato]['campos']])
             
        def escrever_pagamento(self, pagamento):
            #Pega o nome dos campos contido no formato do arquivo
            self.csvWriter.writerow(pagamento)
            
            
class ArquivoPagamentoTcmBaLeitor(ArquivoPagamentoLeitor):
    def __init__(self, caminho_arquivo, versao_formato=1):
        #Abre o arquivo xls
        self.arquivo = open_workbook(caminho_arquivo)
        #Abre a primeira planilha
        self.sheet = self.arquivo.sheet_by_index(0)
        #verifica se é um arquivo de pagamentos do TCM BA
        self.verificarArquivo()
        
        #pula para a oitava linha, onde começam as informações de pagamento
        self.linha_atual = 8
        #guarda alguns dados do arquivo
        self.ultima_linha = self.sheet.nrows
        self.qt_pagamento = int(self.sheet.cell_value(self.ultima_linha-1, 5))
        self.valor_bruto_total = float(self.sheet.cell_value(self.ultima_linha-1, 13))
        #Pega o nome do municipio
        m = re.match(padrao_procura_municipio, self.sheet.cell_value(5, 0).split(':')[1].strip())
        if m:
            self.municipio = formata_nome_empresa(m.groups(0)[0])
            print(formata_nome_empresa(m.groups(0)[0]))
        else:
            raise NomeUnidadeInvalidaExcp
        #Pega o nome da Unidade. Ex. Prefeitura Municipal de xxxx    
        self.unidade = formata_nome_empresa(self.sheet.cell_value(5, 0).split(':')[1].strip())
        
    def __iter__(self):
        return self
    
    def __next__(self):
        """Pega do arquivo os dados do proximo pagamento """
        if self.linha_atual < (self.ultima_linha - 6):
            return self.obter_proximo_pagamento()
        else:
            #fim da iteração
            raise StopIteration
        
    def verificarArquivo(self):
        """Verifica se a planilha veio do site do Tribunal de Contas do Estado"""
        
        #Compara celulas especificas da planilha para confirmar que é um arquivo de pagamento do TCM BA
        if self.sheet.cell_value(0, 3).strip() != 'Tribunal de Contas dos Municípios do Estado da Bahia' or \
           self.sheet.cell_value(2, 3).strip() != 'SIGA - Sistema Integrado de Gestão e Auditoria - Módulo de Análise' or \
           self.sheet.cell_value(3, 0).strip() != 'CONSULTA PAGAMENTO EMPENHO':
            raise FormatoArqInvalidoExcp   
            
    def obter_proximo_pagamento(self):
        #Dicionario utilizado para criar PagamentoMacro
        pagamento_campos = {}
        #pega os nomes dos campos e outras informações 
        nome_campos = VersoesFormatArq[1]["campos"]
        
        #(ultima_linha - 6) tira-se 6 linhas que é o rodapé do arquivo (quadro de totalizações
        #loop no formato do arquivos para pegar as posicoes onde serão encontradas
        #as informaçoes de cada campo
        for nome_campo, tipo_campo, posicao_relativa in nome_campos:
            #Só entrar os campos q tiverem posicao relativa, os outro vao ser informados de outro jeito
            if posicao_relativa:
                linha = self.linha_atual + posicao_relativa[0]
                coluna = posicao_relativa[1]
                pagamento_campos[nome_campo] = converte_campo(tipo_campo, self.sheet.cell_value(linha,coluna), versao_formato = 1)
        
        pagamento_campos['municipio'] = self.municipio
        pagamento_campos['unidade'] = self.unidade
        self.obter_dados_financeiros(pagamento_campos)        
        self.linha_atual  += 4    
        #retirando os campos do dicionario que não pertencem ao objeto PagamentoMacro
        del pagamento_campos['dados_financeiros']
        del pagamento_campos['RP_Contrato']
        pagamento_campos['exercicio_pagamento'] = pagamento_campos['data_pagamento'].date().year
        
         #cria o pagamento a partir do dicionario preenchido
        return PagamentoMacro(**pagamento_campos)
        
    def obter_dados_financeiros(self, pagamento_campos):
            m = re.match(padrao_procura_1, pagamento_campos['dados_financeiros'])
            if m:
                dados_financeiros = m.groups(0)
                pagamento_campos["conta_nome"] = dados_financeiros[0].strip()
                pagamento_campos["agencia"] = dados_financeiros[2].strip()
                pagamento_campos["banco"] = dados_financeiros[1].strip()
                pagamento_campos["numero_conta"] = dados_financeiros[3].strip()
                pagamento_campos["documento"] = dados_financeiros[4].strip() + dados_financeiros[5].strip()                 
            else:
                raise DadosFinanceirosInvalidosExcp
            
            m = re.match(padrao_procura_2, pagamento_campos['RP_Contrato'])
            if m:
                dados_financeiros = m.groups(0)
                pagamento_campos['rp'] = dados_financeiros[0].strip()
                pagamento_campos['contrato'] = dados_financeiros[1].strip()
                                
            else:
                raise DadosFinanceirosInvalidosExcp
            
            #acha a posicao final na string, onde termina a informacao do nome da conta
            
            posicao1 = pagamento_campos['RP_Contrato'].find('RP:')
            posicao2 = pagamento_campos['RP_Contrato'].find('Contrato:')
            pagamento_campos["rp"] = pagamento_campos['RP_Contrato'][posicao1 + len('RP:'):posicao2]
            pagamento_campos["contrato"] = pagamento_campos['RP_Contrato'][posicao2 + len('Contrato:'):]
            
class ArquivoPagamentosMacroLeitor(ArquivoPagamentoLeitor):
    """Classe para tratar arquivo de pagamentos, no formato cvs, gerado pelo sistema macros"""
    def __init__(self,caminho_arquivo,versao_formato=0,tem_cabecalho=1):
        """Abre o arquivo de pagamentos, utilizando a versao do formato"""
        #chama o init do pai
        super().__init__(caminho_arquivo, encoding=VersoesFormatArq[versao_formato]["encoding"])
        #lê o csv, utilizando o separador de VersoesFormato do Arquivo de Pagamento
        self.arquivo_conteudo = csv.reader(self.arquivo, delimiter= VersoesFormatArq[versao_formato]['separador'])
        #Guarda no atributo a versao do formato do arquivo cvs gerado pelo sistema macros
        # onde estão as informações dos pagamentos
        self.versao_formato = versao_formato
        #tem_cabecalho informa se o arquivo tem um cabecalho
        #que deve ser tratado previamente, por padrão tem (=1)
        if VersoesFormatArq[versao_formato]['tem_cabecalho']:
            #Guarda o cabecalho
            self.cabecalho = next(self.arquivo_conteudo)
        else:
            self.cabecalho = None


    def __iter__(self):
        return self

    def __next__(self):
        """Pega do arquivo os dados do proximo pagamento """
        #pega proxima linha (list com os dados de cada campo)
        linha = next(self.arquivo_conteudo)
        #se a linha não for vazia cria um pagamento e retorna-o
        if linha:
             return self.obter_proximo_pagamento(linha)

        else:
            #fim da iteração
            raise StopIteration
    def obter_proximo_pagamento(self, valores_campos):
        
        #Pega o nome dos campos contido no formato do arquivo
        nomes_campos = VersoesFormatArq[self.versao_formato]["campos"]
        #verifica se a quantidade de campos são identicas, se não forem o formato do arquivo eh incompativel
        if len(valores_campos) != len(nomes_campos):
            raise FormatoArqInvalidoExcp("Quantidade de campos do formato nao coincide com a quantidade de campos no arquivo lido")
        else:
            #Dicionario utilizado para criar PagamentoMacro
            pagamento_campos = {}
            
            for indice,(campo,tipo) in enumerate(nomes_campos):
                   #Preenche o dicionario com os nomes dos campos e valores já com as devidas conversões
                   #Notar que é imprescindível que a ordem da lista nomes_campos deve ser igual a ordem
                   #em valores_campos
                   pagamento_campos[campo] = converte_campo(tipo,valores_campos[indice])
                   
        #cria o pagamento a partir do dicionario preenchido
        p = PagamentoMacro(**pagamento_campos)
        return p    
def testePagamentoMacro():
    a = ArquivoPagamentosMacroLeitor(r"teste.pagamento_cheio.csv",versao_formato=0)
    for pagamento in a:
        print(pagamento)

def testePagamentoTcmBa():
        total_pagamento=0.0
        qt_pagamento = 0
        b = ArquivoPagamentoMacroEscritor('/home/lcreina/Documentos/programacao/python3/teste.pagamento.macro.escrito.csv')
        a = ArquivoPagamentoTcmBaLeitor('/home/lcreina/Documentos/programacao/python3/ConsultaPagamentoRelsao.felix.xls')
        b.escrever_cabecalho()
        for pag in a:
            print(pag)
            b.escrever_pagamento(pag)
            total_pagamento += pag.valor_bruto
            qt_pagamento +=1
        
        if round(total_pagamento, 2) != round(float(a.valor_bruto_total), 2) :
            print('Valor_Bruto Lido:', total_pagamento, 'Valor_total_informado no arquivo:', a.valor_bruto_total)
        if qt_pagamento != a.qt_pagamento:
            print('Qt de pagamentos lido:', qt_pagamento, 'Qt de pagamentos informados no arquivo', a.qt_pagamento)
        
        print('Total de Pagamentos lidos: %d\nValor Total de Pagamento %s'%(qt_pagamento, formatar_numero(total_pagamento, precision=2)))
        

if __name__ == "__main__":
   #testePagamentoMacro()
   testePagamentoTcmBa()
