import json

ARQUIVO_DADOS = "ativos.txt"


def salvar_dados(ativos):
    """Grava o dicionário de ativos no arquivo de texto."""
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            json.dump(ativos, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar dados: {e}")


def carregar_dados():
    """Lê o arquivo de texto e devolve o dicionário de ativos carregado."""
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados_brutos = json.load(f)
            return {int(k): v for k, v in dados_brutos.items()}
    except FileNotFoundError:
        return {}
    except (json.JSONDecodeError, IOError) as e:
        print(f"Erro ao carregar dados salvos: {e}")
        return {}