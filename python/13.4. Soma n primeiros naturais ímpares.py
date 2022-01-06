'''
Dado um número inteiro positivo n, imprimir os n primieors naturais ímpares
'''

n = int(input("Digite a quantidade de números naturais ímpares a serem somados: "))
soma = 0
aux = (n * 2) - 1

while aux > 0:
    soma = soma + aux
    aux = aux - 2

print("A soma dos", n, "primeiros números naturais ímpares é igual a", soma)
