#Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.

#Entrada
valor1= float (input("Qual o primeiro valor?"))
valor2= float (input("Qual o segundo valor?"))

#processamento
resposta = valor1 if valor1 > valor2 else valor2

#saida
print("O maior deles: ", resposta)