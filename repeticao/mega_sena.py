#Desenvolva um programa em sua linguagem de programação que simule o sorteio de um concurso da Mega-Sena.A Mega-Sena é uma loteria onde 6 números diferentes são sorteados de um conjunto de 60 números (de 1 a 60). O programa deve atender aos seguintes requisitos:Geração de números sorteados:Gere aleatoriamente 6 números distintos entre 1 e 60.Exiba esses números na tela em ordem crescente.
#Entrada do usuário:
#Pedir que você insira sua aposta, que é composta por 6 números distintos entre 1 e 60.
#Verificação de respostas corretas:
#Compare os números sorteados com os números que você aposta.
#Vou te dizer quantos números você acertou.
#Prêmios:
#Vou mostrar o número de acertos e, de acordo com as regras da Mega-Sena, indicar o prêmio fictício:
#4 hits: Quadra
#5 acertos: Quina
#6 acertos: Sena
#Se você não tiver pelo menos 4 acertos, exibirei uma mensagem informando que você não ganhou.
#Repita: (Opcional)
#Vou perguntar se você deseja realizar um novo sorteio. Em caso afirmativo, reinicie o processo; Caso contrário, encerre o programa.

import random



def numpremiados():
     numeros = random.sample(range(1,61),6)
     return sorted(numeros)


def digitanumaposta ():
    while True:
        try:
            aposta = (list(map(int , input ("Digite os 6 números de 1 a 60 desejados!"))))
            if len(aposta) != 6 or any(numpremiados <1 or numpremiados > 60 for numpremiados in aposta) or len(set(aposta)) !=6:
                    raise ValueError
            return sorted(aposta)
        except ValueError:

            print("Aposta Inválida!")

def verific_aposta(numpremiados , aposta):
     acertos = len(set(numpremiados) & set(aposta))
     if acertos == 6:
          premio = "Sena"
     elif acertos == 5:
        premio = "Quina"
     elif acertos == 4:
          premio = "Quadra"
     else: 
          premio = None
          return acertos, premio     

def resultado(numpremiados, aposta, acertos, premio):
     print(f"os números sorteados foram:{numpremiados}")
     print