"""
TaskTracker: Gerenciador de Tarefas via Linha de Comando (CLI)
Bootcamp II, Fase 2 (Entrega Intermediária)
Autor: Luiz Felipe Rocha | RA: 22604023

Aplicação que permite cadastrar e visualizar tarefas, aplicando as regras
de negócio definidas no planejamento lógico da Fase 1:
  * Título obrigatório (não pode ser vazio nem conter apenas espaços)
  * Prioridade restrita a "Alta", "Média" (ou "Media") e "Baixa"
  * Status definido automaticamente como "Pendente" no cadastro
"""

# Lista em memória que armazena todas as tarefas cadastradas.
# Cada tarefa é um dicionário com: titulo, descricao, prioridade,
# data_limite e status.
tarefas = []

# Prioridades aceitas. A chave é a entrada normalizada (minúsculas)
# e o valor é a forma padronizada que será gravada na tarefa.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

STATUS_INICIAL = "Pendente"


# ===========================================================================
# Funções de validação (regras de negócio)
# ===========================================================================

def ler_titulo():
    """Solicita o título até que seja informado um valor não vazio."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O título é obrigatório e não pode ficar vazio. Tente novamente.\n")


def ler_prioridade():
    """Solicita a prioridade até que seja informada uma opção válida."""
    while True:
        entrada = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Prioridade inválida. Digite apenas Alta, Média (ou Media) ou Baixa.\n")


# ===========================================================================
# Funcionalidades do menu
# ===========================================================================

def cadastrar_tarefa():
    """Coleta os dados, aplica as validações e adiciona a tarefa na lista."""
    print("\n=== CADASTRAR NOVA TAREFA ===")
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_INICIAL,
    }
    tarefas.append(tarefa)
    print(f'\n[OK] Tarefa "{titulo}" cadastrada com sucesso! Status: {STATUS_INICIAL}.')


def visualizar_tarefas():
    """Exibe todas as tarefas cadastradas ou avisa que a lista está vazia."""
    print("\n=== TAREFAS CADASTRADAS ===")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{numero}")
        print(f"  Título.......: {tarefa['titulo']}")
        print(f"  Descrição....: {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade...: {tarefa['prioridade']}")
        print(f"  Data limite..: {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status.......: {tarefa['status']}")
    print(f"\nTotal de tarefas: {len(tarefas)}")


def exibir_menu():
    """Mostra as opções disponíveis ao usuário."""
    print("\n==============================")
    print("        TASKTRACKER")
    print("==============================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    """Loop principal: mantém o menu ativo até o usuário escolher sair."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
