#Construa um algoritmo que leia 50 valores inteiros e positivos e: 
#· Encontre o maior valor
#· Encontre o menor valor
#· Calcule a média dos números lidos

#faça com 5 se der certo ai sim da pra fazer com 50

#OBS01:Refaça o exercício usando lista para armazenar os valores digitados pelo usuário.
#OBS02: Faça com que o sistema sorteie 6 valores digitados pelo usuário logo após o exibir as mensagens.
#  ( para escolher um número aleatório usar o comando  "random.randrange")

maiorValor = 0
menorValor = 999999
media = 0
limite = 50

for x in range (1,limite + 1):
    valor = int (input(f"Qual o {x} º valor?"))
    if( valor > maiorValor):
        maiorValor = valor
    
    if(valor < menorValor):
        menorValor = valor

    media = media +  maiorValor
    print("Soma:", media)
    
print ("Maior:", maiorValor)

print ("Menor:", menorValor)

print ("a média dos números lidos é", media / limite )