agua = -1
while agua <= 0:
    agua = float(input('Introduza o consumo mensal de água (em m3): '))
if agua <= 10:
    print('Consumo Reduzido')
else:
    if agua <= 20:
        print('Consumo Moderado')
    else:
        print('Consumo Excessivo!')