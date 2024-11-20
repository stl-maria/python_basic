import os  # biblioteca

restaurantes = [
    {'nome': 'Bistro do Chef', 'categoria': 'Francês', 'ativo': False},  # dicionarios dentro de uma lista
    {'nome': 'Sakura Sushi', 'categoria': 'Japonês', 'ativo': True},
    {'nome': 'Taco Loco', 'categoria': 'Mexicano', 'ativo': False}
]  # definindo uma lista dentro de uma variavel

def exibir_nome_do_programa():
    # Saída de dados -> print()
    print("""
        Ｈａｐｐｙ Ｖｅｇｇｉ
        """)  # """ para possibilitar pular linhas

def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Ativar restaurante')
    print('4 - Sair\n')  # \n para pular linha no final

def finalizar_app():  # def -> função (bloco de código)
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()  # chamando a função main

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')  # limpando a tela antes de começar
    print(texto,'\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do reastaurante que deseja cadastrar: ')  # informando o nome do restaurante
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')  # informando a categoria
    adicionando_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}  # juntando as informações
    restaurantes.append(adicionando_restaurante)  # utilizando o método append() para adicionar elemento na lista restaurantes
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes:  # para cada restaurante na lista restaurantes
        nome = restaurante['nome']  # obtendo apenas as chaves de nome 'nome'
        categoria = restaurante['categoria']  # obtendo apenas as chaves de nome 'categoria'
        ativo = restaurante['ativo']  # obtendo apenas as chaves de nome 'ativo'
        print(f'- {nome} | {categoria} | {ativo}')
    voltar_ao_menu_principal()



def escolher_opcao():
    try:  # "tente executar"
        #Entrada de dados -> input()
        opcao_escolhida = int(input('Escolha uma opção: '))  # armazenando a entrada de dado dentro de uma variavel, int() tranforma para inteiro

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:   # opção curinga
                opcao_invalida()
    except:  # "caso não consiga, faça..."
        opcao_invalida()

def main():
    os.system('cls')  # limpando a tela antes de começar
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
