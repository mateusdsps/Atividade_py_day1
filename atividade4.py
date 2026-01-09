
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3


preco_total = preco_unitario * quantidade

# Exibindo o relatório da compra
print("-" * 30)
print("DETALHES DA COMPRA")
print("-" * 30)
print(f"Produto: {nome_produto}")
print(f"Quantidade: {quantidade} unidades")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print("-" * 30)
print(f"VALOR TOTAL: R$ {preco_total:.2f}")
print("-" * 30)