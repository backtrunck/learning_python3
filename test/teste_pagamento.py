import sys 
import os 

caminho_base = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0,os.path.join(caminho_base , '..'))

caminho_base,pasta_atual = os.path.split(caminho_base)

from pagamento import * 

def testePagamentoMacro():
    a = ArquivoPagamentosMacroLeitor(r"./arquivos_testes/teste.pagamento_cheio.csv",versao_formato=0)
    for pagamento in a:
        print(pagamento)

def testePagamentoTcmBa():
        total_pagamento=0.0
        qt_pagamento = 0
        b = ArquivoPagamentoMacroEscritor('./arquivos_testes/teste.pagamento.macro.escrito.tcmba.csv')
        a = ArquivoPagamentoTcmBaLeitor('./arquivos_testes/ConsultaPagamentoRelsao.felix.xls')
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
if __name__ == '__main__':

    print ("Teste Pagamento Macro")
    testePagamentoMacro()

    print("Teste PagamentoTcmBa")
    testePagamentoTcmBa()


