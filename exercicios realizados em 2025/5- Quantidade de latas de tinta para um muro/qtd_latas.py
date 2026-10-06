altura = float(input('Qual é a altura do muro? (em metros):'))
comprimento = float(input('Qual é o ocomprimento do muro? (em metros):'))
area = altura * comprimento
latas = area // 6
resto = area % 6
if resto != 0:
    latas = latas+1
 
print('São necessárias', int(latas), 'latas de tinta para pintar o muro.')