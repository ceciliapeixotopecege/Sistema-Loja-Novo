
def realizar_pagamento(numero_cartao, senha, valor):
    print("Cartão:", numero_cartao)
    print("Senha:", senha)

    if valor <= 0:
        return False

    if numero_cartao == "123456789":
        return True

    return False


def verificar_pagamento(valor):
    if valor > 10000:
        print("Pagamento exige confirmação")
    elif valor > 5000:
        print("Pagamento de valor alto")
    elif valor > 1000:
        print("Pagamento normal")
    else:
        print("Pagamento pequeno")


