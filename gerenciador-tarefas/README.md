# Gerenciador de Tarefas

Aplicação web simples para cadastrar e organizar tarefas. Desenvolvida em Python com Flask, HTML e SQLite.

## Funcionalidades

- Adicionar tarefas.
- Marcar tarefas como concluídas e reabri-las.
- Excluir tarefas.
- Salvar os dados localmente em um banco SQLite.

## Requisitos

- Python instalado.
- `pip`, incluído normalmente com o Python.

## Instalação e execução

No PowerShell, abra a pasta `gerenciador-tarefas` e execute:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Quando o servidor iniciar, acesse [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador.

O banco `tarefas.db` é criado automaticamente na pasta de execução quando a aplicação é iniciada pela primeira vez.

## Estrutura do projeto

```text
gerenciador-tarefas/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Tecnologias

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- SQLite, usando o módulo `sqlite3` da biblioteca padrão do Python
