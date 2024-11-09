import os  # biblioteca

# Saída de dados -> print()
print("""
    Ｈａｐｐｙ Ｖｅｇｇｉ
    """)  # """ para possibilitar pular linhas

print("1 - Cadastrar restaurante")
print("2 - Listar restaurantes")
print("3 - Ativar restaurante")
print("4 - Sair\n")  # \n para pular linha no final

#Entrada de dados -> input()
opcao_escolhida = int(input("Escolha uma opção: "))  # armazenando a entrada de dado dentro de uma variavel, int() tranforma para inteiro

def finalizar_app():  # def -> função
    os.system("cls")
    print("Finalizando o app\n")


if opcao_escolhida == 1:
    print("Cadastrar restaurante")
elif opcao_escolhida == 2:
    print("Listar restaurante")
elif opcao_escolhida == 3:
    print("Ativar restaurante")
else:
    finalizar_app()


