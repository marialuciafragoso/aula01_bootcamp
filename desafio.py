nome = input("Digite seu nome: ")

salario = float(input("Digite seu salario: "))
porcentagem_do_bonus = float(input("porcentagem do bonus em %: "))
valor_do_bonus = 1000 + (salario) * (porcentagem_do_bonus) / 100 

print(f"O usuario {nome} possui bonus de {valor_do_bonus}")

salario_total = float(salario) + valor_do_bonus

print(f"O salario total do usuario {nome} é de {salario_total}")
