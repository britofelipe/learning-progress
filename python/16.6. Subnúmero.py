"""
São dados dois números inteiros positivos p e q,
sendo que o número de dígitos de p é menor ou igual ao número de dígitos de q.
Verificar se p é um subnúmero de q.

Exemplos:
p = 23, q = 57238, p é subnúmero de q.
p = 23, q = 258347, p não é subnúmero de q.
"""

p = int(input("Digite o valor de p: "))
q = int(input("Digite o valor de q: "))
aux = p
dig = 0

while aux != 0:
    aux //= 10
    dig += 1

if p // 10 < q // 10:
    while q > 1:
        if q % (10 ** dig) == p:
            print("p é subnúmero de q")
        q //= 10

else: print("p tem o número de dígitos igual ou superior ao de q")