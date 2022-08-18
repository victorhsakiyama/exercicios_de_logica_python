def convercao_de_temperatura():
    print("*********************************************")
    print("*****Transformando Farenheit em Celsius!*****")
    print("*********************************************\n")

    farenheit = float(input("Digite a temperatura em Farenheit: "))

    celsius = 5 * (farenheit - 32) / 9
    print("{} Farenheit é igual a {} Celsius".format(farenheit, celsius))

if(__name__ == "__main__"):
    convercao_de_temperatura()