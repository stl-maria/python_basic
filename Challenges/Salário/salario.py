def calcular_imposto(salario):
    aliquota = 0.00
    if (salario>= 0 and salario <= 1100):
        aliquota= 0.05
    elif (salario >= 1100.01 and salario >= 2500):
        aliquota = 0.10
    else:
        aliquota = 0.15
    
    return aliquota * salario

valor_salario = float(input())
valor_beneficio = float(input())

valor_imposto = calcular_imposto(valor_salario)

saida = valor_salario - valor_imposto + valor_beneficio
print(f'{saida:.2f}') #arredondando o valor para apenas duas casas depois da virgula