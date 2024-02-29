numeros = list(range(31))
divisiveis= filter(lambda x: x%3==0 or x%5==0, numeros)
print(divisiveis)