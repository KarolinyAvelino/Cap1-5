velocidade_inicial=float(input("Digite o valor da velocidade inicial: "))
velocidade_final=float(input("Digite o valor da velocidade final: "))
tempo_transicao=float(input("Digite o valor da tempo de transição de uma para outra: "))
#V = Vo + a*t

aceleracao= (velocidade_final - velocidade_inicial) / tempo_transicao

print("O valor da aceleração é:",aceleracao)