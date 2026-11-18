area_sala=31
area_caixa=3
qtd_caixas=area_sala//area_caixa
resto=area_sala%area_caixa
if resto!=0:
    qtd_caixas+=1
print(f"A quantidade de caixas necessária sao {qtd_caixas} caixas.")