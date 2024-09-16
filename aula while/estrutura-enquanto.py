#1º forma de utilizar while - parecido com FOR
contador = 1 # inicializando a variável

while contador <= 5:
    print(contador)
    contador = contador + 1 # o mesmo que contador +=1

print("="*40)

#2º forma de utilizar while - loop condicional normal

valor = 0 #inicializando variável
while valor >=0:
    valor = int(input("informe um valor qualquer(digite um valor negativo para terminar): "))

    print(f"você digitou {valor}")

# 3º forma de utilizar while - como se fosse faça
while True:
    senha = input("informe a senha: ")
    if senha == "123":
        print("parabéns, senha correta")
        break #forma de encerrar o while
    else:
        print("senha incorreta, tente denovo")