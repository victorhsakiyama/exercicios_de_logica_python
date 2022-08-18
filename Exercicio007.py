def area_do_quadrado():
    print("*********************************************************")
    print("*****Vamos descobrir o dobro da área de um quadrado!*****")
    print("*********************************************************\n")

    largura = float(input("Digite a largura do quadrado: "))

    comprimento = float(input("Agora o comprimento do quadrado: "))

    area = largura * comprimento
    dobro_da_area = area * 2
    print("Um quadrado com largura {}m e comprimento {}m, possui uma área de {}m²".format(largura, comprimento, area))
    print("O dobro dessa área é {}m²".format(dobro_da_area))

if(__name__ == "__main__"):
    area_do_quadrado()