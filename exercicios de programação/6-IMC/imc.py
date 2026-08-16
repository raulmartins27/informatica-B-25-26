peso=float(input("Qual é o teu peso em kg? "))
altura=float(input("Qual é a tua altura? "))
imc=peso/altura**2
if imc<20:
    print(f"O teu IMC é de {imc} valores, estás abaixo do peso.")
elif imc<30:
     print(f"O teu IMC é de {imc} valores, estás com o peso adequado.")
else:
        print(f"O teu IMC é de {imc} valores, estás obeso.")