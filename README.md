# Expensify

Expensify é uma aplicação de gerenciamento de gastos desenvolvida utilizando o framework [Flet](https://flet.dev/). A aplicação permite que os usuários registrem, editem e visualizem suas despesas, ajudando-os a controlar melhor suas finanças pessoais.

## Funcionalidades

- **Cadastro de Usuário**: Permite que novos usuários se registrem fornecendo informações pessoais e de contato.
- **Login de Usuário**: Autenticação segura utilizando email, telefone ou nome de usuário.
- **Gerenciamento de Despesas**: Adicionar, editar e excluir despesas.
- **Visualização de Despesas**: Exibe uma lista de todas as despesas registradas, com informações detalhadas.
- **Persistência de Sessão**: Mantém o usuário autenticado mesmo após fechar a aplicação.

## Tecnologias Utilizadas

- [Flet](https://flet.dev/): Framework para desenvolvimento da interface do usuário.
- [SQLite](https://www.sqlite.org/index.html): Banco de dados relacional.
- [SQLAlchemy](https://www.sqlalchemy.org/): ORM para interagir com o banco de dados SQLite.
- [bcrypt](https://pypi.org/project/bcrypt/): Biblioteca para hashing de senhas.
- Python: Linguagem de programação principal.

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Passos para Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/expensify.git
    cd expensify
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```sh
    flet run
    ```

## Uso

### Cadastro de Usuário

1. Na tela de login, clique em "Cadastre-se".
2. Preencha os campos com suas informações pessoais e clique em "Registrar".

### Login de Usuário

1. Na tela de login, insira seu email, telefone ou nome de usuário e senha.
2. Clique em "Login".

### Gerenciamento de Despesas

1. Após o login, você será redirecionado para a tela principal onde pode ver todas as suas despesas.
2. Para adicionar uma nova despesa, clique em "Adicionar Despesa", preencha os campos necessários e salve.
3. Para editar ou excluir uma despesa existente, utilize os botões correspondentes ao lado da despesa.
