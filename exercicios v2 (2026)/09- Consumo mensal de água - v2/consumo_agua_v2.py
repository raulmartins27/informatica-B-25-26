#perguntar qtd de consumo
while True:
    try:
      agua = float(input("Introduza o consumo mensal de água (em m3): "))
      if agua<0:
         print("Valor inválido, o consumo nao pode ser negativo.")
         continue
      break
    except ValueError:
        print("Valor inválido, tente novamente. ")


#perguntar unidade
while True:
    unidades = ["m3", "m³", "litro", "litros", "l", "galão", "galao", "galões", "galoes"]
    try:
      unidade= input("Qual é a unidade? ").strip().lower()
      print("m3, litros ou galões? ")

      if unidade in unidades:
         break
      else:
         print("Unidade inválida, tente novamente.")
    except ValueError:
         print("Unidade inválida, tente novamente.")


#converter e transformar para m3
if unidade in ["m3", "m³"]:
    agua_m3 = agua
elif unidade in ["litro", "litros", "l"]:
    agua_m3 = agua / 1000
else:
    # Considerando galão americano: 1 galão = 3,78541 litros
    agua_m3 = agua * 3.78541 / 1000 


#apresentar o resultado
if agua<=10:
   print("Consumo reduzido.")
elif agua <=20:
   print("Consumo moderado.")
else:
   print("Consumo excessivo!")
