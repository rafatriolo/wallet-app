# Usar a imagem oficial do Python como base
FROM python:3.10-slim

# Configurar o diretório de trabalho no contêiner
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de dependências (requirements.txt) para o contêiner
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto para dentro do contêiner
COPY . .

# Comando para rodar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
