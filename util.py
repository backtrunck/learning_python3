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
def formata_nome_empresa(nome):
    padrao_ltda = r'(((L|l)(T|t)(D|d)(A|a)\.?)((\s*)$|(\s*-?\s*(M|m)(E|e)\s*)$))$'
    nome_aux = formata_nome_proprio(nome)
    achado = re.search(padrao_ltda, nome_aux)
    print("nome_aux: ", nome_aux)
    if not achado  is None:
       
        print('group + group', achado.group(0))
    
    
                                    
def converte_monetario_float(valor_monetario, descritor_moeda="Real"):
    """ Converte um valor monetario, no formato indicado no parametro 'descritor_moeda', para um valor float"""
    if eh_valor_monetario(valor_monetario, descritor_moeda):
        
        for chave, simbolo in [(v, u) for v, u in descritores_moeda[descritor_moeda].items() if v != 'separador_decimal']:
            if chave != 'simbolo_moeda':
                valor_monetario = valor_monetario.replace(simbolo,'')
            elif chave == 'simbolo_moeda':
                for simb_moeda in simbolo:
                    valor_monetario = valor_monetario.replace(simb_moeda,'')
        
        if descritores_moeda[descritor_moeda]['separador_decimal'] != '.':
            return float(valor_monetario.replace(descritores_moeda[descritor_moeda]['separador_decimal'], '.'))
            
        return float(valor_monetario)        
    
def eh_valor_monetario(valor_moeda="",descritor_moeda="Real"):

	padrao = '^\\s*((' + '|'.join((descritores_moeda[descritor_moeda])['simbolo_moeda']) + ')\\' 
	padrao += descritores_moeda[descritor_moeda]['simbolo_monetario'] 
	padrao += ')?\\s*(((\\d?\\d?\\d' 
	#+ descritores_moeda[descritor_moeda]['separador_milhar'] 
	padrao +=  ')(\\.\\d\\d\\d)*)|(\\d)+)(' +  descritores_moeda[descritor_moeda]['separador_decimal'] 
	padrao +='\\d*)?$'      
    #print(padrao)
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
        print(linha, formata_nome_empresa(linha))
        
if __name__ == "__main__":
    teste_nome_empresa()
