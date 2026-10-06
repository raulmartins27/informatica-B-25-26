pacote_diario=50
pacote_semanal=200
pacote_mensal=500

total_pacote_diario=0
total_pacote_semanal=0
total_pacote_mensal=0

recargas=-1
while recargas<0:
    recargas=int(input("Quantas recargas pretende comprar? "))

contador_recargas=0

print("Tipos de recargas: ")
print("1. Pacote diário = 50$00")
print("2. Pacote semanal = 200$00")
print("3. Pacote mensal = 500$00")

while contador_recargas <= recargas:
    pacote=-1
    while pacote != 1 and pacote !=2 and pacote !=3:
        pacote=int(input(f"Qual é o pacote que deseja comprar para a {contador_recargas}ª recarga?"))

        if pacote==1:
               total_pacote_diario=total_pacote_diario+pacote_diario
        elif pacote==2:
               total_pacote_semanal=total_pacote_semanal+pacote_semanal
        else:
               total_pacote_mensal=total_pacote_mensal+pacote_mensal
        contador_recargas+=1


preço_total=total_pacote_diario+total_pacote_semanal+total_pacote_mensal

print("\n----- RESULTADOS -----")
print(f"Total gasto em bilhetes para pacote_diario:{total_pacote_diario}$00.")
print(f"Total gasto em bilhetes para Praia Baixo: {total_pacote_semanal}$00.")
print(f"Total gasto em bilhetes para pacote_mensal: {total_pacote_mensal}$00.")
         
print(f"Preço final total: {preço_total}$00.")