while True:
        nome = input("Digite o nome completo: ")
        if len(nome) > 15:
# len - ter o tamanho/número de itens de algo
            print("Nome aceito!")
            break
        else:
            print("Nome muito curto. Tente novamente.")