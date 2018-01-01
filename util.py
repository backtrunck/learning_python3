import re
descritores_moeda = {"Real":\
                                        {  'simbolo_monetario':"$", \
                                            'simbolo_moeda':('R', 'r'), \
                                            'separador_milhar':'.', \
                                            'separador_decimal':','}\
                                    }    
                                    
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
			
			
if __name__ == "__main__":
    #eh_valor_monetario()
	teste_eh_valor_monetario()
