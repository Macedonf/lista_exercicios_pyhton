# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

# entrada
valores = [] # como dentro de valores esta zerado, precisa por o comando append para ir incluindo os itens. se não teria que descrever a quantidade de itens dentro. ex: [0,0,0].
valores.append  (int(input("Digite o primeiro valor?"))) # 5
valores.append (int(input("Digite o segundo valor?"))) # 2
valores.append (int(input("Digite o terceiro valor?"))) # 7

for x in valores:
    print(x)
if ( valores [0] > valores[1] ):
    valortemp = valores[0]
    valores[0] = valores [1]
    valores[1] = valortemp

if ( valores [0] > valores[2] ):
    valortemp = valores[0]
    valores[0] = valores [2]
    valores[2] = valortemp

if ( valores [1] > valores[2] ):
    valortemp = valores[1]
    valores[1] = valores [2]
    valores[2] = valortemp


print (valores)
# processamento
# valorTemp = valorDestino
#    valorDestino = valorOrigin
#    valorOrigin = valorTemp    
 #   return [valorOrigin, valorDestino]

#if( valor1 > valor2 ):
 #   resposta = trocaNumeros(valor1, valor2)
  #  valor1 = resposta[0]
   # valor2 = resposta[1] 
    # valorTemp = valor2
    # valor2 = valor1
    # valor1 = valorTemp
    
#if( valor1 > valor3 ):
 #   resposta = trocaNumeros(valor1, valor3)
  #  valor1 = resposta[0]
   # valor3 = resposta[1] 
    # valorTemp = valor3
    # valor3 = valor1
    # valor1 = valorTemp

#if( valor2 > valor3 ):
 #   resposta = trocaNumeros(valor2, valor3)
  #  valor2 = resposta[0]
   # valor3 = resposta[1] 
    # valorTemp = valor3
    # valor3 = valor2
    # valor2 = valorTemp

# saida
#print(valor1, valor2, valor3)

