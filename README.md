# mvp-sprint1-back

Este repositório contém o código-fonte do back-end para o MVP da disciplina de Desenvolvimento Full Stack Básico.

---

## Descrição da API

No contexto de Asset Administration Shells blá blá blá.

---

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver a aplicação.
- **Flask**: Microframework para desenvolvimento web.
- **SQLAlchemy**: Biblioteca de ORM (Object-Relational Mapping) para trabalhar com bancos de dados.

---

## Como Executar

Para executar este projeto, será necessário ter todas as bibliotecas Python listadas no arquivo `requirements.txt` instaladas. Siga as etapas abaixo para configurar o ambiente e executar a aplicação.

### 1. Clonar o Repositório

Clone o repositório para o seu ambiente local.

```sh
$ git clone <url-do-repositorio>
$ cd mvp-sprint1-back
```

### 2. Criar e Ativar o Ambiente Virtual

É fortemente recomendado uso de ambientes virtuais, como virtualenv, para gerenciar as dependências do projeto.

```sh
$ python -m venv env
$ source env/bin/activate  # No Windows use `env\Scripts\activate`
```

### 3. Instalar as Dependências

Instale as dependências listadas no arquivo requirements.txt.

```sh
(env)$ pip install -r requirements.txt
```

### 4. Executar a API

Para iniciar a API, execute o comando abaixo:

```sh
(env)$ flask run --host 0.0.0.0 --port 5000
```

#### Modo de Desenvolvimento

Em modo de desenvolvimento, é recomendado utilizar o parâmetro --reload, que reiniciará automaticamente o servidor sempre que houver uma mudança no código fonte.

```sh
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
