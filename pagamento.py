import datetime
from util import converte_monetario_float, formata_nome_proprio
class FabricaPagamento():

        tipos_dados = ('texto','data_hora','monetario','inteiro')

        VersoesFormatArqMacro =( \
                            {'encoding':'iso-8859-1',
                             'separador':';',
                             'formato_data':'%d/%m/%y',
                             'formato_monetario':'Real', \
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
                             },)
        @classmethod
        def criar_pagamento(cls,linha = '',versao_formato = 0):
            separador = cls.VersoesFormatArqMacro[versao_formato]["separador"]
            #para cada linha:retirar os espacos em branco das extremidades
            #Retira as aspas e transforma a linha numa lista, por meio do caracter 'separador'
            valores_campos = linha.strip().replace('"','').split(separador)
            #Pega o nome dos campos contido no formato do arquivo
            nomes_campos = cls.VersoesFormatArqMacro[versao_formato]["campos"]
            #verifica se a quantidade de campos são identicas, se não forem o formato do arquivo eh incompativel
            if len(valores_campos) != len(nomes_campos):
                raise FormatoArqInvalido("Quantidade de campos do formato nao coincide com a quantidade de campos no arquivo lido")
            else:
                #Dicionario utilizado para criar PagamentoMacro
                pagamento_campos = {}
                
                for indice,(campo,tipo) in enumerate(nomes_campos):
                       pagamento_campos[campo] = cls.converte_campo(tipo,valores_campos[indice])
                       
            #print(pagamento_campos)
            p = PagamentoMacro(**pagamento_campos)
            return p    

        @classmethod
        def converte_campo(cls,tipo_campo,valor_campo, versao_formato=0):
            if tipo_campo in (cls.tipos_dados):
                if tipo_campo == cls.tipos_dados[0]: #tipo_campo = 'texto'?
                    return valor_campo.strip()
                elif tipo_campo == cls.tipos_dados[1]: #tipo_campo = 'data_hora'?
                    return datetime.datetime.strptime(valor_campo,cls.VersoesFormatArqMacro[versao_formato]["formato_data"])
                elif tipo_campo == cls.tipos_dados[2]: #tipo_campo = 'monetario'?
                    return converte_monetario_float(valor_campo, cls.VersoesFormatArqMacro[versao_formato]["formato_monetario"])
                elif tipo_campo == cls.tipos_dados[3]: #tipo_campo = 'inteiro'?
                    return int(valor_campo)
            else:
                raise TipoDadosInvalido


class FormatoArqInvalido(Exception):
    pass
    
class TipoDadosInvalido(Exception):
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
                        historico = ''):

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
             self.valor_liquido = valor_bruto
             self.valor_retencao = valor_retencao
             self.municipio = municipio
             self.historico = historico
    def __str__(self):
             texto = "Data Pagamento: " + self.data_pagamento.strftime('%d/%m/%Y')
             texto += "\nMunicipio: " + formata_nome_proprio(self.municipio)
             texto += "\nUnidade: " + formata_nome_proprio(self.unidade)
             texto += "\nCredor: " + formata_nome_proprio(self.credor)
             texto += "\nValor Bruto: " + str(self.valor_bruto)
             return texto

class ArquivoPagamentosMacro():
    """Classe para tratar arquivo de pagamentos, no formato cvs, gerado pelo sistema macros"""
    def __init__(self,caminho_arquivo,versao_formato=0,tem_cabecalho=1):
        """Abre o arquivo de pagamentos, utilizando a versao do formato"""
        self.arquivo = open(caminho_arquivo,"r",encoding = FabricaPagamento.VersoesFormatArqMacro[versao_formato]["encoding"])

        #versao do formato do arquivo cvs gerado pelo sistema macros
        # onde estão as informações dos pagamentos
        self.versao_formato = versao_formato
        #tem_cabecalho informa se o arquivo tem um cabecalho
        #que deve ser tratado previamente, por padrão tem (=1)
        if tem_cabecalho:
            self.cabecalho = self.arquivo.readline().strip().split()
        else:
            self.cabecalho = None


    def __iter__(self):
        return self

    def __next__(self):
        linha = self.arquivo.readline()
        if linha:
            
             return FabricaPagamento.criar_pagamento(linha,self.versao_formato)

        else:
            raise StopIteration


if __name__ == "__main__":
    #try:
        a = ArquivoPagamentosMacro(r"teste.pagamento_menor.csv",versao_formato=0)
        for pagamento in a:
            print(pagamento)
        #print(VersoesFormatArqMacro )
    #except Exception as e:
    #        print(e.message)

