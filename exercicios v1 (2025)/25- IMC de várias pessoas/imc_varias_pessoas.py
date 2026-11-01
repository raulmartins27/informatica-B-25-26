qtd_pessoas=-1
escalao1=0
escalao2=0
escalao3=0
while qtd_pessoas<0:
    qtd_pessoas=int(input("Quantas pessoas serao analisadas? "))
for i in range(1,qtd_pessoas+1):
    peso=-1
    while peso<0:
        peso=float(input(f"Qual é o peso (em KG) da pesssoa {i}? "))
    altura=-1
    while altura<0:
         altura=int(input(f"Qual é a altura (em CM) da pessoa {i}? "))
    imc=peso/(altura**2)
    print(f"O imc da pessoa {i} é de {imc:.2f} valores.")

    if imc<18.5:
        print("Abaixo do peso.")
        escalao1+=1
    elif imc<=24.9:
        print("Peso normal.")
        escalao2+=1
    else:
        print("Excesso de peso.")
        escalao3+=1
print("\nO número de pessoas em cada escalão: ")
print(f"Escalão 1: {escalao1} pessoas. ")
print(f"Escalão 2: {escalao2} pessoas. ")
print(f"Escalão 3: {escalao3} pessoas. ")
print(f"Total de pessoas analisadas: {qtd_pessoas}. ")
