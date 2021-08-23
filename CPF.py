from createdFunctions import cpfValidator


cpf = str(input("Digite seu CPF (XXX.XXX.XXX-XX): "))
valid = cpfValidator(cpf)

if valid:
    print(f"CPF {cpf} Valido!")
else:
    print(f"CPF {cpf} Invalido!")

