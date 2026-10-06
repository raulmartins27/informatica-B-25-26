consumo_agua=-1
preço_total=0
while consumo_agua<=0:
    consumo_agua=int(input("Qual foi o consuno de agua em m3?" ))
for i in range(1, consumo_agua+1):
    if i<=5:
        preço_total+=250
    elif i<=10:
        preço_total+=300
    else:
        preço_total+=400
print(f"\nconsumo total: {consumo_agua} m3.")
print(f"Valor total final: {preço_total} escudos.")