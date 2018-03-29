#coding=utf-8
import mysql.connector

import sys,os,getpass,csv

from utilitarios.validadores import validar_cnpj

from utilitarios.terminal import ProgressMeter

#parametros para inicialização
#C:\projetos\teste.txt 07009304000169,09277669000442,11080055000175,11962077000169 09277669000442,11080055000175,11962077000169

#tipos de interface gráficas
TERMINAL=1
WINDOWS=2

#Dados para conexão com BD
PORTA = 3306
BANCO_DADOS = 'TCM_BA'
#produção
HOST = 'esfinge.df.cgu'

#homologação
#HOST = 'esfinge-hm.df.cgu1'



def obter_licitacoes_um_pra_muitos(conexao,alvo_principal,alvos_secundarios,\
                                   progress_bar = None):
    """Obtem as licitações em que o alvo (um) participou com qq um dos muitos
        parametros:
        conexao (MySqlCursor): cursor para o BD
        alvo_principal (string): CNPJ da empresa alvo
        alvos_secundários (string): CNPJs das outras empresas
        retorno:
        licitações (lista) """

    licitacoes_alvo_principal = obter_licitacoes(alvo_principal,conexao)

    #lista para guardar as licitações em que o alvo principal e secundários
    #participaram
    licitacoes_comuns = []

    #lista para guardar as licitações em que os alvos participaram
    licitacoes_alvo = []

    licitacoes_alvos_secundarios = obter_licitacoes(alvos_secundarios,conexao)

    #se foram recuperadas licitações, verifica se são comuns às licitações
    #alvo principal
    if licitacoes_alvos_secundarios:
        for licitacao in licitacoes_alvo_principal:
            if licitacao in licitacoes_alvos_secundarios:
                licitacoes_alvo.append(licitacao)

    #se houve licitações comuns, recupere todas os dados das mesmas do BD
    if licitacoes_alvo:
         consulta = "SELECT " + \
            "u.Descricao, m.Nome as Municipio, " +\
            "u.TipoUnidade, l.ExercicioHomologacao, +" \
            "l.Processo, l.Modalidade, " +\
            "l.DataHomologacao, l.Execucao, " + \
            "l.ValorEstimado, l.Objeto, " +\
            "l.`CNPJ-CPF`, l.Fornecedor, " + \
            "l.ValorHomologado " +\
            "FROM ( TCM_BA.tcmba_unidades u INNER " + \
            "JOIN TCM_BA.tcmba_municipios m ON (u.Municipio = m.Codigo)) " + \
            "INNER JOIN  (TCM_BA.tcmba_licitacoes AS l) ON " + \
            "(l.Unidade = u.Codigo) " + \
            "WHERE l.unidade = %s and l.datahomologacao = %s " + \
            "and l.processo = %s and l.modalidade = %s"
         if progress_bar != None:
            progress_bar.set_valor_max(len(licitacoes_alvo))


    cursor_licitacoes = conexao.cursor(buffered=True)

    for i,licitacao in enumerate(licitacoes_alvo):
        cursor_licitacoes.execute(consulta,tuple(licitacao))
        if progress_bar != None:
            progress_bar.update_progress(i+1)
        licitacoes_comuns += cursor_licitacoes.fetchall()

    return licitacoes_comuns

