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
    if not ativosM:
        print("Nenhum ativo cadastrado no momento!")
    else:
        for ativo in ativosM:
            print(f"ID: {id_ativo} | Nome: {dados['nome']} | Tipo: {dados['tipo']}")
            
def loc_ativo():
    print("\n --- Buscando Ativo ---")
    if not ativosM:
        print("Nenhum arquivo cadastrado")
        return 
    search = input("Digite o ID do arquivo: ")
    if search.isdigit():
        id_search = int(busca)
        if id_search in ativosM:
            dados = ativosM[id_search]
        print(f"ID: {id_search} | Nome: {dados['nome']} | Responsável: {dados['responsavel']} | Setor: {dados['setor']}") | Tipo: {dados['tipo']}")
        return 

def att_ativo():
    print("\n --- Atualizando Ativo ---")
    if not ativosM:
        print("Nenhum ativo cadastrado no momento!")
        return

    try:
        id_ativo = int(input("Digite o ID do ativo que deseja atualizar: "))
    except ValueError:
        print("ID inválido, deve ser um número inteiro.")
        return

    if id_ativo not in ativosM:
        print("Ativo não encontrado.")
        return

    dados = ativosM[id_ativo]
    print(f"Atualizando ativo: {dados['nome']} (deixe em branco pra não alterar um campo)")

    novo_nome = input(f"Novo nome [{dados['nome']}]: ").strip()
    novo_responsavel = input(f"Novo responsável [{dados['responsavel']}]: ").strip()
    novo_setor = input(f"Novo setor [{dados['setor']}]: ").strip()

    if novo_nome:
        dados["nome"] = novo_nome
    if novo_responsavel:
        dados["responsavel"] = novo_responsavel
    if novo_setor:
        dados["setor"] = novo_setor

    print("Ativo atualizado com sucesso!")

def del_ativo():
    print("\n --- Excluindo Ativo ---")
    if not ativosM:
        print("Nenhum ativo cadastrado no momento!")
        return

    try:
        id_ativo = int(input("Digite o ID do ativo que deseja excluir: "))
    except ValueError:
        print("ID inválido, deve ser um número inteiro.")
        return

    if id_ativo not in ativosM:
        print("Ativo não encontrado.")
        return

    nome = ativosM[id_ativo]["nome"]
    del ativosM[id_ativo]
    print(f"Ativo {nome} (e suas vulnerabilidades) foi excluído com sucesso!")

def cadastro_vulnerabilidade():
    print("\n --- Cadastrando Vulnerabilidade ---")
    if not ativosM:
        print("Nenhum ativo cadastrado no momento!")
        return

    try:
        id_ativo = int(input("Digite o ID do ativo: "))
    except ValueError:
        print("ID inválido, deve ser um número inteiro.")
        return

    if id_ativo not in ativosM:
        print("Ativo não encontrado.")
        return

    descricao = input("Descrição da vulnerabilidade: ")
    categoria = input("Categoria (ex: senha fraca, falha de configuração): ")

    print("Selecione a severidade:")
    for s in severidade:
        print(f"{s.value}. {s.name}")

    print("Selecione o status:")
    for st in status_vulnerabilidade:
        print(f"{st.value}. {st.name}")

    try:
        sev_escolhida = int(input("Número da severidade: "))
        status_escolhido = int(input("Número do status: "))

        sev = severidade(sev_escolhida)
        status = status_vulnerabilidade(status_escolhido)

        ativosM[id_ativo]["vulnerabilidades"].append({
            "descricao": descricao,
            "categoria": categoria,
            "severidade": sev.name,
            "status": status.name
        })

        print("Vulnerabilidade cadastrada com sucesso!")
    except ValueError:
        print("Entrada inválida, tente novamente!")

def visualizar_vulnerabilidades():
    print("\n --- Vulnerabilidades do Ativo ---")
    if not ativosM:
        print("Nenhum ativo cadastrado no momento!")
        return

    try:
        id_ativo = int(input("Digite o ID do ativo: "))
    except ValueError:
        print("ID inválido, deve ser um número inteiro.")
        return

    if id_ativo not in ativosM:
        print("Ativo não encontrado.")
        return

    vulns = ativosM[id_ativo]["vulnerabilidades"]

    if not vulns:
        print("Este ativo está sem vulnerabilidades registradas.")
    else:
        for i, v in enumerate(vulns, start=1):
            print(f"{i}. {v['descricao']} | Categoria: {v['categoria']} "
                  f"| Severidade: {v['severidade']} | Status: {v['status']}")



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