distancia = -1
while distancia < 0:
    distancia = float(input("Qual foi a distância percorrida pelo veículo? "))
unidade_distancia = ""

while unidade_distancia not in ["km", "quilómetro", "quilómetros",
                                "m", "metro", "metros",
                                "cm", "centímetro", "centímetros"]:

    unidade_distancia = input("Qual é a unidade? (km, m ou cm): ").lower()

    if unidade_distancia not in ["km", "quilómetro", "quilómetros",
                                 "m", "metro", "metros",
                                 "cm", "centímetro", "centímetros"]:
        print("Unidade inválida. Tenta novamente.")

if unidade_distancia in ["km", "quilómetro", "quilómetros"]:
    distancia_km = distancia
elif unidade_distancia in ["m", "metro", "metros"]:
    distancia_km = distancia / 1000
else:
    distancia_km = distancia / 100000




tempo = -1
while tempo < 0:
    tempo = float(input("Em quanto tempo o veículo percorreu aquela distância? "))
unidade_tempo = ""

while unidade_tempo not in ["h", "hora", "horas",
                            "m", "min", "minuto", "minutos",
                            "s", "seg", "segundo", "segundos"]:

    unidade_tempo = input("Qual é a unidade de tempo? (horas, minutos ou segundos): ").lower()

    if unidade_tempo not in ["h", "hora", "horas",
                             "m", "min", "minuto", "minutos",
                             "s", "seg", "segundo", "segundos"]:
        print("Unidade inválida. Tenta novamente.")

if unidade_tempo in ["h", "hora", "horas"]:
    tempo_horas = tempo
elif unidade_tempo in ["m", "min", "minuto", "minutos"]:
    tempo_horas = tempo / 60
else:
    tempo_horas = tempo / 3600



velocidade = distancia_km / tempo_horas
if velocidade <= 60:
    print(f"A velocidade do veículo era {velocidade} km/h.\nDentro do limite.")
elif velocidade <= 100:
    print(f"A velocidade do veículo era {velocidade} km/h.\nAtenção! Velocidade elevada.")
else:
    print(f"A velocidade do veículo era {velocidade} km/h.\nExcesso de velocidade!")