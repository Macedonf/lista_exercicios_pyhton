#Acrescente ao exercício anterior a mensagem Você foi REPROVADO! Estude mais... caso a média calculada seja menor que 6.0.

#Entrada
prova1 = float (input ("Qual a nota da primeira prova?"))
prova2 = float (input ("Qual a nota da segunda prova?"))

#Processamento
somaprovas = float (prova1 + prova2)
media = float (somaprovas / 2)

if float (media >= 6.0):
    resposta = ("PARABÉS! Você foi aprovado!")

else: resposta = ("Você foi REPROVADO! Estude mais...")


#Saída

print (" sua média foi", media,".", resposta)