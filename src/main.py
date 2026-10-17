"""
TaskTracker - Gerenciador de Tarefas via Linha de Comando (CLI)
Bootcamp II - Fase 2 (Entrega Intermediária)

Aplicação que permite cadastrar e visualizar tarefas.
Versão inicial: menu de navegação e loop principal.
"""

# Lista em memória que armazena todas as tarefas cadastradas.
# Cada tarefa é um dicionário com: titulo, descricao, prioridade,
# data_limite e status.
tarefas = []

STATUS_INICIAL = "Pendente"


# ---------------------------------------------------------------------------
# Funcionalidades do menu
# ---------------------------------------------------------------------------

def cadastrar_tarefa():
    """Coleta os dados e adiciona a tarefa na lista."""
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição: ").strip()
    prioridade = input("Prioridade (Alta / Média / Baixa): ").strip()
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
    print("\n--- TAREFAS CADASTRADAS ---")
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
