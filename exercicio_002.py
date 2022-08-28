#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

def escolhe_numero():
    print("*******************************")
    print("*****Escolha o seu número!*****")
    print("*******************************\n")

    numero = input("Qual número? ")
    print("O número escolhido foi: ", numero)

if(__name__ == "__main__"):
    escolhe_numero()
