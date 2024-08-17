#Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de azulejos possui 1,5 m2.

#Entrada
Comprimento = float (input ("Qual o comprimento da cozinha?"))
Largura =  float (input ("Qual a largura da cozinha?"))
Altura =  float (input ("Qual a altura da cozinha?"))
Caixa_d_azulejos = float (1.5)
#Processamento
area_parede = float (Altura * Largura)
Total_d_caixas = float (area_parede / Caixa_d_azulejos)
#Saída

print ("a cozinha possui", area_parede, "m²", ", e necessita de", Total_d_caixas, "caixas de azulejos para colocar em todas as paredes")