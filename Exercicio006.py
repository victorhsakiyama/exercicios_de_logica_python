def area_do_circulo():
    print("***********************************************")
    print("*****Vamos descobrir a área de um circulo!*****")
    print("***********************************************\n")

    raio = float(input("Digite o raio de um circulo: "))

    area = 3.14 * (raio * raio)
    print("A área de um circulo com raio {} é {}".format(raio, area))

if(__name__ == "__main__"):
    area_do_circulo()