#Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área (Pi * (raio * raio))
#ENTRADA
raio= int (input("qual é o raio?"))


#PROCESSAMENTO
def calculoarea(valorRaio):
    PI = 3.14
    return PI * (valorRaio * valorRaio)

#SAÍDA
print(" Area do circulo " , calculoarea(raio))

