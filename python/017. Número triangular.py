'''
Um número triangular é calculado pela fórmula triangular = n * (n+1)/2
Sendo n o índice desse número triangular
Escreva um programa que imprima os números triangulares com índices múltiplos de 5 entre 5 e 50
'''

n = 0

print("Os números triagulares entre 5 e 50 são:")
for n in range (5, 51, 5):
    formula = (n*(n+1)/2)
    print(formula)