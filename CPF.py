cpf = input("CPF(xxx.xxx.xxx-xx) :")


while (cpf[3] !=".") or (cpf[7] !=".") or (cpf[11] !="-"):
        cpf = input("O formato deve ser: (xxx.xxx.xxx-xx) :")
else:
        print("O formato está correto")