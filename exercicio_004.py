#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media_bimestral():
    print("*******************************")
    print("*****Média de 4 bimestres!*****")
    print("*******************************\n")

    bimestre1 = int(input("Digite a nota do primeiro bimestre: "))

    bimestre2 = int(input("Agora do segundo bimestre: "))

    bimestre3 = int(input("O terceiro bimestre: "))

    bimestre4 = int(input("E por fim o quarto bimestre: "))

    media = (bimestre1 + bimestre2 + bimestre3 + bimestre4)/4
    print("A média das suas notas {}, {}, {} e {} é {}".format(bimestre1, bimestre2, bimestre3, bimestre4, media))

if(__name__ == "__main__"):
    media_bimestral()