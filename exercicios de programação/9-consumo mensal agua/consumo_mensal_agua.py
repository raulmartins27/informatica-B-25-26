consumo=-1
while consumo<0:
    consumo=float(input("Introduza a quantidade de agua consumida (em m³) "))
if consumo <=10:
    print("Consumo reduzido.")
elif consumo<=20:
    print("Consumo moderado.")
else:
    print("Consumo excessivo!")