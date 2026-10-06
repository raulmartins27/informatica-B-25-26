temp_dia=float(input("Qual foi a temperatura de manha? "))
temp_tarde=float(input("Qual foi a temperatura a tarde? "))
media_temp=(temp_dia+temp_tarde)/2

if media_temp<20:
    print(f"A média da temperatura foi de {media_temp} graus, dia fresco.")
elif media_temp<30: 
    print(f"A média da temperatura foi de {media_temp} graus, dia agradável.")
else:
    print(f"A média da temperatura foi de {media_temp} graus, dia quente.")