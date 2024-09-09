altura = float(input("informe a sua altura em metros:"))
sexo = int(input("você é digite 1(homem) ou 2(mulher):"))

if sexo == 1:
    peso = (72.7 * altura) - 58
    print(f"peso ideal: {peso:.2f}kg")

elif sexo == 2:
    peso = (62.1 * altura) - 44.7
    print(f"peso ideal: {peso:.2f}kg")

else:
    print(f"Dado errado, digite novamente") 

