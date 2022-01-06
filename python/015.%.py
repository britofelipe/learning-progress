#n = int(input("Digite o número de pessoas: "))

#cont = 0

dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))
idade = int(input("Digite a idade a ser completa: "))

print("A pessoa fará", idade, "anos no dia", dia, "/", mes, "/", ano + idade)
print("A pessoa fá %i anos no dia %i/%i/%i\n" %(idade, dia, mes, ano + idade))

#para inteiros = %i ou %d
#para % --> %%
#para floats --> %f
#para strings --> #s