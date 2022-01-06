# A área de cobertura da tinta é de 1 litro para cada 6 metros quadrados
# A tinta é vendida em latas de 18 litros, que custam R$ 80,00
# Dessa forma, uma lata de tinta pinta o equivalente a 18*6=108m² e custa R$80,00.

print("Bem-vindo à loja de tintas Hidracor.\n")
print("Aqui nós vendemos:")
print("\tLatas de tinta de 18 litros, por R$ 80,00.")
print("\tGalões de tinta de 4 litros, por R$ 25,00.\n")
area = int(input("Diga a quantidade de m² da área a ser pintada: "))

area = area * 1.1
excesso = area - int(area)
area = int(area)

if excesso > 0:
    area = area + 1

print("\tPor precaução, recomendamos que você compre quantidade de tinta o suficiente para a área de", area, "m², ou seja, com 10% de margem.\n")

litros = area//6
if area % 6 > 0:
    litros = litros + 1

print("Considerando que cada litro de tinta é capaz de preencher 6m² de área, você precisará de", litros,"litros de tinta.\n")

print("1) Comprar apenas latas de 18 litros")
latas = litros//18
if litros % 18 > 0:
        latas = latas + 1

print("Serão necessãrias", latas, "latas")
print("Obteremos", latas*18, "litros")
print("Total: R$", latas*80)

print("\n2) Comprar apenas galões de 4 litros")
galoes = litros // 4
if litros % 4 > 0:
    galoes = galoes + 1

print("Serão necessãrios", galoes, "galoes")
print("Obteremos", galoes * 4, "litros")
print("Total: R$", galoes * 25)

print("\n3) Misturar latas e galões, de forma que o preço seja menor")

latas = litros//18
galoes = 0
litros_restantes = litros % 18

if litros_restantes <= 3*4:
    galoes = litros_restantes // 4
    if litros_restantes % 4 > 0:
        galoes += 1
else:
    latas += 1

if latas == 1:
    print("\nVocê precisará comprar", latas, "lata de tinta, o que sairá por R$", latas*80,  ", equivalendo a", latas*18, "litros de tinta")
else:
    print("Você precisará comprar", latas, "latas de tinta, o que sairá por R$", latas*80, ", equivalendo a", latas*18, "litros de tinta")

if galoes == 1:
    print("Você precisará comprar", galoes, "galão de tinta, o que sairá por R$", galoes*25, ", equivalendo a", galoes*4, "litros de tinta")
else:
    print("Você precisará comprar", galoes, "galoes de tinta, o que sairá por R$", galoes*25, ", equivalendo a", galoes*4, "litros de tinta")

print("No total, você gastará R$", latas*80 + galoes*25)