user1 = " " 
while user1 == " ":
    user1 = input("Usuário: ")
    senha1 = input("Senha: ")
    if senha1 == user1:
        input("Usuário e senha não podem ser iguais, insira uma nova senha: ")    
    else:
        print(f"Seja bem vindo {user1}")
        print("<3"*30)

user2 = " "
while user2 == " ":
    user2 = input("Usuário: ")
    senha2 = input("Senha: ")
    if senha2 == user2:
        input("Usuário e senha não podem ser iguais, insira uma nova senha: ")
    else:
        print(f"Seja bem vindo {user2}")
        print("<3"*30)
