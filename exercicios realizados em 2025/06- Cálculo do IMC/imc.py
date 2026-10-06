peso = float(input('Introduza o peso (em kg):'))
altura = float(input('Introduza a altura (em metros):'))
 
imc=peso/(altura**2)
 
print('O seu IMC é:')
 
if imc<20:
    print('Abaixo do peso')
else:
    if imc<30:
        print('Peso adequado')
    else:
        print('Obeso')