FROM python:3

# Copie os arquivos Python para dentro do contêiner
COPY server.py /app/server.py
COPY main.py /app/main.py
COPY start.sh /app/start.sh

# Defina o diretório de trabalho como /app
WORKDIR /app

# Instale quaisquer dependências necessárias
RUN pip install psutil

# Dê permissão de execução ao script
RUN chmod +x start.sh

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["/app/start.sh"]
