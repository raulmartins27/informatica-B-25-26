print("seja bem vindo ao valor absoluto de um determinado número")
valor= input(float("Digite o número em que deseja ver o seu valor absoluto. "))
if valor > 0:
    VA= valor * 1
else:
    VA= valor * (-1)
print (f"o valor absoluto do {valor} é: {VA}.")
