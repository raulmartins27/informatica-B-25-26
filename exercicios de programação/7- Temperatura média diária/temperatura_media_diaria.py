temp_morning=float(input("Qual foi a temperatura de manha? "))
temp_afternoon=float(input("Qual foi a temperatura a tarde? "))
media_temp=(temp_morning+temp_afternoon)/2
media_formatada=f"{media_temp:.1f}".replace(".", ",")

if media_temp<20:
    print(f"A média da temperatura foi de {media_formatada} graus celcius, dia fresco.")
elif media_temp<30: 
    print(f"A média da temperatura foi de {media_formatada} graus celcius, dia agradável.")
else:
    print(f"A média da temperatura foi de {media_formatada} graus celcius, dia quente.")