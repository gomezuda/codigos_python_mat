# 4º questão!
valor_inicial = int(input("Informe o valor inicial: "))
valor_final = int(input("Informe o valor final: "))

soma = 0 #inicialiazando uma variável
for contador in range(valor_inicial, valor_final+1):
    soma = soma + contador #faz com que a variável acumule esse valor


print(f"a soma do intervalo de {valor_inicial} até {valor_final} é {soma}")


