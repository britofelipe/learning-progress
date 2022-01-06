'''Faça um programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo'''

numero=int(input("Digite o número desejado: "))

if numero//100 >= 0:
    centenas = numero//100
    if centenas > 1:
        print(centenas, "centenas")
    elif centenas == 1:
        print(centenas, "centena")
if numero//100 >= 0:
    centenas = numero//100
    if centenas > 1:
        print(centenas, "centenas")
    elif centenas == 1:
        print(centenas, "centena")