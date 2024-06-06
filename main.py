import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_programa():
        print('''
              Happy Veggi''')

def exibir_opcoes():
        print('1. Cadastrar restaurantes.')
        print('2. Listar restaurantes.')
        print('3. Ativar restaurantes.')
        print('4. Sair\n')

def finalizar_app():
        os.system('cls')
        print('Finalizando o app.')

def voltar_ao_menu():
        input('Digite uma tecla para voltar ao menu principal')
        main()

def opcao_invalida():
        print('Opcao invalida"\n')
        voltar_ao_menu()

def cadastrar_novo_restaurante():
        os.system('cls')
        print('Cadastro de novos restaurantes.\n')
        nome_do_restaurate = input('Digite o nome do restaurante que deseja cadastar: ')
        restaurantes.append(nome_do_restaurate)
        print(f'O restaurate {nome_do_restaurate} foi cadastrado com sucesso.\n')
        voltar_ao_menu()

def listar_restaurantes():
        os.system('cls')
        print('Listar os restaurantes.\n')
        for restaurante in restaurantes:
                print(f'.{restaurante}')
        voltar_ao_menu()

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
def main():
        os.system('cls')
        exibir_nome_programa()
        exibir_opcoes()
        escolher_opcao_1()

if __name__ == '__main__':
        main()