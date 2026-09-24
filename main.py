from enum import Enum

#enumeração para os tipos de ativos
class tipo_ativo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    IMPRESSORA = 3
    BANCO_DE_DADOS = 4
    PCS = 5

###    Protótipos de Funções que vou chamar lá no Main()
def cadastro_ativo():
    print("\n --- Cadastrando Ativo ---")
    if ativosM:
        id_ativo = max(ativosM.keys()) + 1
    else:
        id_ativo = 1

    name = input("Selecione o nome do ativo que você queira cadastrar: ")

    print("Selecione o tipo do ativo\n")
    for _ in tipo_ativo:
        print(f"{_.value}. {_.name}")
    try:
        escolhido = int(input("Escolha o número do tipo:"))
        tipo = tipo_ativo(escolhido)

        ativosM[id_ativo] = {
            "nome": name,
            "tipo": tipo.name
        }

        print(f"Sucesso! o {name} foi cadastrado!")
    except ValueError:
        print("Entrada Inválida, tente novamente!")


    
def lista_ativos():
    print("\n --- Listando Ativos ---")
def loc_ativo():
    print("\n --- Buscando Ativo ---")
def att_ativo():
    print("\n --- Atualizando Ativo ---")
def del_ativo():
    print("\n --- Excluindo Ativo ---")



ativosM = {}

### construindo a função para printar o menu e pedir a opção do usuário para deixar o código mais limpo e legível
def menu():
     print("\n --- Menu de Gerenciamento de Ativos ---")
     print("1. Cadastrar Ativo")
     print("2. Listar Ativos")
     print("3. Buscar Ativo")
     print("4. Atualizar Ativo")
     print("5. Excluir Ativo")
     print("0. Sair")
#Dispatch Table para boas práticas e aproveitamento de memória
opcoes = {
    "1": cadastro_ativo,
    "2": lista_ativos,
    "3": loc_ativo,
    "4": att_ativo,
    "5": del_ativo,
}
# Aqui eu chamo a função main, crio o loop com apenas uma condicional e quebro ele se a pessoa escolher 0, criando esse feedback interativo
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do programa...")
            break
        #O get pega o input do usuário e analisa atráves da key do dict respectivo; também coloco uma condição para evitar que a pessoa escolha uma opção incorreta
        # e printando a string respectiva a key que o cara escolheu 
        user_input = opcoes.get(opcao)

        if user_input is None:
            print("Opção inválida. Tente novamente.")
        else:
            user_input()

if __name__ == "__main__":
    main()