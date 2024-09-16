while True:
        nome = input("Digite o nome completo: ")
        if len(nome) > 15:
# len - ter o tamanho/número de itens de um texto
            print("Nome aceito!")
            break #sair de um loop
        else:
            print("Nome muito curto. Tente novamente.")