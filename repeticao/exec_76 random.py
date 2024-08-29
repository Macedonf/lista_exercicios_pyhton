#Construa um algoritmo que leia 50 valores inteiros e positivos e: 
#· Encontre o maior valor
#· Encontre o menor valor
#· Calcule a média dos números lidos

#faça com 5 se der certo ai sim da pra fazer com 50

#OBS01:Refaça o exercício usando lista para armazenar os valores digitados pelo usuário.
#OBS02: Faça com que o sistema sorteie 6 valores digitados pelo usuário logo após o exibir as mensagens.
#  ( para escolher um número aleatório usar o comando  "random.randrange")
import random

maior = 0
menor = 999999
soma = 0
limite = 10
listValores = []

for x in range (1,limite + 1):
    # valor = int (input(f"Qual o {x} º valor?"))
    valor = random.randrange(1, 11)
    if(valor > maior):
        maior = valor
    if(valor < menor):
        menor = valor
    soma = soma +  maior


    listValores.append (valor)

print ("Soma:", soma)

print ("Média:", soma/limite )

print ("Maior:", maior)

print ("Menor:", menor)

print ("Valores:", listValores)

#numeros = range(1, 61)
#resultado = random.sample(numeros, 6)
#print("Os números sorteados são:", resultado)

listadeSorteados = []

for z in range (4):
    index = random.randrange(0,10)
    valorSorteado = listValores[index]
    contDuplicados = 0
    for s in listadeSorteados:
        if(s==valorSorteado):
            contDuplicados += 1
    if(contDuplicados ==0):
        listadeSorteados.append(valorSorteado)


        
print ("Número sorteado:", listadeSorteados)

