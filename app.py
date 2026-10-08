
from usuario import login, cadastrar_usuario
from carrinho import finalizar_compra
from pagamento import realizar_pagamento


def executar():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if login(usuario, senha):

        carrinho = ["notebook", "mouse", "teclado"]

        total = finalizar_compra(carrinho, "ouro")

        numero_cartao = input("Número do cartão: ")
        senha_cartao = input("Senha do cartão: ")

        if realizar_pagamento(numero_cartao, senha_cartao, total):
            print("Pagamento realizado")
        else:
            print("Pagamento recusado")


executar()

