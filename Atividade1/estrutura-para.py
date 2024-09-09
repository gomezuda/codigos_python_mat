'''

Essa estrutura de repetição é o mais comum em qualquer outra linguagem de programação
for (contador = 1; contador <=5; contador++){

}
'''

#1° Exemplo
for contador in range(1,6):
    print(contador)

print("-"*30)
#2° Exemplo
for contador in range(1,11,2):
#aumentar o 3° parâmetro irá aumentar a forma de contagem dos valores que estão sendo exibidos
    print(contador)

print("-"*30)
#3° Exemplo - Número do maior pro menos
for contador in range(10,1,-1):
    print(contador,end=" ")