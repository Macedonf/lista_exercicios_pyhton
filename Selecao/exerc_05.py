#Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

#Entrada
valor = int (input("escreva um valor:"))

#Processamento
Resposta = ""
if valor >= 0 : 
    Resposta = "positivo"
else:
     Resposta = "negativo"

      #saidas
print (" o valor é", Resposta)
