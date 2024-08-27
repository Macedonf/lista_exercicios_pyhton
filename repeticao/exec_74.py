#Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem:“Múltiplo de 10”.
multiplo = int (input("Qual o multiplo desejado?"))
valorInicial = int (input("Qual o valor final?"))
valorFinal = int (input("Qual seria o valor final?"))

if(valorFinal < valorFinal):
    for i in range (valorInicial, valorFinal+1):
        if (i % multiplo == 0):
            print (i, "multiplo", multiplo)
    else:
       print(i)

else: print("valor inválido!")



#for i in range (1, 101):

 #   if (i % 10 == 0):
  #   print (i, "multiplo de 10")

#else: print(i)