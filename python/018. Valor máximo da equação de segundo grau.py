'''
Sabe-se que um número da forma n**3 é igual a soma de n ímpares consecutivos
Exemplo: 1**3 = 1, 2**3 = 2+5, 3**3 = 7+9+11, 4**3 = 13+15+17+19
Dado m, determine os ímpares consecutivos cuja soma é igual a n**3 para n
assumindo valores de 1 a m
'''

print("n³")
m = int(input("Digite o valor de n: "))
x = y = valor = valor_maximo = 0

for m in range(0, m):
    for n in range(0, n):
        if m*n - m**2 + n > valor_maximo:
            valor_maximo = m*n - m**2 + n
            x = m
            y = n
print("Para a coordenada (%i,%i), tem-se o valor %i como máximo para a equação" %(x, y, valor_maximo))
