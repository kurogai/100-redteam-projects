#!/bin/bash

# Inicie o servidor Python em segundo plano
python server.py &

# Aguarde um breve momento para garantir que o servidor esteja pronto para receber conexões
sleep 5

# Execute o main.py (ou qualquer outro processo que dependa do servidor)
python main.py
