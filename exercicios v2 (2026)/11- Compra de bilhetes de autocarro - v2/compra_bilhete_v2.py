def validar_qtd_minimo(pergunta, minimo):
    while True:
        try: 
         valor = int(input(pergunta)).strip()
         if valor <= minimo :
            print(f"Valor inválido,\n o valor deve ser igual ou superior {minimo}. ")
         else:
            return valor
        except ValueError:
           print("Valor inválido, tente novamente. ")

def validar_qtd_maximo(pergunta, maximo):
    while True:
        try: 
         valor = int(input(pergunta).strip())
         if valor > maximo :
            print(f"Valor inválido,\n o valor deve ser igual ou inferior {maximo}. ")
         else:
            return valor
        except ValueError:
           print("Valor inválido, tente novamente. ")


def main():
    preço_destino = {"Assomada" : "250" ,
                     "Praia_Baixo" : "300" ,
                     "Tarrafal" : "400"}
    
    escolha_assomada=[]
    escolha_praiabaixo=[]
    escolha_tarrafal=[]    

        #aparece a tabela de destino e o respetivo preço
    for destino, preco in preço_destino.items():
           print(f"{destino}: {preco}$ ") 

        #pergunta qtd d bilhetes desejadas         
    qtd_bilhete = validar_qtd_minimo("Deseja comprar quantos bilhetes? ", 1)

        #pergunta destino d cada bilhete
    for qtd in range(qtd_bilhete):  
        destino = validar_qtd_maximo(f"Qual é o destino do bilhete {qtd+1}? ", 3)
        if destino == 1:
            escolha_assomada.append(250)
        elif destino == 2:
            escolha_praiabaixo.append(300)
        else:
            escolha_tarrafal.append(400)
            return destino
    
       
main() 


def resultados():
  total_assomada = sum(escolha_assomada)
  total_praiabaixo = sum(escolha_praiabaixo)       
  total_tarrafal = sum(escolha_tarrafal)        

  total = total_assomada + total_praiabaixo + total_tarrafal

  print(f"\nTotal Assomada: {total_assomada}$")
  print(f"Total Praia_Baixo: {total_praiabaixo}$")
  print(f"Total Tarrafal: {total_tarrafal}$")
  print(f"Total geral: {total}$")
 
resultados()
