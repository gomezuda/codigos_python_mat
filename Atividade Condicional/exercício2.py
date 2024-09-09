salario = int(input("Informe o seu salário: R$"))

if salario < 600:
    aumento = salario * 0.30 
    novo_salario = salario + aumento 
    print(f"seu novo salario é R${salario:.2f}.")

else:
    print(f"Você não tem direito ao aumento.")
