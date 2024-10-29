# Usando uma imagem Python como base
FROM python:3.9-slim

# Configura o diretório de trabalho
WORKDIR /middleware-site

# Copia os arquivos para o container
COPY . /middleware-site

# Instala as dependências
RUN pip install -r requirements.txt

# Expõe a porta do servidor Flask
EXPOSE 5000

# Comando para rodar o servidor
CMD ["python", "middleware.py"]
