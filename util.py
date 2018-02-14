import re
descritores_moeda = {"Real":\
                            {  'simbolo_monetario':"$", \
                                'simbolo_moeda':('R', 'r'), \
                                'separador_milhar':'.', \
                                'separador_decimal':','}\
                            }  
def formata_nome_proprio (nome, tamanho_minimo = 4):
        nome_proprio = []
        for indice, palavra in enumerate(nome.title().split()):
            if len(palavra) < tamanho_minimo:
                palavra = palavra.lower()
            nome_proprio.append(palavra)
        return " ".join(nome_proprio)
        
def formata_nome_empresa(nome, tamanho_minimo = 3):
    padrao_ltda = r'((L|l)(T|t)(D|d)(A|a)(\.?))((\s*-?\s*(M|m)(E|e)\s*)?)\s*$'
    tipo_empresarial = ''
    nome_aux = formata_nome_proprio(nome, tamanho_minimo)
    achado = re.search(padrao_ltda, nome_aux)
    
    
    if achado:   
        #print(achado.groups(0))
        if achado.groups(1)[0]:
            #print(achado.groups(1)[0])
            tipo_empresarial += 'Ltda.'
        if achado.groups(7)[6]:
            #print(achado.groups(7)[6])
            if tipo_empresarial:
                tipo_empresarial = 'Ltda - Me'
            else:
                tipo_empresarial =  '- Me'
        nome_aux = re.sub(padrao_ltda, tipo_empresarial, nome_aux)
    
    return nome_aux
def formatar_numero(number, precision=0, group_sep='.', decimal_sep=','):

    number = ('%.*f' % (max(0, precision), number)).split('.')

    integer_part = number[0]
    if integer_part[0] == '-':
        sign = integer_part[0]
        integer_part = integer_part[1:]
    else:
        sign = ''
      
    if len(number) == 2:
        decimal_part = decimal_sep + number[1]
    else:
        decimal_part = ''
   
    integer_part = list(integer_part)
    c = len(integer_part)
   
    while c > 3:
        c -= 3
        integer_part.insert(c, group_sep)

    return sign + ''.join(integer_part) + decimal_part
    
def converte_monetario_float(valor_monetario, descritor_moeda="Real"):
    """ Converte um valor monetario, no formato indicado no parametro 'descritor_moeda', para um valor float"""
    #verifica se é um numero negativo
    if valor_monetario.find('-') != -1:
        #achou um sinal de menos, retira-o e ajusta o valor do multiplicador para no final 
        #negativar o numero
        valor_monetario = valor_monetario.replace('-', '')
        multiplicador = -1.0
    else:
        multiplicador = 1.0
        
    if eh_valor_monetario(valor_monetario, descritor_moeda):
        
        for chave, simbolo in [(v, u) for v, u in descritores_moeda[descritor_moeda].items() if v != 'separador_decimal']:
            if chave != 'simbolo_moeda':
                valor_monetario = valor_monetario.replace(simbolo,'')
            elif chave == 'simbolo_moeda':
                for simb_moeda in simbolo:
                    valor_monetario = valor_monetario.replace(simb_moeda,'')
        
        if descritores_moeda[descritor_moeda]['separador_decimal'] != '.':
            return float(valor_monetario.replace(descritores_moeda[descritor_moeda]['separador_decimal'], '.')) \
                    * multiplicador
            
        return float(valor_monetario) * multiplicador       
    
def eh_valor_monetario(valor_moeda="",descritor_moeda="Real"):

	padrao = '^\\s*-?\\s*((' + '|'.join((descritores_moeda[descritor_moeda])['simbolo_moeda']) + ')\\' 
	padrao += descritores_moeda[descritor_moeda]['simbolo_monetario'] 
	padrao += ')?\\s*(((\\d?\\d?\\d' 
	#+ descritores_moeda[descritor_moeda]['separador_milhar'] 
	padrao +=  ')(\\.\\d\\d\\d)*)|(\\d)+)(' +  descritores_moeda[descritor_moeda]['separador_decimal'] 
	padrao +='\\d*)?$'      
    #padrao = '^\s*((R|r)\$)?\s*(((\d?\d?\d)(\.\d\d\d)*)|(\d)+)(,\d*)?$'
	if valor_moeda.strip() :
		if re.match(padrao,valor_moeda):
			return 1
		else:
			return 0
	else:
		return 0

def teste_eh_valor_monetario():
    arquivo = open('teste_monetario')
    for linha in arquivo:
        lista = linha.strip().split(";")
        if eh_valor_monetario(lista[0]) != int(lista[1]):
            print("Erro -> {}".format(lista[0]))
        else:
            print("Ok -> {}".format(lista[0]))
            if int(lista[1]) == 1:
                print(converte_monetario_float(lista[0], "Real"))

def teste_nome_empresa():
    arquivo = open('teste_nome_empresa.txt')
    for linha in arquivo:
        lst = linha.split(";")
        print("linha->", lst[0].strip())
        print("formata_nome_empres->", formata_nome_empresa(lst[0]))
    
if __name__ == "__main__":
    teste_nome_empresa()
