import os
def processar_resposta(resposta):
 if resposta =='1':1
 print(f'{os.linesep}{resposta}Quais dias você está buscando?{os.linesep}')
 pass
 if resposta =='2':
  print(f'{os.linesep}{resposta}temos alguns pacotes, quais você deseja?{os.linesep}')
  pass
 if resposta =='3':
  print(f'{os.linesep}{resposta}temos alguns valores de passagem, quais você deseja?{os.linesep}')
  pass 
def start():
#Apresentar o chatbot de viagens
 print('Boa tarde! Meu nome é ana e sou do chat bot de viagens B2D.Poderia me informar o seu e-mail?')
#pedir o e-mail
email=input('Digite o seu e-mail:')
while True:
 #oferecer o menu de  opções 
 resposta =input(f'Quais serviços você está procurando?{os.linesep}[1]-Hospedagem{os.linesep}[2]-Pacote( hospedagem+passagem) {os.linesep} [3]-passagem de avião')
 #processar a resposta
processar_resposta(resposta,email)
#finalizar o chatbot
print('Foi enviado para o seu e-mail um comprovante de pagamento e sua passagem. Espero que aproveite a sua viagem.Qualquer dúvida, envie um e-mail para o pessoal de suporte:agenciaviagensb2d@hotmail.com')


 