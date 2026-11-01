while True:
  while True:
    try:
      numero=float(input("Digite um número: ").replace(',', '.'))
      break
    except ValueError:
      print("Digite um número válido")
  if numero % 2==0:
    print("O número é par.") 
  else:
    print("O número é impar.")
  continuar=input("Deseja continuar? sim ou nao? ").lower()
  if continuar in ("nao", "n", "nn", "não"):
    break