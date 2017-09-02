#coding: utf-8

print ("=========================\nGeração de Fatores Primos\n=========================\n")

'''========================
 Definição de variáveis:
========================'''

num = int(input('Insira um número inteiro e positivo: ')) #solicita número ao usuário
while num < 2:
    if num == 1:
        print ("você digitou 1, digite um número superior \n")
        num = int(input('Insira um número inteiro e positivo: ')) #solicita número ao usuário
    else:
        num = int(input('Insira um número inteiro e positivo: ')) #solicita número ao usuário

primos = [2, 3, 5, 7]                           #conjunto básico de números primos
ultimo = primos[-1] + 2                         #soma dois ao último item da lista de num. primos
fatores = []                                    #criação da lista de fatores
num2 = num                                      #para exibir ao final

'''========================================================================================
Adiciona números à lista de números primos (Caso o número informado seja maior que 7)
========================================================================================'''

while num > ultimo:
    for primo in primos:           # varre a lista e realiza a checagem
        if ultimo % primo == 0:    # se o número for divisível pelo núm. da lista, soma-se 2.
            ultimo += 2         
    primos.append(ultimo)       # se for primo, adiciona o número a lista.

''' ============================
Gera lista de fatores primos:
============================='''

for fat in primos:                # varre a lista e realiza a checagem
    while num % fat == 0:         # se divisível pelo número da lista, ele é adicionado na lista de fatores
        fatores.append(fat)
        if num == fat:            # se o núm. solicitado for igual ao fator, a função é interrompida
            break
        else:                   # se o núm. solicitado for diferente do fator, o num. solicitado é subtraído pelo fator.
            num = num // fat

''' =================
Exibe o resultado:
====================='''
# Exibirá do primeiro item ao penúltimo da lista acrescentando o "x" e então exibirá o último item.

print ("\n",num2,end=" = ")
f = 0
while f < len(fatores)-1:
    print (fatores[f], end=' x ')
    f += 1
print(fatores[-1],"\n")