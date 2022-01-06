'''Faça um programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo'''

numero=int(input("Digite o número desejado: "))

if numero//100 >= 0:
    centenas = numero//100
    if centenas > 1:
        print(centenas, "centenas")
    elif centenas == 1:
        print(centenas, "centena")
    numero = numero % 100
if numero//10 >= 0:
    dezenas = numero//10
    if dezenas > 1:
        print(dezenas, "dezenas")
    elif dezenas == 1:
        print(dezenas, "dezena")
    numero = numero % 10
if numero//1 >= 0:
    unidades = numero
    if unidades > 1:
        print(unidades, "unidades")
    elif unidades == 1:
        print(unidades, "unidade")
    numero = numero % 10