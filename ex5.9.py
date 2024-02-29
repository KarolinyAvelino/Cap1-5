nomes = input("Digite uma lista de nomes separados por espaço: ").split()
maiusculo = list(map(lambda x: x.upper(), nomes))
print("Nomes em caixa alta:", maiusculo)
