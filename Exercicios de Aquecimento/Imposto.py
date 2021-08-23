def somaImposto(Imposto, custo):
    return custo + (custo * Imposto / 100)


cost = float(input("Informe o valor do produto: R$ "))
tax = float(input("Informe a taxa de juros: "))

finalPrice = somaImposto(tax, cost)
print(f"O valor final do produto é de R${finalPrice:.2f}")