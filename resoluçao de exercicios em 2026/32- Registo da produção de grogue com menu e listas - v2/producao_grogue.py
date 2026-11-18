print("REGISTO DA PRODUÇÃO DE GROGUE NA ILHA DE SANTIAGO E DE SANTO ANTÃO.")
print("O QUE DESEJA FAZER?")
print("1. INTRODUZIR  OS DADOS")
print("2. CONSULTAR UMA POSIÇÃO NA LISTA")
print("3. ALTERAR O VALOR DE UM ELEMENTO DA LISTA")
print("4. CONSULTAR O TOTAL DE PRODUÇÃO POR ILHA")
print("5. CONSULTAR A MÉDIA DA PRODUÇÃO POR ILHA")
print("6. JUNTAR AS DUAS LISTAS")
print("7. CONSULTAR QUAL FOI A ILHA QUE PRODUZIU MAIS")
print("8. SAIR")
escolha=0
lista_produtor_santiago=[]
lista_produtor_snt_antao=[]
while escolha <=0 or escolha>8:
    escolha=int(input("Escolha uma opção entre 1 e 8: "))
    if escolha==1:
        #1. INTRODUZIR  OS DADOS NO SISTEMA
        produtor_santiago=-1
        while produtor_santiago<0:
           produtor_santiago=int(input("Quantos produtores existem na ilha de Santiago? "))
        for i in range(produtor_santiago):
            litros1=-1
            while litros1<0:
                litros1=float(input(f"Quantos litros foram produzidos pelo produtor {i+1}?" ))
                lista_produtor_santiago.append(litros1)
        produtor_snt_antao=-1
        while produtor_snt_antao<0:
           produtor_snt_antao=int(input("Quantos produtores existem na ilha de Santo Antão? "))
        for i in range(produtor_snt_antao):
            litros2=-1
            while litros2<0:
                litro2=float(input(f"Quantos litros foram produzidos pelo produtor {i+1}?" ))
                lista_produtor_snt_antao.append(litros2)
    else:
        if escolha==2:
            #2. CONSULTAR UMA POSIÇÃO NA LISTA
            print("Deseja verificar a posição de que lista? ")
            print("1. Lista de produtores de grogue da ilha de Santiago;")
            print("2. Lista de produtores de grogue da ilha de Santo Antão;")
            escolha_lista=0
            while escolha_lista <=0 or escolha_lista>2:
                escolha_lista=int(input("Escolha a opção 1 ou 2: "))
                if escolha_lista==1:
                     indice = -1
                     while indice < 0 or indice >= len(lista_produtor_santiago):
                       indice = int(input(f"Que posição deseja verificar? (0 a {len(lista_produtor_santiago)-1}): "))
                     print(f"O produtor na posição {indice} produziu {lista_produtor_santiago[indice]} litros.")
                else:
                    if escolha_lista==2:
                         indice = -1
                         while indice < 0 or indice >= len(lista_produtor_snt_antao):
                           indice = int(input(f"Que posição deseja verificar? (0 a {len(lista_produtor_snt_antao)-1}): "))
                         print(f"O produtor na posição {indice} produziu {lista_produtor_snt_antao[indice]} litros.")
        else:
             if escolha==3:
                 #3. ALTERAR O VALOR DE UM ELEMENTO DA LISTA
                 print("Deseja modificar os valores de que lista?")
                 print("1. Lista de produtores de grogue da ilha de Santiago")
                 print("2. Lista de produtores de grogue da ilha de Santo Antão")
                 escolha_modif_lista=0
                 while escolha_modif_lista<=0 or escolha_modif_lista>2:
                     escolha_modif_lista=int(input("Escolha a opção 1 ou 2:"))
                 if escolha_modif_lista==1:
                     lista=lista_produtor_santiago
                 else:
                     lista=lista_produtor_snt_antao
                 print(lista)
                 indice=-1
                 while indice<0 or indice>=len(lista):
                     print(f"É possível modificar as posições entre 0 a {len(lista)-1}")
                     indice=int(input(f"Qual é a posição que deseja modificar?"))
                     novo_valor = -1
                 while novo_valor < 0:
                      novo_valor = float(input("Digite o novo valor de litros (>=0): "))
                 lista[indice] = novo_valor
                 print("Lista atualizada:", lista)
             else:
                 if escolha==4:
                     #4. CONSULTAR O TOTAL DE PRODUÇÃO POR ILHA
                     print("Deseja consultar o total de produção de que ilha?")
                     print("1. Ilha de Santiago")
                     print("2. Ilha de Santo Antão")
                     consultar_ttl_produção=0
                     while consultar_ttl_produção<=0 or consultar_ttl_produção>2:
                         consultar_ttl_produção=int(input("Escolha entre 1 e 2:"))
                     if consultar_ttl_produção == 1:
                        total = 0
                        for litros in lista_produtor_santiago:
                            total += litros 
                        print(f"O total de produção na Ilha de Santiago é {total} litros.")
                     else:
                        total = 0
                        for litros in lista_produtor_snt_antao:
                            total += litros  
                        print(f"O total de produção na Ilha de Santo Antão é {total} litros.")
                 else:
                     if escolha==5:
                        #5. CONSULTAR A MÉDIA DA PRODUÇÃO POR ILHA
                        print("Deseja consultar a média de produção de que ilha?")
                        print("1. Ilha de Santiago")
                        print("2. Ilha de Santo Antão")
                        escolha_media = 0
                        while escolha_media <= 0 or escolha_media > 2:
                            escolha_media = int(input("Escolha 1 ou 2: "))
                            if escolha_media == 1:
                             total = 0
                            for litros in lista_produtor_santiago:
                                total += litros
                            if len(lista_produtor_santiago) > 0:
                                media = total / len(lista_produtor_santiago)
                                print(f"A média de produção na Ilha de Santiago é {media:.2f} litros.")
                            else:
                                print("Não existem dados na lista de Santiago.")
                        else:
                            total = 0
                            for litros in lista_produtor_snt_antao:
                                total += litros
                            if len(lista_produtor_snt_antao) > 0:
                                media = total / len(lista_produtor_snt_antao)
                                print(f"A média de produção na Ilha de Santo Antão é {media:.2f} litros.")
                            else:
                                print("Não existem dados na lista de Santo Antão.")                        
                     else:
                         if escolha==6:
                             #6. JUNTAR AS DUAS LISTAS
                             if len(lista_produtor_santiago) == 0 and len(lista_produtor_snt_antao) == 0:
                                 print("Não existem dados nas listas para juntar.")
                             else:
                                lista_juntada = lista_produtor_santiago + lista_produtor_snt_antao
                                print("As duas listas foram juntadas com sucesso!")
                                print(f"Lista mesclada:{lista_juntada}" )
                         else:
                             if escolha==7:
                                 #7. CONSULTAR QUAL FOI A ILHA QUE PRODUZIU MAIS
                                   total_santiago = 0
                                   for litros in lista_produtor_santiago:
                                        total_santiago += litros
                                        total_snt_antao = 0
                                   for litros in lista_produtor_snt_antao:
                                        total_snt_antao += litros
                                        print(f"Total Santiago: {total_santiago} litros.")
                                        print(f"Total Santo Antão: {total_snt_antao} litros.")
                                        if total_santiago > total_snt_antao:
                                         print("A Ilha de Santiago produziu mais grogue.")
                                        else:
                                            if total_snt_antao > total_santiago:
                                             print("A Ilha de Santo Antão produziu mais grogue.")
                                            else:
                                             print("As duas ilhas produziram a mesma quantidade de grogue.")
                             else:
                                 if escolha==8:
                                     #8. SAIR
                                     print("Programa terminado. Obrigado pela sua visita, volte sempre!")
    break                 