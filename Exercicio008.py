def salario():
    print("******************************************************")
    print("*****Vamos descobrir quanto você ganha seu pobre!*****")
    print("******************************************************\n")

    valor_hora = float(input("Digite quanto você ganha por hora: "))

    horas_mes = int(input("Agora quantas horas você trabalha por mês: "))

    salario = valor_hora * horas_mes
    if(salario >= 2380):
        print("Parabéns! Ganhano R${} você já pode declarar imposto de renda.".format(salario))
    else:
        print("Só R${}? Você deve ser morador de Sarandi, meus pêsames...".format(salario))

if(__name__ == "__main__"):
    salario()