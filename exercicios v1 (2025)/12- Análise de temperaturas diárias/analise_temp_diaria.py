qtd_temperaturas=-1
while qtd_temperaturas<0:
    qtd_temperaturas=int(input("Qual é a quantidade de temperaturas que deseja introduzir?"))

contador=1
soma_temperatura=0
while contador<=qtd_temperaturas:
    temperatura=int(input(f"Qual foi a temperatura registada no dia {contador} "))
    soma_temperatura=soma_temperatura+temperatura
    contador+=1

media_temperatura=soma_temperatura/qtd_temperaturas
print(f"A média da temperatura é:{round(media_temperatura, 2)}")
if media_temperatura<15:
    print('Clima Frio')
else:
    if media_temperatura<25:
        print('Clima Agradavél')
    else:
        print('Clima Quente')
