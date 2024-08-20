#Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
from datetime import date

#Entrada
anoNasc = int (input("Qual o ano do seu nascimento?"))
ANOATUAL = date.today().year

#Processamento
resposta = ""
idade = (ANOATUAL - anoNasc)
if (idade >= 16): resposta = "sim"

else: resposta = "não"

#Saída
print ("Você poderá votar esse ano: ", resposta)
print ("Porque você tem", idade , "anos")