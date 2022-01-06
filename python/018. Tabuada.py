'''
Peça para o usuário entrar com o início e o fim da tabuada
e imprima a tabuada correspondente dentro dos intervalos considerados
'''

inicio = int(input("Diga o valor do início da tabuada: "))
fim = int(input("Diga o valor do fim da tabuada: "))
n = 1
m = 1

for n in range (inicio, fim + 1):
    print("Tabuada do { }".format(n))
    for m in range (inicio, fim + 1):
        print ("%i x %i = %i" %(n, m, n*m))

