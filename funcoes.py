#atividade aula2
#calcular os impostos
#calcula o inss
sal_bruto=float(input("Digite o salario bruto: "))
num_dependentes = int(input("Digite o numero de dependentes: "))

def calcular_inss(salario_bruto):
    if salario_bruto <=1000.00:
        return 0.0
    if salario_bruto <=2000.00:
        return 0.1
    else:
        return salario_bruto * 0.2

#calcula o imposto de renda
def imposto_de_renda(salario_liquido):
    if salario_liquido <=1400.00:
        return 0.0
    elif salario_liquido <=2500.00:
        return salario_liquido * 0.12
    elif salario_liquido <=5000.00:
        return salario_liquido * 0.2
    else:
        return salario_liquido * 0.27

#calcula o desconto de dependentes
def desconto_dependentes(num_dependentes):
    dependentes= 100
    desconto_dependentes = num_dependentes* dependentes
    return desconto_dependentes

#calcula o salario liquido
def calc_salario_liquido(sal_bruto, num_dependentes):
    desconto_inss = calcular_inss(sal_bruto)
    salario_liquido = sal_bruto - desconto_inss - desconto_dependentes(num_dependentes)
    desconto_ir  = imposto_de_renda(salario_liquido)

    miseria_final = sal_bruto - desconto_inss - desconto_ir
    return miseria_final

print (calc_salario_liquido(sal_bruto, num_dependentes))
