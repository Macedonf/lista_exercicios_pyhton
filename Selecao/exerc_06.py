#Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for digitado o valor zero, escrever a palavra zero.

#Entrada
valor = int (input("escreva um valor:"))

#Processamento
Resposta = ""
if valor ==0 :
     Resposta = "zero"

elif valor > 0 : 
    Resposta = "positivo"
else:
     Resposta = "negativo"


      #saidas
print (" o valor é", Resposta)