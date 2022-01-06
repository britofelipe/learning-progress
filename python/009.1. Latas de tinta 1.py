print("Bem-vindo à loja de tintas Hidracor.")
area = int(input("Diga a quantidade de m² da área a ser pintada: "))

# A área de cobertura da tinta é de 1 litro para cada 3 metros quadrados
# A tinta é vendida em latas de 18 litros, que custam R$ 80,00
# Dessa forma, uma lata de tinta pinta o equivalente a 18*3=54m² e custa R$80,00.

quantidade=area//54
quantidade=quantidade+1

price = 80 * quantidade

if quantidade == 1:
    print("Você precisará comprar", quantidade, "lata de tinta, o que sairá por R$", price)
else:
    print("Você precisará comprar", quantidade, "latas de tinta, o que sairá por R$", price)