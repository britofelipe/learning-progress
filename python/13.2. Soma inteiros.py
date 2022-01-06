'''

'''

n = int(input("Digite um número: "))
soma = 0
aux = n

while aux != 0:
    soma = soma + aux
    aux = aux - 1
print("A soma dos", n, "primeiros números inteiros é igual a", soma)
