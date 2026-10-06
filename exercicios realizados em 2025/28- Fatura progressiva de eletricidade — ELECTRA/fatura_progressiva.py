consumo_eletricidade=-1
escalao1=0
escalao2=0
escalao3=0
escalao4=0
valor_consumo=0

while consumo_eletricidade<=0:
    consumo_eletricidade=int(input("Qual foi o seu consumo (em kWh) de eletricidade? "))
for i in range(1, consumo_eletricidade+1):
    if i<=50:
        valor_consumo+=30
        escalao1+=1
    elif i<=100:
        valor_consumo+=50
        escalao2+=1
    elif i<=150:
        valor_consumo+=80
        escalao3+=1
    else:
        valor_consumo+=100
        escalao4+=1

print("Consumo total em kWh:")       
if consumo_eletricidade<=50:
    print(f"Escalão 1 (baixo consumo): {consumo_eletricidade} kWh.")
elif consumo_eletricidade<=100:
    print(f"Escalão 2 (consumo medio): {consumo_eletricidade} kWh.")
elif consumo_eletricidade<=150:
    print(f"Escalão 3 (alto consumo): {consumo_eletricidade} kWh.")
else:
    print(f"Escalão 4 (consumo excessivo): {consumo_eletricidade} kWh.")

print(f"Escalão 1 (Baixo consumo): {escalao1} kWh." )
print(f"Escalão 2 (consumo medio): {escalao2} kWh." )
print(f"Escalão 3 (alto consumo): {escalao3} kWh." )
print(f"Escalão 4 (consumo excessivo): {escalao4} kWh." )
print(f"\nValor total da fatura: {valor_consumo} escudos. ")