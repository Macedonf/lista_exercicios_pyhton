#Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
from datetime import date

#Entrada
anoNasc = int (input("Qual o ano do seu nascimento?"))
#ANOATUAL = date.today().year

#Processamento
def verificarOpcaoVoto(idadeUser):
    #resposta = ""
    #idade = ANOATUAL -anoNasc
    if (idadeUser >= 16):
    #resposta =""
        return "sim"

    else:
    #resposta="não"
     return "Não"

def idade(nascimento):
    ANOATUAL = date.today().year
    return ANOATUAL - nascimento

idadeAtualUser = idade(anoNasc)
#Saída

print("Você poderá votar este ano:", verificarOpcaoVoto(idadeAtualUser))
print("Porquê você tem ", idadeAtualUser,"idade")
