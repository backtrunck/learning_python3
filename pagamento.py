import datetime
class FabricaPagamento():

        tipos_dados = ('texto','data_hora','monetario','inteiro')

        VersoesFormatArqMacro =( \
                            {'encoding':'iso-8859-1',
                             'separador':';',
                             'formato_data':'%d/%m/%y',
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
            #Retira as aspas e transforma a linha numa lista, por meio do
            #caracter 'separador'
            valores_campos = linha.strip().replace('"','').split(separador)
            nomes_campos = cls.VersoesFormatArqMacro[versao_formato]["campos"]
            print("tam valores_campos %d tam nomes_campos %d"%   (len(valores_campos) , len(nomes_campos)))
            if len(valores_campos) != len(nomes_campos):
                raise FormatoArqInvalido("Quantidade de campos do formato nao coincide com a quantidade de campos no arquivo lido")
            else:
                pagamento_campos = {}
                for indice,(campo,tipo) in enumerate(nomes_campos):
                       pagamento_campos[campo] = cls.converte_campo(tipo,valores_campos[indice])
            print(pagamento_campos)

        @classmethod
        def converte_campo(cls,tipo_campo,valor_campo):
            if tipo_campo in (cls.tipos_dados):
                if tipo_campo == cls.tipos_dados[0]: #tipo_campo = 'texto'?
                    return valor_campo.strip()
                elif tipo_campo == cls.tipos_dados[1]: #tipo_campo = 'data_hora'?
                    return datetime.datetime.strptime(valor_campo,"%d/%m/%y")
                elif tipo_campo == cls.tipos_dados[2]: #tipo_campo = 'monetario'?
                    return float(valor_campo)
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
             self.valor_bruto = PyOsString_to_double(valor_bruto)
             self.valor_liquido = PyOsString_to_double(valor_bruto)
             self.valor_retencao = PyOsString_to_double(valor_retencao)
             self.municipio = municipio
             self.historico = historico
    def __str__(self):
             texto = "\nData Pagamento: " + self.data_pagamento
             texto += "\nMunicipio: " + self.municipio
             texto += "\nValor Bruto: " + self.valor_bruto + "\n"

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
            #separador = VersoesFormatArqMacro[self.versao_formato]["separador"]
            #para cada linha:retirar os espacos em branco das extremidades
            #Retira as aspas e transforma a linha numa lista, por meio do
            #caracter 'separador'
            #valores_campos = linha.strip().replace('"','').split(separador)
            #nomes_campos = VersoesFormatArqMacro[self.versao_formato]["campos"]
            #print("tam valores_campos %d tam nomes_campos %d"%   (len(valores_campos) , len(nomes_campos)))
            #if len(valores_campos) != len(nomes_campos):
            #       raise FormatoArqInvalido("Quantidade de campos do formato nao coincide com a quantidade de campos no arquivo lido")
            #else:
                #dados_pagamento={}
                #for i in range(len(nomes_campos)):
                #   dados_pagamento[nomes_campos[i]] = valores_campos[i]
                #return dados_pagamento
             FabricaPagamento.criar_pagamento(linha,self.versao_formato)

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

