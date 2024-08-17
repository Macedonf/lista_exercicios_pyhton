#Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (Km) no início do dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$)recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.

#Entrada
Preco_combustivel = float (4.87)
km_inicio = float (input("Qual o odômetro no inicio do dia?"))
Km_Fim = float ( input ("Qual o Odômetro no fim do dia?"))
Litros_Comb = float (input("Quantos litros de combustível foram gastos no decorer do dia?"))
Dinheiro_recebido = float (input("Qual o valor total recebido no dia de trabalho"))

#Processamento
Km_rodados = float (Km_Fim - km_inicio) 
Consumo = float (Km_rodados / Litros_Comb)
Gasto_total_comb = float (Litros_Comb * Preco_combustivel)
lucro = float ( Dinheiro_recebido - Gasto_total_comb)

#Saída
print ( "o consumo do carro foi de", Consumo, "km por litro e o seu lucro foi de", lucro, "reais")