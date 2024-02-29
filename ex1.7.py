nome = input("Digite o nome do produto:")
preco_custo= float(input("Digite o preço de custo do produto:"))
preco_venda = float(input("Digite o preço de venda do produto:"))
quantidade_estoque = int(input("Digite a quantidade no estoque do produto:"))

lucro = (preco_venda - preco_custo) * quantidade_estoque

print ("O lucro será:",lucro)