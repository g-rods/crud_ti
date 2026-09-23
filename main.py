from enum import Enum

#enumeração para os tipos de ativos
class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    IMPRESSORA = 3
    BANCO_DE_DADOS = 4
    PCs = 5

###    Protótipos de Funções que vou chamar lá no Main()
def cadastro_ativo():
    print("\n --- Cadastrando Ativo ---")
def lista_ativos():
    print("\n --- Listando Ativos ---")
def loc_ativo():
    print("\n --- Buscando Ativo ---")
def att_ativo():
    print("\n --- Atualizando Ativo ---")
def del_ativo():
    print("\n --- Excluindo Ativo ---")



ativosM = {}

#construindo a função para printar o menu e pedir a opção do usuário para deixar o código mais limpo e legível
def menu():
     print("\n --- Menu de Gerenciamento de Ativos ---")
     print("1. Cadastrar Ativo")
     print("2. Listar Ativos")
     print("3. Buscar Ativo")
     print("4. Atualizar Ativo")
     print("5. Excluir Ativo")
     print("0. Sair")

#definindo a função principal do programa, que vai chamar o menu e as funções de acordo com a opção escolhida pelo usuário
#respeitando good pratices de programação. usando o loop para criar um menu interativo que só vai sair quando o usuário escolher a opção de sair.
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_ativo()
        elif opcao == "2":
            lista_ativos()
        elif opcao == "3":
            loc_ativo()
        elif opcao == "4":
            att_ativo()
        elif opcao == "5":
            del_ativo()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()