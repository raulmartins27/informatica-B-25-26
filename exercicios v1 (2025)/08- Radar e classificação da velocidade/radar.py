velocidade = float(input('Introduza a velocidade do veículo (em km/h):'))
if velocidade <= 60:
    print('Dentro do limite de velocidade.')
else:
    if velocidade <= 100:
        print('Atenção! Velocidade elevada.')
    else:
        print('Excesso de velocidade!')
