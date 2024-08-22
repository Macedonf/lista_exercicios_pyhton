#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

#Entrada
numeromaca = int (input("Olá, quantas maças deseja comprar?"))

macamenosduzia = float (0.30)
macaduzia = float (0.25)
#Processamento
if int (numeromaca >= 6):
    resposta = float (macaduzia * numeromaca)

else: resposta = float (macamenosduzia * numeromaca)    

#Saída
print ("O valor total da sua compra é de, R$", resposta, ".")