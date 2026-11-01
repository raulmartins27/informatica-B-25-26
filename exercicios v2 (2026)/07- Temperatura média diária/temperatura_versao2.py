def unidade_medida_temperatura(pergunta, unidades_validas):
    while True:
        try:
            unidade=input(pergunta).strip().lower()
            if unidade in unidades_validas:
                return unidades_validas[unidade]
            else: print("Unidade inválida. Digite novamente! ")
        except ValueError:
            print("Unidade inválida. Digite novamente. ")


unidades_validas = {
    # Celsius
    "c": "celsius",
    "ºc": "celsius",
    "°c": "celsius",
    "celsius": "celsius",
    "celcius": "celsius",
    "°C celsius": "celsius",
    "°C celcius": "celsius",

    # Fahrenheit
    "f": "fahrenheit",
    "ºf": "fahrenheit",
    "°f": "fahrenheit",
    "fahrenheit": "fahrenheit",
    "°C fahrenheit": "fahrenheit",

    # Kelvin
    "k": "kelvin",
    "kelvin": "kelvin",
    "°C kelvin": "kelvin"
}

#temperatura de manha
while True:
    try:
       temperatura_manha=float(input("Qual foi a temperatura de manha? ").replace("," , "."))
       break 
    except ValueError:
        print("Temperatura inválida, tente novamente. ")


#unidade temperatura de manha    
unidade_temperatura=unidade_medida_temperatura("Qual é a unidade da temperatura? ", unidades_validas) 

#transformar temperatura de manha em celcius
if unidade_temperatura=="celcius":
    temperatura_manha=temperatura_manha
    
elif unidade_temperatura=="fahrenheit":
    temperatura_manha=(temperatura_manha - 32) *  5/9

elif unidade_temperatura=="kelvin":
    temperatura_manha-=273.15



#temperatura da tarde
while True:
    try:
        temperatura_tarde=float(input("Qual foi a temperatura à tarde? ").replace("," , "."))
        break
    except ValueError:
        print("Temperatura inválida, tente novamente. ")

#unidade temperatura da tarde    
unidade_temperatura=unidade_medida_temperatura("Qual é a unidade da temperatura? ", unidades_validas)

#transformar unidade temperatura da tarde em celcius
if unidade_temperatura=="celsius":
    temperatura_tarde=temperatura_tarde
    
elif unidade_temperatura=="fahrenheit":
    temperatura_tarde=(temperatura_tarde - 32) *  5/9

elif unidade_temperatura=="kelvin":
    temperatura_tarde-=273.15



#calculo media temperatura
media_temperatura = (temperatura_manha+temperatura_tarde)/2



if media_temperatura<20:
    print(f"A média da temperatura foi de {media_temperatura} °C, dia fresco.")
elif media_temperatura<30: 
    print(f"A média da temperatura foi de {media_temperatura} °C, dia agradável.")
else:
    print(f"A média da temperatura foi de {media_temperatura} °C, dia quente.")
