import serial 


s = serial.Serial('/dev/ttyUSB1',9600)
while 1:
    s.write(b'0X1')
    print('Lendo...')
    print(s.read(1))
    sair = raw_input("S para sair")

    if sair.upper() == 'S':
        exit(0)
