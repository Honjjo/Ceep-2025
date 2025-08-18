TAM_CNPJ = 18
cnpj = input("Por favor insira seu CNPJ (formato XX.XXX.XXX/XXXX-XX): ")
flag = True
if len(cnpj) != TAM_CNPJ:
    flag = False
elif (cnpj[2] != ".") or (cnpj[6] != ".") or (cnpj[10] != "/") or (cnpj[15] != "-"):
    flag = False
else:
    for i in range(TAM_CNPJ):
        if i not in [2, 6, 10, 15]:
            caractere = cnpj[i]
            if not caractere.isdigit():
                flag = False
                break
if flag:
    print("Formato de CNPJ Válido. ")
else:
    print("O CNPJ informado não tem um formato válido.")