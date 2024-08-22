#Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

#Entrada
valor = int (input("escreva um valor:"))

#Processamento
resposta = ""
if valor >= 0 : 
    resposta = "positivo"
else:
     resposta = "negativo"

      #saidas
print (" o valor é", resposta)