def obter_licitacoes_muitos_pra_muitos(conexao,alvos_principais,\
                                       progress_bar = None):
    """Obtem as licitações em que o alvo (um) participou com qq um dos muitos
        parametros:
        conexao (MySqlCursor): cursor para o BD
        alvo_principal (string): CNPJ da empresa alvo
        alvos_secundários (string): CNPJs das outras empresas """


    #lista para guardar as licitações em que o alvo principal e secundários
    #participaram
    licitacoes_comuns = []

    consulta = "SELECT DISTINCT unidade, datahomologacao, processo, " + \
        "modalidade " + \
        "FROM TCM_BA.tcmba_licitacoes " + \
        gerar_filtro(alvos_principais)   + \
        " GROUP BY unidade, datahomologacao, processo, modalidade " + \
        "HAVING COUNT(*) > 1"
    #se não for None e ProgresseMeter, então é um ProgressBar(interf. grafica)
    if progress_bar != None:
        progress_bar.config(mode="indeterminate")
        progress_bar.start(50)
        
    cursor = conexao.cursor(buffered=True)
    cursor.execute(consulta,tuple(alvos_principais))
    licitacoes_alvos_principais = cursor.fetchall()

    if licitacoes_alvos_principais:

        consulta = "SELECT " + \
            "u.Descricao, m.Nome as Municipio, " +\
            "u.TipoUnidade, l.ExercicioHomologacao, +" \
            "l.Processo, l.Modalidade, " +\
            "l.DataHomologacao, l.Execucao, " + \
            "l.ValorEstimado, l.Objeto, " +\
            "l.`CNPJ-CPF`, l.Fornecedor, " + \
            "l.ValorHomologado " +\
            "FROM ( TCM_BA.tcmba_unidades u INNER " + \
            "JOIN TCM_BA.tcmba_municipios m ON (u.Municipio = m.Codigo)) " + \
            "INNER JOIN  (TCM_BA.tcmba_licitacoes AS l) ON " + \
            "(l.Unidade = u.Codigo) " + \
            "WHERE l.unidade = %s and l.datahomologacao = %s " + \
            "and l.processo = %s and l.modalidade = %s"

        if progress_bar != None:
            progress_bar.stop()
            progress_bar.config(mode="determinate")
            #progress_bar.set_valor_max(len(licitacoes_alvos_principais))
            progress_bar["maximum"] = len(licitacoes_alvos_principais)


        for i,licitacao in enumerate(licitacoes_alvos_principais):
            cursor.execute(consulta,tuple(licitacao))
            #se for um progrees Meter
            if type(progress_bar) is ProgressMeter:
                progress_bar.update_progress(i+1)
            elif progress_bar != None:
                #é um progrees bar
                progress_bar["value"] = i + 1
            licitacoes_comuns += cursor.fetchall()

    return licitacoes_comuns

def obter_licitacoes(cnpjs,conexao):
    """ Obtem todas as licitações que uma empresa participou
    parâmetros:
        cnpj (lista): números dos cnpjs das empresas a serem pesquisas
        conexao (MySqlConnector): conexão com o BD
    retorno:
        licitacoes (set): Conjunto das licitações em que a empresa participou
    """
    if len(cnpjs) == 1:
        consulta = "SELECT DISTINCT unidade, datahomologacao, processo" + \
                    ", modalidade " + \
                    "FROM TCM_BA.tcmba_licitacoes " + \
                    "WHERE `CNPJ-CPF`= %s"
    else:
        #todas as licitações com participação do cnpjs
        consulta = "SELECT DISTINCT unidade, datahomologacao, processo," + \
            " modalidade " + \
            "FROM TCM_BA.tcmba_licitacoes " + \
            gerar_filtro(cnpjs)

    cursor = conexao.cursor(buffered=True)


    #lista para guardar as licitações
    licitacoes = []

    #obtem todas as licitações das empresas
    cursor.execute(consulta,tuple(cnpjs))

    licitacoes = cursor.fetchall()

    return licitacoes

def gerar_filtro(lista_cnpj):

    filtro_cnpjs_secundarios = ("`CNPJ-CPF` = %s*" * len(lista_cnpj)).split('*')
    #retira o ultimo elemento (string vazia)
    filtro_cnpjs_secundarios.pop()
    #forma um where de OR com os cnpjs
    filtro_cnpjs_secundarios = "WHERE " +  " OR ".join(filtro_cnpjs_secundarios)
    return filtro_cnpjs_secundarios

def obter_conexao(servidor,porta,banco_dados,usuario,senha):

    conexao = mysql.connector.connect(  host= servidor,
                                            port=porta,
                                            database= banco_dados,
                                            user=usuario,
                                            password=senha)

    return conexao

