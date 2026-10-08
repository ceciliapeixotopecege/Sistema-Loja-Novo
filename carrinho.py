produtos = {
    "notebook": 3500,
    "mouse": 80,
    "teclado": 150,
    "monitor": 900
}


def calcular_total(carrinho):
    total = 0

    for produto in carrinho:
        if produto in produtos:
            total = total + produtos[produto]
        else:
            print("Produto não encontrado")

    return total


def aplicar_desconto(total, tipo_cliente):
    if tipo_cliente == "ouro":
        total = total * 0.80
    elif tipo_cliente == "prata":
        total = total * 0.90
    elif tipo_cliente == "bronze":
        total = total * 0.95
    else:
        total = total

    return total


def finalizar_compra(carrinho, tipo_cliente):
    total = calcular_total(carrinho)
    total = aplicar_desconto(total, tipo_cliente)

    if total > 0:
        print("Compra finalizada")
        print("Total:", total)
    else:
        print("Carrinho vazio")

    return total
 