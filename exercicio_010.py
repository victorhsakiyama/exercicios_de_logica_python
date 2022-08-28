#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

def convercao_de_temperatura():
    print("*********************************************")
    print("*****Transformando Celsiu em Farenheit!*****")
    print("*********************************************\n")

    celsius = float(input("Digite a temperatura em graus Celsius: "))

    farenheit = (celsius * 1.8) + 32
    print("{} Celsius é igual a {} Farenheit".format(celsius, farenheit))

if(__name__ == "__main__"):
    convercao_de_temperatura()