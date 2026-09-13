while True:
    numero=float(input("Digite um número e veja se ele é par ou ímpar: ").replace(',', '.'))
    if numero % 2==0:
      print("O número é par.") 
    else:
      print("O número é impar.")
    continuar=input("Deseja continuar? sim ou nao?")
    if continuar.lower()== "nao":
     break
