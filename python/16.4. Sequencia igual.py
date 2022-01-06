'''
Segmentos iguais consecutivos
'''

cont, ant, seg = 0, -1, 0
n = int(input("Digite a quantidade de números na sequência: "))

while cont < n:
    num = int(input("Digite o próximo número da sequência: "))
    if ant == num:
        seg += 1
    ant = num
    cont += 1

print("A sua sequência de %i números tem %i números iguais ao anterior" %(n, seg))