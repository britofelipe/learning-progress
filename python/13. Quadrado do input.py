'''
Dada uma sequência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados
'''

x = int(input("Digite um número: "))

while x != 0:
    print("O quadrado de", x, "é", x*x)
    x = int(input("Digite um número: "))

if x == 0:
    print("Você encerrou o programa")