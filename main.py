from enum import Enum
from persistencia import salvar_dados, carregar_dados
import random

# enumeração para os tipos de ativos
class tipo_ativo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    IMPRESSORA = 3
    BANCO_DE_DADOS = 4
    PCS = 5

# enumeração de risco de vulnerabilidade
class severidade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4

# enumeração para status de tratamento da vulnerabilidade
class status_vulnerabilidade(Enum):
    ABERTA = 1
    EM_TRATAMENTO = 2
    SOOOULVEEED = 3
    GRAVE_RISCO = 4


ativosM = carregar_dados()


## funções
def cadastro_ativo():
    print("\n --- Cadastrando Ativo ---")
    id_ativo = random.randint(1000, 9999)
    while id_ativo in ativosM:
        id_ativo = random.randint(1000, 9999)
    name = input("Nome/hostname do ativo: ").strip()
    while not name:
        name = input("O nome não pode ser vazio. Digite novamente:").strip

    responsavel = input("Responsável pelo ativo: ")
    setor = input("Setor/localização do ativo: ")

    print("Selecione o tipo do ativo\n")
    for t in tipo_ativo:
        print(f"{t.value}. {t.name}")

    try:
        escolhido = int(input("Escolha o número do tipo: "))
        tipo = tipo_ativo(escolhido)

        ativosM[id_ativo] = {
            "nome": name,
            "responsavel": responsavel,
            "setor": setor,
            "tipo": tipo.name,
            "vulnerabilidades": []
        }

        print(f"Sucesso! O ativo {name} foi cadastrado com ID {id_ativo}!")
        salvar_dados(ativosM)
    except ValueError:
        print("Entrada inválida, tente novamente!")


def lista_ativos():
    print("\n --- Listando Ativos ---")
    if not ativosM:
        print("Nenhum ativo cadastrado no momento!")
    else:
        for id_ativo, dados in ativosM.items():
            print(f"ID: {id_ativo} | Nome: {dados['nome']} | Responsável: {dados['responsavel']} "
                  f"| Setor: {dados['setor']} | Tipo: {dados['tipo']}")


def loc_ativo():
    print("\n --- Buscando Ativo ---")
    if not ativosM:
        print("Nenhum ativo cadastrado no momento!")
        return

    busca = input("Digite o ID ou o nome/hostname do ativo: ").strip()

    if busca.isdigit():
        id_busca = int(busca)
        if id_busca in ativosM:
            dados = ativosM[id_busca]
            print(f"ID: {id_busca} | Nome: {dados['nome']} | Responsável: {dados['responsavel']} "
                  f"| Setor: {dados['setor']} | Tipo: {dados['tipo']}")
            return

    encontrados = [
        (id_a, dados) for id_a, dados in ativosM.items()
        if dados["nome"].lower() == busca.lower()
    ]

    if encontrados:
        for id_a, dados in encontrados:
            print(f"ID: {id_a} | Nome: {dados['nome']} | Responsável: {dados['responsavel']} "
                  f"| Setor: {dados['setor']} | Tipo: {dados['tipo']}")
    else:
        print("Nenhum ativo encontrado com esse ID ou nome.")


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
    salvar_dados(ativosM)


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
    salvar_dados(ativosM)


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
        salvar_dados(ativosM)
    except ValueError:
        print("Entrada inválida, tente novamente!")


def visu_vulnerabilidade():
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
### construindo a função para printar o menu e pedir a opção do usuário para deixar o código mais limpo e legível
def menu():
    print("\n --- Menu de Gerenciamento de Ativos ---")
    print("1. Cadastrar Ativo")
    print("2. Listar Ativos")
    print("3. Buscar Ativo")
    print("4. Atualizar Ativo")
    print("5. Excluir Ativo")
    print("6. Cadastrar Vulnerabilidades")
    print("7. Visualizar Vulnerabilidades")
    print("0. Sair")

#Dispatch Table para boas práticas e aproveitamento de memória
opcoes = {
    "1": cadastro_ativo,
    "2": lista_ativos,
    "3": loc_ativo,
    "4": att_ativo,
    "5": del_ativo,
    "6": cadastro_vulnerabilidade,
    "7": visu_vulnerabilidade,
}

# Aqui eu chamo a função main, crio o loop com poucas condicionais e quebro ele se a pessoa escolher 0, criando esse feedback interativo
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do programa...")
            break

        user_input = opcoes.get(opcao)

        if user_input is None:
            print("Opção inválida. Tente novamente.")
        else:
            user_input()


if __name__ == "__main__":
    main()