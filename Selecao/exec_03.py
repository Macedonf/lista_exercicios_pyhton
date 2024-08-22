#3) Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

#Entrada
prova1 = float (input ("Qual a nota da primeira prova?"))
prova2 = float (input ("Qual a nota da segunda prova?"))

#Processamento
somaprovas = float (prova1 + prova2)
media = float (somaprovas / 2)

if float (media >= 6.0):
    resposta = ("PARABÉS! Você foi aprovado!")

else: resposta = ("")


#Saída

print (" sua média foi", media,".", resposta)