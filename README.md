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



