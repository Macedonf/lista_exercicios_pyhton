#Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts),as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é de 18 watts por metro quadrado.

#ENTRADA

Potencia_lam = float (input ("Qual a potencia da lâmpada em watts?")) #72
largura = float (input("Qual a largura do cômodo?")) #4
Comprimento = float (input("Qual o comprimento do Cômodo?")) #4
#Processamento
lampada_metro = float (Potencia_lam / 18)
Metros_quadrados = float (largura * Comprimento)
numero_lampada = float(Metros_quadrados / lampada_metro)

#Saída
print("O número necessário de lâmpadas para iluminar o cômodo é de", numero_lampada, "lâmpadas")

