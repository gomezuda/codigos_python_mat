horas_trabalhadas = float(input("digite a quantidade de horas trabalhadas aqui amore: "))
valor_hora = float(input("digite o valor por hora:R$: "))
salario = (horas_trabalhadas, valor_hora)

if horas_trabalhadas > 40:
    horas_normais = 40
    horas_extras = horas_trabalhadas - 40
    salario_base = horas_normais * valor_hora
    bonus_extra = horas_extras *valor_hora * 1.5

else:
    horas_normais = horas_trabalhadas
    horas_extras = 0
    salario_base = horas_normais * valor_hora
    bonus_extra = 0

salario_total = salario_base + bonus_extra

print(f"o salário total é:R${salario_total:.2f}")