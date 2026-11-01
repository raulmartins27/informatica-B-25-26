Assomada=250
Praia_Baixo=300
Tarrafal=400

total_assomada=0
total_Praia_Baixo=0
total_Tarrafal=0

qtd_bilhetes=-1
while qtd_bilhetes<0:
    qtd_bilhetes=int(input("Qual é a quantidade de bilhetes que deseja comprar? "))

contador=1
print("Preços e destinos: ")
print("1. Assomada=250$00")
print("2. Praia_Baixo=300$00")
print("3. Tarrafal=400$00")


while contador<=qtd_bilhetes:
    destino=-1
    while destino != 1 and destino !=2 and destino !=3:
     destino=int(input(f"Qual é o destino do bilhete {contador}?  "))

    if destino==1:
       total_assomada=total_assomada+Assomada
    elif destino==2:
       total_Praia_Baixo=total_Praia_Baixo+Praia_Baixo
    else:
       total_Tarrafal=total_Tarrafal+Tarrafal
    contador+=1
preço_total=total_assomada+total_Praia_Baixo+total_Tarrafal
print("\n----- RESULTADOS -----")
print(f"Total gasto em bilhetes para Assomada:{total_assomada}$00.")
print(f"Total gasto em bilhetes para Praia Baixo: {total_Praia_Baixo}$00.")
print(f"Total gasto em bilhetes para Tarrafal: {total_Tarrafal}$00.")
 
print(f"Preço final total: {preço_total}$00.")