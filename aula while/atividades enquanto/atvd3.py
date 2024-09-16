soma_positivos = 0
quantidade_negativos = 0
i = 0

while i < 10:
    valor = int(input(f"digite o {i+1}º valor inteiro: "))
    if valor > 0:
        soma_positivos+= valor
    elif valor < 0:
        quantidade_negativos += 1

print(f"soma dos números positivos: {soma_positivos}")
print(f"quantidade de valores negativos: {quantidade_negativos}")