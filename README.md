# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastro e visualização de tarefas, desenvolvida na **Fase 2 (Entrega Intermediária)** do **Bootcamp II**.

**Autor:** Luiz Felipe Cunha · Curso de Desenvolvimento de Software

## Descrição funcional

O TaskTracker oferece um menu contínuo no terminal com três opções:

1. **Cadastrar nova tarefa** — registra título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas** — lista todas as tarefas com suas propriedades.
3. **Sair da aplicação** — encerra o programa.

### Estrutura de cada tarefa

| Campo        | Tipo   | Regra                                                                 |
|--------------|--------|-----------------------------------------------------------------------|
| Título       | String | Obrigatório. Entradas vazias ou só com espaços são rejeitadas.        |
| Descrição    | String | Texto livre.                                                          |
| Prioridade   | String | Aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`.                 |
| Data Limite  | String | Data planejada para conclusão (formato sugerido `DD/MM/AAAA`).        |
| Status       | String | Definido automaticamente como `Pendente` no cadastro.                 |

### Regras de negócio

- Se o título for inválido, o sistema exibe uma mensagem de erro e pede nova digitação até receber um valor válido.
- Se a prioridade estiver fora do padrão, o sistema exibe uma mensagem de erro e repete a pergunta.
- Se nenhuma tarefa tiver sido cadastrada, a listagem informa que não há registros no momento.

## Tecnologias utilizadas

- **Python 3** (sem bibliotecas externas)
- **Git** para versionamento
- **GitHub** para hospedagem do repositório

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                 # Documentação principal e instruções de uso
├── .gitignore                # Ignora arquivos temporários do Python e ambientes virtuais
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico e arquitetural da Fase 1
└── src/
    └── main.py               # Código-fonte principal do TaskTracker
```

## Instalação

1. Tenha o **Python 3** instalado (verifique com `python --version` ou `python3 --version`).
2. Clone o repositório:

```bash
git clone https://github.com/Luizlf07/tasktracker-projeto.git
cd tasktracker-projeto
```

Não há dependências externas para instalar.

## Execução

```bash
python src/main.py
```

> Em Linux/macOS, use `python3 src/main.py` se o comando `python` não estiver disponível.

### Exemplo de uso

```
==============================
        TASKTRACKER
==============================
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
Escolha uma opção: 1

--- CADASTRAR NOVA TAREFA ---
Título da tarefa:
[ERRO] O título é obrigatório e não pode ficar vazio. Tente novamente.

Título da tarefa: Estudar Git
Descrição: Revisar comandos de commit e push
Prioridade (Alta / Média / Baixa): urgente
[ERRO] Prioridade inválida. Digite apenas Alta, Média (ou Media) ou Baixa.

Prioridade (Alta / Média / Baixa): Alta
Data limite (DD/MM/AAAA): 20/10/2026

[OK] Tarefa "Estudar Git" cadastrada com sucesso! Status: Pendente.
```

## Próximos passos (Fase 3)

Empacotamento da aplicação, containerização com Docker, testes e deploy.
