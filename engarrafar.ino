#include <Wire.h>
//#include "rgb_lcd.h"

/*Disposição do pinos arduino mega
 * pinos(0 ,--,--,--,--,--,--,7)
 * PORTB(53,52,51,50,10,11,12,13)
 * PORTC(37,36,35,34,33,32,31,30)
 */

#define GARRAFADISP   0b00000001  //bit testa se tem garrafa
#define POSINICIAL    0b00000010  //bit posição inicial
#define POSENCHER     0b00000100  //bit posição enchimento
#define POSTAMPAR     0b00001000  //bit posição tampa
#define POSRETIRAR    0b00010000  //bit posição remoção
#define GARRAFACHEIA  0b00100000  //bit teste garrafa cheia
#define GARRAFATAMPA  0b01000000  //bit teste garrafa tampada
#define AVANPISTAO    0b10000000  //bit indica avanço do pistão

#define ACIONABOMBA   0b00000010  //bit indica funcionamento da bomba
#define ACIONAESTEIRA 0b00000001  //bit para acionar esteira

  
int PosInicial = 0; //Posição 1 da esteira, garrafa empurrada pelo pistão
int PosEncher = 0; //Posição 2 da esteira, garrafa esperando enchimento
int PosTampar = 0; //Posição 3 da esteira, garrafa esperando tampa
int PosRetirar = 0; //Posição 4 da esteira, garrafa sendo removida pelo robô
int GarrafaDis = 0; //Mostra Garrafa disponível no pistão
int AvanPistao = 0; //Sinalizador de pistão acionado
int EsteiraOn = 0; //Simboliza Esteira Funcionando
//^Leds

unsigned int msg;  //dados trocados com o PC


int Liga; //Botão que aciona Pistão

char buff[4];


/*void DisplayPos(int PosInicial, int PosEncher, int PosTampar, int PosRetirar){
  digitalWrite(5, PosInicial);
  digitalWrite(6, PosEncher);
  digitalWrite(7, PosTampar);
  digitalWrite(8, PosRetirar);  
}*/
void AvanEsteira(){
  //avança esteira 1 metro
}

void Pausa(int tempo){
  //define quanto tempo de pausa tera cada ação
}

void EnviaPos(){
    if (Serial.available()){
    sprintf(buff,"%1d%1d%1d%1d",PosInicial,PosEncher,PosTampar,PosRetirar);
    Serial.println(buff);
   }
}

void MovePos(){
  //a cada interação move a lampada uma posição à frente.
}

void aciona_pistao(){  
  PORTB |= AVANPISTAO; //avanca pistao
  Serial.print(PORTB);   
  delay(2000);
  PORTB &= ~AVANPISTAO; //retrai pistao
}

void AcionaBomba(){
  if (!(PORTB & GARRAFACHEIA)){
    PORTB |= ACIONABOMBA;
    Pausa(5000);
    PORTB &= ~ACIONABOMBA;
  }
}

void aciona_esteira(){
  if (PORTB & (POSINICIAL | POSENCHER | POSTAMPAR )){  //Tem pelo menos uma garrafa na esteira na posição inicial, encher ou tampar
      if (~(PORTB & POSRETIRAR)){                      //Não tem garrafa na posição retirar
        PORTC |= ACIONAESTEIRA;
        delay(2000);
        PORTB <<= 1;
        PORTC &= ~ACIONAESTEIRA;
      }
  }
}

void setup() {
  Serial.begin(9600);
  //Define pinos do PORTB como saída
  DDRB = GARRAFADISP |POSINICIAL | POSENCHER | POSTAMPAR | POSRETIRAR |GARRAFACHEIA |GARRAFATAMPA | AVANPISTAO ;
  DDRC = ACIONAESTEIRA;
  
  PORTB = 0;
  PORTC = 0;
 
}

void loop() {
  if (Serial.available() != 0){
    msg = Serial.read();
    if (msg != 0XFFFF){
      PORTB = msg;
      delay(1000);
    }
    
    if (EsteiraOn == 0){
      if (~(PORTB & POSINICIAL))            //posicao inicial vazia?
          if (PORTB & GARRAFADISP)          //tem garrafa disponivel            
            aciona_pistao();                 //aciona pistão 
      aciona_esteira();
      /*if (PORTD & POSENCHER){
        //Função encher garrafa
        
      }
      if (PosTampar != 0){
      //Função tampa garrafa
      }
      if (PosRetirar != 0){
      //Função retirar garrafa
      }
      EnviaPos();
      
      //Função ligar esteira{
      //EsteiraOn = 1;
      //digitalWrite(9,EsteiraOn);
      //}
      
      EnviaPos();*/
      
    }
 } 
}
