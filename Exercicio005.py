def convercao_de_medidas():
    print("**********************************")
    print("*****Vamos converter medidas!*****")
    print("**********************************\n")

    metros = float(input("Digite uma medida em metros: "))

    centimetros = metros * 100
    print("A medida {}m que você digitou é igual a {}cm".format(metros, centimetros))

if(__name__ == "__main__"):
    convercao_de_medidas()