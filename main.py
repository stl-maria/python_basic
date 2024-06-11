import os

#array restaurantes
restaurantes = ['Pizza', 'Sushi']

#nome do app
def exibir_nome_programa():
        print('''
              Happy Veggi''')

#opções de ações no app
def exibir_opcoes():
        print('1. Cadastrar restaurantes.')
        print('2. Listar restaurantes.')
        print('3. Ativar restaurantes.')
        print('4. Sair\n')

#finalizar o app
def finalizar_app():
        exibir_subtitulo('Finalizando o app.') #refatorando o código

#voltando para o menu principal
def voltar_ao_menu():
        input('Digite uma tecla para voltar ao menu principal')
        main()

#quando a opção que o usuário ubmeteu for invalida
def opcao_invalida():
        print('Opcao invalida"\n')
        voltar_ao_menu()

#refatorando a ação limpar tela + nome da ação
def exibir_subtitulo(texto):
        os.system('cls')
        print(texto)
        print()

#cadastrar novo restaurante de array
def cadastrar_novo_restaurante():
        exibir_subtitulo('Cadastro de novos restaurantes.') #refatorando o código 
        nome_do_restaurate = input('Digite o nome do restaurante que deseja cadastar: ')
        restaurantes.append(nome_do_restaurate)
        print(f'O restaurate {nome_do_restaurate} foi cadastrado com sucesso.\n')

        voltar_ao_menu()

#mostrar a lista de restaurantes do array
def listar_restaurantes():
        exibir_subtitulo('Listar os restaurantes.') #refatorando o código 
        
        for restaurante in restaurantes:
                print(f'.{restaurante}')
        voltar_ao_menu()

#analisar melhor esta opção depois
"""def excluir_restaurante():
        for restaurante in restaurantes:
                print(f'.{restaurante}')

        nome_do_restaurante = input('\nQual restaurante deseja excluir?')
        restaurantes.remove(nome_do_restaurante)
        print('Restaurantes excluido')"""

#quando a opção desejada é selecionada
def escolher_opcao_1():
        try:
                opcao_escolhida = int(input('Escolha uma opção: '))
                if opcao_escolhida == 1:
                        cadastrar_novo_restaurante()
                elif opcao_escolhida == 2:
                        listar_restaurantes()
                elif opcao_escolhida == 3:
                        print('Ativas restaurantes.')
                elif opcao_escolhida == 4:
                        finalizar_app()
                else:
                        opcao_invalida()
        except:
                opcao_invalida()

#sequencia das funções a serem assionadas
def main():
        os.system('cls')
        exibir_nome_programa()
        exibir_opcoes()
        escolher_opcao_1()

#main
if __name__ == '__main__':
        main()