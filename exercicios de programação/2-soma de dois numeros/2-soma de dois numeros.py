print("Seja bem vindo ao programa da soma de dois numeros")
numero1=float(input('Qual é o valor do primeiro numero?').replace(",", "."))
numero2=float(input('Qual é o valor do segundo numero?').replace(",", "."))
result=numero1+numero2
if result.is_integer():
    print(f"O resultado da soma dos dois números é {int(result)}")
else:
    print(f"O resultado da soma dos dois números é {result}")