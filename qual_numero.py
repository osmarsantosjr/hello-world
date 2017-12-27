import random
cont = True
while (cont == True):
    num = random.randint(1,10)
    guess = int(input("Tente advinhar o número de 1 à 10: "))
    while(guess != num):
        if guess > num:
            guess = int (input("Muito alto, tente novamente: "))
        else:
            guess = int (input("Muito baixo, tente novamente: "))
    print ("Parabéns, você acertou!")
    choice = (input("Digite S e pressione ENTER para continuar ou apenas ENTER para encerrar!"))
    if choice != "S" and choice != "s":
        cont = False
