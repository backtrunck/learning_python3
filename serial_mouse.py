import serial 

def converte_velocidade(velocidade):
    return int(velocidade)/131.0
    
def converte_aceleracao(aceleracao):
    return int(aceleracao)/16384.0
	
s = serial.Serial('/dev/ttyUSB0',9600)
vel_x_inicial = vel_y_inicial = vel_z_inicial = 0
while 1:
   #s.write(b'\x01')
   # print('Lendo...')
  
   dados_recebidos = s.readline().decode('utf-8').strip()
   print(dados_recebidos)
   if dados_recebidos[0] == '0':
       tipo_registro, vel_x_inicial, vel_y_inicial, vel_z_inicial = dados_recebidos.split(";")
    
   elif dados_recebidos[0] == '1':
       tipo_registro, vel_x, vel_y, vel_z, acel_x, acel_y, acel_z = dados_recebidos.split(";")
       print("Velocidades Iniciais x={} y={} z={}".format(converte_velocidade(vel_x_inicial), converte_velocidade(vel_y_inicial), converte_velocidade(vel_z_inicial)))
       print("Velocidades x={} y={} z={}".format(converte_velocidade(vel_x),converte_velocidade(vel_y), converte_velocidade(vel_z)))
       
       print("Aceleracoes x={} y={} z={}".format(converte_aceleracao(acel_x), converte_aceleracao(acel_y),converte_aceleracao(acel_z)))
    
   else:
       print(dados_recebidos)
  # portb = s.read(1)


   
   #pb = int.from_bytes(portb,byteorder='little')
 
