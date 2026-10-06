num_passageiros=-1
valor_bilhete=0
valor_total=0
escalao1=0
escalao2=0
escalao3=0
escalao4=0
while num_passageiros<=0:
    num_passageiros=int(input("Qual é o número de passageiros? "))
for passageiro in range(1, num_passageiros+1):
    idade=-1
    while idade<0:
        idade=int(input(f"Qual é a idade do passageiro {passageiro}? "))
    if idade<=2:
        valor_bilhete=0
        escalao1+=1
    elif idade<=11:
        valor_bilhete=25000*0.50
        escalao2+=1
    elif idade<=64:
        valor_bilhete=25000
        escalao3+=1
    else:
        valor_bilhete=25000*0.70
        escalao4+=1
    valor_total+=valor_bilhete
print("\n---RESULTADOS---")
print("CLASSIFICAÇAO DA VIAGEM:")
if num_passageiros<=4:
    print("Viagem individual (até 4 passageiros): ")
elif num_passageiros<=9:
    print("Viagem familiar (de 5 a 9 passageiros): ")
else:
    print("Viagem em grupo (10 ou mais passageiros): ")

print("\nO número de passageiros em cada escalao: ")
print(f"Escalao 1 (0 a 2 anos): {escalao1} passageiros")
print(f"Escalao 2 (3 a 11 anos): {escalao2} passageiros")
print(f"Escalao 3 (12 a 64 anos): {escalao3} passageiros")
print(f"Escalao 4 (65 anos ou mais): {escalao4} passageiros")

print(f"\nVALOR TOTAL A PAGAR: {valor_total:.2f} escudos.")