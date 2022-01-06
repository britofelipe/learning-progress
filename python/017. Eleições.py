'''
Numa eleição existem três candidatos
Faça um programa que peça o número total de eleitores
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato
'''

eleitores = int(input("Diga o número de eleitores da eleição: "))
print("Na presente eleição, concorrem os seguintes candidatos: ")
print("Fernando Pessoa - Número 1")
print("Álvaro Campos - Número 2")
print("Ricardo Reis - Número 3")
voto1 = 0
voto2 = 0
voto3 = 0
nulos = 0

for n in range (1, eleitores+1):
    voto = int(input("Eleitor nº %i, diga o número do seu candidato: " %n))
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    else:
        print("Voto nulo")
        nulos += 1

print("Os candidatos obtiveram o seguinte número de votos: ")
print("Fernando Pessoa - %i votos" %voto1)
print("Álvaro Campos - %i votos" %voto2)
print("Ricardo Reis - %i votos" %voto3)
print("Nulos - %i votos\n" %nulos)

if voto1 > voto2:
    if voto1 > voto3:
        maisvotado = voto1
        print("O vencedor dessa eleição foi o candidato Fernando Pessoa, com %i votos" %voto1)
elif voto2 > voto1:
    if voto2 > voto3:
        maisvotado = voto2
        print("O vencedor dessa eleição foi o candidato Álvaro Campos, com %i votos" % voto2)
elif voto3 > voto1:
    if voto3 > voto2:
        maisvotado = voto3
        print("O vencedor dessa eleição foi o candidato Ricardo Reis, com %i votos" % voto3)
if voto1 == voto2 or voto1 == voto3 or voto2 == voto3:
    print("A eleição empatou\n")
