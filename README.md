# Projeto tarefa teste
Este projeto é uma aplicação de gerenciamento de vendas desenvolvida usando Django, Django REST Framework e Python para fornecer uma API para produtos, vendas e informações de clientes.

## Estrutura do Projeto

O projeto é dividido em várias partes principais:

- **`sales`**: Aplicativo principal que contém os modelos e views para gerenciar produtos, vendas e clientes.
- **`sales/api`**: Módulo responsável pela definição dos serializers e views da API REST.
- **`sales/migrations`**: Diretório que contém as migrações do banco de dados.
- **`sales/static`**: Diretório para arquivos estáticos como CSS, JavaScript e imagens.
- **`sales/templates`**: Diretório para os templates HTML.
- **`sales/urls.py`**: Arquivo de configuração das URLs do aplicativo.
- **`sales/views.py`**: Arquivo com as views do aplicativo.
- **`manage.py`**: Script de gerenciamento do Django.

## Instalação e Configuração

1. Clone o repositório para o seu ambiente local:

   ```bash

   git clone https://github.com/seu-usuario/nome-do-repositorio.git

   ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/Mac
    venv\Scripts\activate  # No Windows


    ```
3. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações do banco de dados:

    ```bash
    python manage.py migrate --fake sales
    ```

5. Inicie o servidor de desenvolvimento:
 ```bash
    python manage.py runserver
 ```

6. Acesse a aplicação no navegador em http://127.0.0.1:8000/.

## Utilização da API

A API oferece endpoints para gerenciar produtos, vendas e clientes. Abaixo estão os endpoints disponíveis, junto com os métodos HTTP suportados e uma breve descrição de cada um:

### Produtos

- **Listar todos os produtos**
  - **Endpoint:** `/api/produtos/`
  - **Método:** `GET`
  - **Descrição:** Retorna uma lista de todos os produtos.

- **Criar um novo produto**
  - **Endpoint:** `/api/produtos/`
  - **Método:** `POST`
  - **Descrição:** Cria um novo produto com os dados fornecidos.

- **Obter detalhes de um produto**
  - **Endpoint:** `/api/produtos/<int:pk>/`
  - **Método:** `GET`
  - **Descrição:** Retorna os detalhes de um produto específico pelo ID.

- **Atualizar um produto**
  - **Endpoint:** `/api/produtos/<int:pk>/`
  - **Método:** `PUT`
  - **Descrição:** Atualiza os dados de um produto específico pelo ID.

- **Excluir um produto**
  - **Endpoint:** `/api/produtos/<int:pk>/`
  - **Método:** `DELETE`
  - **Descrição:** Exclui um produto específico pelo ID.

### Vendas Master

- **Listar todas as vendas**
  - **Endpoint:** `/api/vendas-master/`
  - **Método:** `GET`
  - **Descrição:** Retorna uma lista de todas as vendas.

- **Criar uma nova venda**
  - **Endpoint:** `/api/vendas-master/`
  - **Método:** `POST`
  - **Descrição:** Cria uma nova venda com os dados fornecidos.

- **Obter detalhes de uma venda**
  - **Endpoint:** `/api/vendas-master/<int:codigo>/`
  - **Método:** `GET`
  - **Descrição:** Retorna os detalhes de uma venda específica pelo código.

- **Atualizar uma venda**
  - **Endpoint:** `/api/vendas-master/<int:codigo>/`
  - **Método:** `PUT`
  - **Descrição:** Atualiza os dados de uma venda específica pelo código.

- **Excluir uma venda**
  - **Endpoint:** `/api/vendas-master/<int:codigo>/`
  - **Método:** `DELETE`
  - **Descrição:** Exclui uma venda específica pelo código.

### Vendas Detalhe

- **Listar todos os detalhes das vendas**
  - **Endpoint:** `/api/vendas-detalhe/`
  - **Método:** `GET`
  - **Descrição:** Retorna uma lista de todos os detalhes das vendas.

- **Criar um novo detalhe de venda**
  - **Endpoint:** `/api/vendas-detalhe/`
  - **Método:** `POST`
  - **Descrição:** Cria um novo detalhe de venda com os dados fornecidos.

- **Obter detalhes de um detalhe de venda**
  - **Endpoint:** `/api/vendas-detalhe/<int:codigo>/`
  - **Método:** `GET`
  - **Descrição:** Retorna os detalhes de um detalhe de venda específico pelo código.

- **Atualizar um detalhe de venda**
  - **Endpoint:** `/api/vendas-detalhe/<int:codigo>/`
  - **Método:** `PUT`
  - **Descrição:** Atualiza os dados de um detalhe de venda específico pelo código.

- **Excluir um detalhe de venda**
  - **Endpoint:** `/api/vendas-detalhe/<int:codigo>/`
  - **Método:** `DELETE`
  - **Descrição:** Exclui um detalhe de venda específico pelo código.

### Pessoas

- **Listar todas as pessoas**
  - **Endpoint:** `/api/pessoas/`
  - **Método:** `GET`
  - **Descrição:** Retorna uma lista de todas as pessoas cadastradas.

- **Criar uma nova pessoa**
  - **Endpoint:** `/api/pessoas/`
  - **Método:** `POST`
  - **Descrição:** Cria uma nova pessoa com os dados fornecidos.

- **Obter detalhes de uma pessoa**
  - **Endpoint:** `/api/pessoas/<int:pk>/`
  - **Método:** `GET`
  - **Descrição:** Retorna os detalhes de uma pessoa específica pelo ID.

- **Atualizar uma pessoa**
  - **Endpoint:** `/api/pessoas/<int:pk>/`
  - **Método:** `PUT`
  - **Descrição:** Atualiza os dados de uma pessoa específica pelo ID.

- **Excluir uma pessoa**
  - **Endpoint:** `/api/pessoas/<int:pk>/`
  - **Método:** `DELETE`
  - **Descrição:** Exclui uma pessoa específica pelo ID.

