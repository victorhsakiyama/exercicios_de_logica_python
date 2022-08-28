#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

def salario():
    print("********************************************")
    print("*****Vamos descobrir quanto você ganha!*****")
    print("********************************************\n")

    valor_hora = float(input("Digite quanto você ganha por hora: "))

    horas_mes = int(input("Agora quantas horas você trabalha por mês: "))

    salario = valor_hora * horas_mes
    if(salario >= 2380):
        print("Parabéns! Ganhando R${} você já pode declarar imposto de renda.".format(salario))
    else:
        print("Só R${}? Meus pêsames...".format(salario))

if(__name__ == "__main__"):
    salario()