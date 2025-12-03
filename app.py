from db import usuarios
from usuarios import cadastrar_usuario, login_usuario, mostrar_estatisticas


def menu_inicial():
    print("\n+-------------------------------------+")
    print("|  SISTEMA DE PROVAS                  |")
    print("+-------------------------------------+")
    print("| [1] Cadastrar usuário               |")
    print("| [2] Login                           |")
    print("| [3] Estatísticas                    |")
    print("| [4] Sair                            |")
    print("+-------------------------------------+")


while True:
    menu_inicial()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario(usuarios)

    elif opcao == "2":
        if usuarios:
            login_usuario(usuarios)
        else:
            print("Nenhum usuário cadastrado.\n")

    elif opcao == "3":
        mostrar_estatisticas(usuarios)

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.\n")
