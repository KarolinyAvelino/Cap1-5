frase = input("digite um frase: ")
palavras= frase.split()
contem_a = filter(lambda p:p.find("a")>=0 , palavras)
#contem_a = filter(lambda p: "a" in p , palavras)
subst_o = [p.replace("a", "o") for p in contem_a]
print(subst_o)
