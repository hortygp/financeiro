#atividade aula2
#calcular os impostos
#calcula o inss
sal_bruto=float(input("Digite o salario bruto"))
num_dependentes = int(input("Digite o numero de dependentes"))

def calcular_inss(salario_bruto):
    if salario_bruto <=1000:
        return 0.0
    if salario_bruto <=2000:
        return 0.1
    else:
        return salario_bruto * 0.2

#calcula o desconto de dependentes
def desconto_dependentes(num_dependentes):
    dependentes= 100
    desconto_dependentes = num_dependentes* dependentes
    return desconto_dependentes


#calcula o imposto de renda
def imposto_de_renda(salario_bruto):
    imposto_de_renda = salario_bruto*0.5
    return imposto_de_renda
