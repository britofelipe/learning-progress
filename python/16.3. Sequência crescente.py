'''
Sequências comprimento crescente máximo
'''

n, ant, seg = 1, -1, 0

while n != 0:
    n = int(input("Digite o número da sequência: "))
    if n > ant:
        seg += 1
    else:
        n = 0
    ant = n

print("O seu segmento crescente máximo é ", seg)

