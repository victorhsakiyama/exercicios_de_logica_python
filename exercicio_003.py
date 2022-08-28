#Faça um Programa que peça dois números e imprima a soma.

def soma_numeros():
    print("*******************************")
    print("*****Escolha dois números!*****")
    print("*******************************\n")

    numero1 = int(input("Digite o primeiro número: "))

    numero2 = int(input("Agora o segundo número: "))

    soma = numero1 + numero2
    print("O resultado de {}+{} é {}".format(numero1, numero2, soma))

if(__name__ == "__main__"):
    soma_numeros()