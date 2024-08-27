#Construa um algoritmo que leia 50 valores inteiros e positivos e:
#· Encontre o maior valor
#· Encontre o menor valor
#· Calcule a média dos números lidos

#OBS01:Refaça o exercício usando lista para armazenar os valores digitados pelo usuário.
#OBS02: Faça com que o sistema sorteie 6 valores digitados pelo usuário logo após o exibir as mensagens.
#  ( para escolher um número aleatório usar o comando  "random.randrange")

maiorValor = 0
menosValor = 0
soma = 0

for x in range (1,6):
    valor = int (input(f"Qual o {x} º valor?"))
