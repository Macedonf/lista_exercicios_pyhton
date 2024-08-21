#A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de seu carro para que ele possa percorrer um determinado número de voltas até o primeiro reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os abastecimentos é o mesmo.


#ENTRADA
comprimento= float (input("Qual o cumprimento da pista (em metros)?"))#1000
voltas= int(input("Qual o numero total de voltas? ")) #10
abastec= int( input("Qual o numero de abastceimento desejado ?")) #2                    
consumo= float(input("Qual o consumo de combustivel do carro (km/L)?")) #10


#PROCESSAMENTO
def calculolitros():
    kmtotal = (comprimento / 1000) * voltas
    consumototal= kmtotal / consumo
    return consumototal / abastec

#SAIDA
print (" o número mínimo de litros necessários até o primeiro reabastecimento" , calculolitros())