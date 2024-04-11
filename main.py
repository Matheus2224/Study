

salario = float( input("Informe o salário:") )

if salario <= 3000:
    print("Programador Junior")
elif salario > 3000 and salario <= 6000: 
    print("Programador Plenio")
elif salario > 6000 and salario <= 15000:
    print("Programador Senior")
else: 
    print("Gerente de Prjeto")
