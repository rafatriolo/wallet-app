# Wallet App

Este é um sistema de gerenciamento de carteiras que permite realizar transferências entre usuários. O projeto é desenvolvido com **Django** e utiliza **PostgreSQL** como banco de dados.

## Requisitos

Certifique-se de ter os seguintes itens instalados:

- Python 3.9 ou superior
- Docker e Docker Compose
- Git

## Técnicas Utilizadas

- Arquitetura MVC 
- Testes automatizados com Pytest
- Dockerfile e Docker Composer 
- Utilizei o Flake8 como Linter e o Black para Formatação de Código
- Utilizei o JWT Token para dar mais segurança nas requisições e fiz também um refresh token que expira tokens antigos.
- Foi feito em Python com Django e o Rest Framework do Django. (preferi o Python do que o C# pois é bem mais simples e se adequa melhor ao projeto)
- Utilizei o PostgreSQL pois ele é melhor no tratamento de objetos JSON do que o MYSQL ou o SQLite por exemplo.

## Instalação

 - Após clonar este repositório, copie o arquivo .env.example para um novo arquivo .env no mesmo nível do .env.example.
   O arquivo .env.example já está com as credenciais corretas.
 - Suba os containers com o Docker: docker-compose up --build
 - Crie um superuser no terminal: python manage.py createsuperuser (siga as instruções)
 - Acesse a aplicação no navegador: Django Admin: http://localhost:8000/admin e faça login com o usuário previamente criado.


## Endpoints 

### Criar um token com superuser criado no terminal

**URL**: `/api/token/`  
**Método**: `POST`  
**Descrição**: Cria um JWT Token

#### Exemplo de Requisição:

```json
POST /api/token/
Content-Type: application/json

{
    "username": "admin",
    "password": "1234"
}

```
#### Exemplo de Resposta
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNzc3MjgyOSwiaWF0IjoxNzM3Njg2NDI5LCJqdGkiOiJiYTE3NWVhOGU5ZTI0ZTc4OTVmMjQ5YWMxNDUxYTVkZSIsInVzZXJfaWQiOjF9.19d_uiGbKe6aKQvPUZkScMEqbZAXZOUVi4WyRROS4hY",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3Njg4MjI5LCJpYXQiOjE3Mzc2ODY0MjksImp0aSI6IjUwNWFhYjlhOGUwNjQ0YWFiMTEyMWRkM2UwNzM5NDU4IiwidXNlcl9pZCI6MX0.HFvnrN1Ew1AOBeHZFsNFXhDKpNWJyaYoheRdylRNBQc"
}

```

### Criar um usuário

**URL**: `/api/create-user/`  
**Método**: `POST`  
**Descrição**: Cria um Usuário no sistema e automaticamente já criada uma Wallet para esse usuário com saldo 0.00

#### Exemplo de Requisição:

```json
POST /api/create-user/
Content-Type: application/json

{
    "username": "outro_user3",
    "email": "outro_user3@example.com",
    "password": "1234"
}

```
#### Exemplo de Resposta
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "Usuário criado com sucesso!",
    "user": {
        "id": 3,
        "username": "outro_user3",
        "email": "outro_user3@example.com"
    }
}
```

### Adiciona Saldo a Carteira do Usuário

**URL**: `api/wallet/1/add-balance/`  
**Método**: `POST`  
**Descrição**: Adiciona saldo a wallet do usuário, substituir o número 1 pelo id do usuário

#### Exemplo de Requisição:

```json
POST api/wallet/1/add-balance/
Content-Type: application/json


{
    "amount": 500
}


```
#### Exemplo de Resposta
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "Saldo adicionado com sucesso!",
    "balance": "500.00"
}
```

### Realizar uma Transferência Entre Wallets 

**URL**: `api/transfer/`  
**Método**: `POST`  
**Descrição**: Realiza a transferência entre wallets de usuários retirando o valor de quem está mandando e adicionando valor a quem está recebendo

#### Exemplo de Requisição:

```json
POST api/transfer/
Content-Type: application/json

{
    "sender_user_id": 1,
    "receiver_user_id": 2,
    "amount": 1000
}



```
#### Exemplo de Resposta
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "Transferência realizada com sucesso!",
    "transfer": {
        "id": 22,
        "sender": "admin",
        "receiver": "outro_user3",
        "amount": "1000.00",
        "timestamp": "2025-01-24T10:54:25.826076Z"
    }
}
```

### Listar Transferência entre Usuários com filtro opcional por Data

**URL**: `api/user/2/transfers/`  
**Método**: `GET`
**QueryParams**: `start_date` & `end_date`
**Descrição**: Lista as transferências realizadas entre usuários com o filtro de data sendo passado como parâmetro na URL 

#### Exemplo de Requisição:

```json
GET api/user/2/transfers/?start_date=2025-01-01&end_date=2025-12-31
Content-Type: application/json

HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "id": 3,
        "amount": "5000.00",
        "timestamp": "2025-01-24T01:15:47.138167Z",
        "sender": {
            "id": 2,
            "username": "outro_user3",
            "email": "outro_user3@example.com"
        },
        "receiver": {
            "id": 1,
            "username": "admin",
            "email": "admin@example.com"
        }
    },
    {
        "id": 4,
        "amount": "5000.00",
        "timestamp": "2025-01-24T01:16:12.364160Z",
        "sender": {
            "id": 2,
            "username": "outro_user3",
            "email": "outro_user3@example.com"
        },
        "receiver": {
            "id": 1,
            "username": "admin",
            "email": "admin@example.com"
        }
    }
]


```




