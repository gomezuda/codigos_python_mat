# 3º questão

valor = int(input("informe o valor e qualquer maior que zero: "))

for contador in range(1, valor+1):
    if valor % contador == 0:
        print(contador,end=" ")