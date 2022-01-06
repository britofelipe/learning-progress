'''
Dado um número natural n > 10, verificar se n é palíndromo
'''

n = int(input("Digite o seu número: "))

aux, rev = n, 0

while aux > 0:
    rev = 10*rev + (aux % 10)
    aux = aux // 10

if rev == n:
    print("O seu número é palíndromo")
else:
    print("O seu número não é palíndromo")