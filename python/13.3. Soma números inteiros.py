'''
Questão anterior adaptada
'''

n = int(input("Digite a quantidade de números a serem somados: "))
soma = 0
cont = 0

while cont < n:
    aux = int(input("Digite um número da sequência: "))
    if aux > 0:
        soma = soma + aux
    cont = cont + 1
print("A soma dos", n, "primeiros números inteiros é igual a", soma)