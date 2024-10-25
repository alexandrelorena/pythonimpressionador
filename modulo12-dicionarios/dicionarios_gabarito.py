# Exercício 1
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

produto_procurado = input("Digite o produto:")
produto_procurado = produto_procurado.lower()
if produto_procurado in precos:
    preco = precos[produto_procurado]
    print(f"Produto: {produto_procurado}, Preço: R${preco}")
else:
    print("Produto não encontrado, tente novamente")

# Exercício 2
# Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
# Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
# Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado
produto_procurado = input("Digite o produto:")
produto_procurado = produto_procurado.lower()
if produto_procurado in precos:
    preco = precos[produto_procurado]
    print(f"Produto: {produto_procurado}, Preço: R${preco}")
else:
    opcao = input(f"Deseja Cadastrar {produto_procurado}? (S/N)")
    if opcao.lower() == "s":
        preco = float(input(f"Digite o preço do {produto_procurado} (apenas números)"))
        precos[produto_procurado] = preco
        print(precos)
    else:
        print("Produto não encontrado, tente novamente")



# Exercício 3
# Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos. 
# calcule o novo valor dos produtos com base nas seguintes regras:
# Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
# Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
# Preços acima de 2.000 vão ter reajuste de 20%
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
for produto in precos:
    preco_produto = precos[produto]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.1
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.2
    print(f"Produto {produto}, Novo Preço: R${novo_preco}")


# Exercício 4
# Edite o programa antigo para ter os 2 dicionários, o de preços originais e o de novos preços
# Em seguida calcule o valor total de reajuste em R$ que teve entre a lista de produtos original e a lista final
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
novos_precos = {}
for produto in precos:
    preco_produto = precos[produto]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.1
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.2
    print(f"Produto {produto}, Novo Preço: R${novo_preco}")
    novos_precos[produto] = novo_preco
total_antigo = sum(precos.values())
total_novo = sum(novos_precos.values())
reajuste = total_novo - total_antigo
print(f"O reajuste total foi de R${reajuste}")


# Exercício 5
# Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
# Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
# Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022
vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    percentual = valor_23 / valor_22 - 1
    print(f"Em {mes}, a variação percentual foi de: {percentual:.1%}")

total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())
crescimento = total_23 / total_22 - 1
print(f"Crescimento Real: {crescimento:.1%}")

# Exercício 6 - Desafio
# No final da reunião de apresentação dos números, seu chefe perguntou:
# E se nos meses de 2023 que a gente vendeu menos do que 2022 a gente tivesse pelo menos empatado com 2022 (ou seja, se nos meses de 2023 em que as vendas foram menores do que o mesmo mês em 2022, o valor de vendas tivesse sido igual a 2022)
# Qual teria sido o nosso crescimento de 2023 frente a 2022?


# existem várias formas de fazer, aqui resolvemos editar o dicionario de vendas_23 quando o valor dele era menor do que vendas_22, para depois de editado recalcularmos o crescimento
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    percentual = valor_23 / valor_22 - 1
    if percentual < 0:
        vendas_23[mes] = valor_22
    print(f"Em {mes}, a variação percentual foi de: {percentual:.1%}")

total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())
crescimento = total_23 / total_22 - 1
print(f"Crescimento simulado: {crescimento:.1%}")