'''
Dados n e uma sequência de n números inteiros,
determinar a soma dos números pares
'''

n = int(input("Digite a quantidade de números a serem inseridos: "))
cont = 0
soma = 0

while cont < n:
    num = int(input("Digite o %iº número da sequência: " %(cont+1)))
    if num % 2 == 0:
        soma += num
    cont += 1

if soma == 0:
    if n == 1:
        print("O seu número não é par.")
    if n > 1:
        print("A sua sequência de %i números não possui número par." %n)
else:
    print("A soma dos números pares de sua sequência de %i números é igual a %i" %(n, soma))
