# Wallet App

Este é um sistema de gerenciamento de carteiras que permite realizar transferências entre usuários. O projeto é desenvolvido com **Django** e utiliza **PostgreSQL** como banco de dados.

## Requisitos

Certifique-se de ter os seguintes itens instalados:

- Python 3.9 ou superior
- Docker e Docker Compose
- Git

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




