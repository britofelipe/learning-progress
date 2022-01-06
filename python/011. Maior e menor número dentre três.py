'''
Faça um programa que leia três números e mostre o maior e o menor deles
'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b >= c:
    print("O maior número é", a)
    print("O menor número é", c)
elif a >= c >= b:
    print("O maior número é", a)
    print("O menor número é", b)
elif b >= a >= c:
    print("O maior número é", b)
    print("O menor número é", c)
elif b >= c >= a:
    print("O maior número é", b)
    print("O menor número é", a)
elif c >= a >= b:
    print("O maior número é", c)
    print("O menor número é", b)
elif c >= b >= a:
    print("O maior número é", c)
    print("O menor número é", a)