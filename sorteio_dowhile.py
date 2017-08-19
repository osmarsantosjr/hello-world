import random
qtdsorteios = (int(input("Informe a quantidade de sorteios: ")))
qtdpessoas = (int(input("Informe a quantidade de pessoas: ")))
x=0
while x < qtdsorteios:
    num = random.randint(1,qtdpessoas)
    print ("E o sorteado foi o núm.: %i" %num)
    x += 1