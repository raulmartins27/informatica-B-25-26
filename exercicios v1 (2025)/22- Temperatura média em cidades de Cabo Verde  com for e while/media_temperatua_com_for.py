qtd_cidades=-1
while qtd_cidades<0:
    qtd_cidades=int(input("Quantas cidades deseja analisar? "))
    if qtd_cidades<0:
        print("Itntroduza um valor positivo.")

soma_temperatura=0       
for i in range(1, qtd_cidades+1):
    temperatura=-1
    while temperatura<10 or temperatura>45:
        temperatura=float(input(f"Qual foi a temperatura registada na cidade {i} em (°C)? "))
        if temperatura<10 or temperatura>45:
            print("Temperatura irrealista em Cabo Verde, introduza novamente.")
        soma_temperatura+=temperatura

media=soma_temperatura/qtd_cidades
print(f"\nA temperatura média das cidades é: {media:.2f} °C")