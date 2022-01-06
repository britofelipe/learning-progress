'''
Dado um inteiro não-negativo n, verificar se n é triangular
120 é triangular, pois 4*5*6 == 120
'''

n = int(input("Digite o número: "))

x = 1
y = 2
z = 3

while x*y*z <= n:
    if x*y*z == n:
        print("O número que você digitou é triangular")
    x += 1
    y += 1
    z += 1
if (x - 1) * (y - 1) * (z - 1) != n:
    print("O número que você digitou não é triangular")

x = 1
y = 2
z = 3
while x*y*z < n:
    x += 1
    y += 1
    z += 1
if x * y * z == n:
    print("É triangular")
else:
    print("Não é triangular.")
