numero1= int(input("Digite o primeiro numero (a): "))
numero2= int(input("Digite o segundo numero (b): "))
numero3= int(input("Digite o terceiro numero (c): "))

delta= (numero2 ** 2)- 4 * numero1 * numero3

x1 = (-numero2 + delta ** (1/2)) / (2 * numero1)
x2 = (-numero2 - delta ** (1/2)) / (2 * numero1)

print("x1: {}, x2: {}".format(x1, x2))