def main():
    """
    Gera arquivo com os dados das licitações onde determinadas empresas, supos-
    tamente concorreram
    Parâmetros:
        arq_out (string) caminho para o arquivo se saida
        cnpj_alvo (string) cnpj da empresa que deve ser pesquisada
        cnpjs_alvo (string) (opcional) lista de cnpj, separados por virgula,
            de empresas para as quais deve-se verificar se existem licitação,
            nas quais estas empresas concorreram junto com o cnpj alvo.
    """
    #import datetime

    if len(sys.argv) < 3:
        print("Sintaxe inválida: usar: partc_licit /caminho/arquivo cnpj_alvo \
<listas_cnpjs>")
        exit(1)

    caminho,nome_arquivo = os.path.split(sys.argv[1])

    #verifica se a diretório exist
    if not os.path.isdir(caminho):
        print("Diretório Não Existe: %s" % caminho)
        exit(1)

    #verifica se o arquivo passado é válido
    if not nome_arquivo :
        print("Arquivo inválido: %s" % sys.argv[1])
        exit(1)

    #validar cnpj
    cnpjs = sys.argv[2].split(',')
    cnpjs_principais = []
    sair = False
    for cnpj in cnpjs:
        cnpj_temp = validar_cnpj(cnpj)
        if not cnpj_temp:
            print("CNPJ inválido: %s" % cnpj)
            sair = True
        else:
            cnpjs_principais.append(cnpj_temp)
    if sair:
        exit(1)

    if len(sys.argv) > 3:
        cnpjs_temp = sys.argv[3].split(',')

        cnpjs_secundarios = [cnpj for cnpj in cnpjs_temp if validar_cnpj(cnpj)]

    try:
        arquivo_csv = open(os.path.join(caminho,nome_arquivo),'w',newline='')
    except IOError as e:
        if e.errno == 13:
            print("Aceeso negado ao arquivo")
            exit(e.errno)
        else:
            print("Erro ao abrir arquivo: %d "% e.errno)

    except Exception as e:
        print("Erro ao abrir arquivo: %s" % e.__class__.__name__)
        exit(e.errno)


    usr = 'luiscar'

    #while not usr:
    #    usr = input("usuário: ")

    senha = '#qoataqfdsj33'

    #while not senha:
    # senha = getpass.getpass("senha: ")
    try:
        conexao = mysql.connector.connect(  host= HOST,
                                            port=PORTA,
                                            database= BANCO_DADOS,
                                            user=usr,
                                            password=senha)
    except mysql.connector.ProgrammingError as erro:
        if erro.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acesso negado para o usuário, verique usuário e senha")
            exit(erro.errno)
        elif erro.errno == mysql.connector.errorcode.ER_DBACCESS_DENIED_ERROR:
            print("Sem permissão de acessar o banco {}".format(BANCO_DADOS))
            exit(erro.errno)
        else:
            print("Erro: {}".format(erro))
            exit(erro.errno)
    except mysql.connector.InterfaceError as erro:
            print("Impossivel conectar com o servidor: {}".format(erro.msg))
            exit(erro.errno)

    print()
    cursor = conexao.cursor(buffered=True)


    cursor_alvo_principal = conexao.cursor(buffered=True)

    #lista para guardar as licitações em que o alvo principal e secundários
    #participaram
    licitacoes_comuns = []

    #caso seja passada apenas um cnpj principal
    if len(cnpjs_principais) == 1:
        #Caso sejam passados cnpj secundários, faça pesquisa um para muitos
        if cnpjs_secundarios:

            licitacoes_comuns = obter_licitacoes_um_pra_muitos(conexao,\
                                                            cnpjs_principais,\
                                                            cnpjs_secundarios)
        else:
            #Obter todas as licitações do alvo principal(sem alvos secundários)
            licitacoes_comuns = obter_licitacoes(cnpjs_principais,conexao)

    else:
        #todos com todos
        p = ProgressMeter()
        licitacoes_comuns = obter_licitacoes_muitos_pra_muitos(\
                                                        conexao,\
                                                        cnpjs_principais,p)

    conexao.close()

    #se existirem licitações comuns, gerar arquivo .csv
    if licitacoes_comuns:

        escritor = csv.writer(arquivo_csv,delimiter=";", \
                              quotechar='"',quoting = csv.QUOTE_ALL)


        for (   desc,municipio,tp_unidade,\
                exercicio,processo,modalidade,\
                dt_homologacao,execucao,valor_estimado,\
                objeto,cnpj,fornecedor,valor_homologado) in licitacoes_comuns:

                escritor.writerow(
                        [desc,municipio,tp_unidade,\
                        exercicio,processo,modalidade,\
                        dt_homologacao,execucao,valor_estimado,\
                        objeto,cnpj,fornecedor,valor_homologado])


    arquivo_csv.close()




if __name__ == '__main__':
    main()
