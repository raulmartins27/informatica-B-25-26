qtd_bilhete=-1
while qtd_bilhete < 0:
    qtd_bilhete=int(input("Qual é a quantidade de bilhetes desejada? "))
    if qtd_bilhete<0:
        print("Valor inválido, tente novamente. ")

qtd_escalao1=0 #idade inferior a 10 anos - gratuita
qtd_escalao2=0 #idade entre 10 e 15 anos - 500$00
qtd_escalao3=0 #idade igual ou superior a 16 anos - 750$00

soma_preço_escalao1=0
soma_preço_escalao2=0
soma_preço_escalao3=0

for i in range(1, qtd_bilhete+1):
    idade_utilizador=-1
    while idade_utilizador<=0:
        idade_utilizador=int(input(f"Qual é a idade da pessoa que vai utilizar o bilhete {i}? "))
        if idade_utilizador<0:
            print("Idade inváida, introduza novamente. ")

    if idade_utilizador<10:
        qtd_escalao1+=1
    elif idade_utilizador<=15:
        qtd_escalao2+=1
        soma_preço_escalao2+=500
    else:
        qtd_escalao3+=1
        soma_preço_escalao3+=750

preço_final=soma_preço_escalao1+soma_preço_escalao2+soma_preço_escalao3

print("\n----RESULTADOS----")
print(f"bilhetes vendidos para a escalao 1: {qtd_escalao1} ")
print(f"Valor total do escalao 1: {soma_preço_escalao1}")

print(f"\nbilhetes vendidos para a escalao 2: {qtd_escalao2} ")
print(f"Valor total do escalao 2: {soma_preço_escalao2}")

print(f"\nbilhetes vendidos para a escalao 3: {qtd_escalao3} ")
print(f"Valor total do escalao 3: {soma_preço_escalao3}")

print(f"\nValor final total à pagar: {preço_final}$00. ")