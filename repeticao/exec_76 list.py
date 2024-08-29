#Construa um algoritmo que leia 50 valores inteiros e positivos e: 
#· Encontre o maior valor
#· Encontre o menor valor
#· Calcule a média dos números lidos

#faça com 5 se der certo ai sim da pra fazer com 50

#OBS01:Refaça o exercício usando lista para armazenar os valores digitados pelo usuário.
#OBS02: Faça com que o sistema sorteie 6 valores digitados pelo usuário logo após o exibir as mensagens.
#  ( para escolher um número aleatório usar o comando  "random.randrange")

maior = 0
menor = 999999
soma = 0
limite = 5
listValores = []

for x in range (1,limite + 1):
    valor = int (input(f"Qual o {x} º valor?"))
    if( valor > maior):
        maior = valor
    if(valor < menor):
        menor = valor

    soma = soma +  maior
    print ("Soma:", soma)
    listValores.append (valor)

print ("Maior:", maior)

print ("Menor:", menor)

print ("Média", soma / limite )

print ("Valores:", listValores)

for x in listValores:
    if (x % 2 ==0):
        print("item:" , x)


