preco_mercadoria= float(input("Digite da mercadoria: "))
desconto= float(input("Digite valor do desconto: "))
imposto= float(input("Digite valor do imposto: "))

preco_final= (preco_mercadoria - desconto) + imposto

print("O preço final da mercadoria é:", preco_final)