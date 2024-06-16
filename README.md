# mvp-sprint1-back

Este repositório contém o código-fonte do back-end para o MVP da disciplina de Desenvolvimento Full Stack Básico.

--- 

## Sumário

1. [Descrição da API](#descrição-da-api)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Como Executar](#como-executar)
---

## 1. Descrição da API

De acordo com a [OPC Foundation](https://reference.opcfoundation.org/I4AAS/v100/docs/4.1), o Asset Administration Shell (AAS) é a representação digital padronizada de um ativo na Indústria 4.0. Essa representação não apenas encapsula os dados físicos de um ativo, mas também integra sua lógica operacional e sua história evolutiva. Em um cenário onde a digitalização e a conectividade são essenciais, o AAS se torna crucial para a interoperabilidade entre sistemas, permitindo que diferentes componentes de uma fábrica inteligente se comuniquem de maneira eficiente e se adaptem às mudanças operacionais em tempo real.

O AAS não se limita apenas à descrição estática de um ativo. Ele é dinâmico, sendo continuamente atualizado por designers de sistemas, usuários de ativos, aplicações e processos ao longo do ciclo de vida do ativo. Isso não apenas melhora a eficiência operacional, mas também possibilita a implementação de estratégias avançadas de manutenção preditiva e otimização de recursos.

No contexto deste MVP, estamos simplificando o processo de criação de um AAS, focando nos aspectos fundamentais como identificação, tipo de ativo, informações globais, entre outros. Este é um primeiro passo para desenvolver capacidades mais robustas que envolvem submodelos detalhados e elementos de propriedade, essenciais para um gerenciamento detalhado e inteligente dos ativos na Indústria 4.0.

Com essa base inicial, nosso objetivo é expandir este projeto para incluir funcionalidades avançadas de modelagem de Asset Administration Shells, suportando uma variedade maior de tipos de ativos e permitindo integrações mais profundas com sistemas de produção e manutenção. Este trabalho não apenas facilitará a gestão de ativos complexos, mas também promoverá uma maior eficiência e adaptabilidade em ambientes industriais modernos.


---

## 2. Tecnologias Utilizadas

- `Python`: Linguagem de programação utilizada para desenvolver a aplicação.
- `Flask`: Microframework para desenvolvimento web.
- `SQLAlchemy`: Biblioteca de ORM (Object-Relational Mapping) para trabalhar com bancos de dados.

---

## 3. Como Executar

Para executar este projeto, será necessário ter todas as bibliotecas Python listadas no arquivo `requirements.txt` instaladas. Siga as etapas abaixo para configurar o ambiente e executar a aplicação.

### 3.1. Clonar o Repositório

Clone o repositório para o seu ambiente local.

```sh
$ git clone <url-do-repositorio>
$ cd mvp-sprint1-back
```

### 3.2. Criar e Ativar o Ambiente Virtual

É fortemente recomendado uso de ambientes virtuais, como virtualenv, para gerenciar as dependências do projeto.

```sh
$ python -m venv env
$ source env/bin/activate  # No Windows use `env\Scripts\activate`
```

### 3.3. Instalar as Dependências

Instale as dependências listadas no arquivo requirements.txt.

```sh
(env)$ pip install -r requirements.txt
```

### 3.4. Executar a API

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
