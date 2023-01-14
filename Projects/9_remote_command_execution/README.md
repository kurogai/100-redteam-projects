<h1 align="center">Remote command execution</h1>

## :information_source:  technologies used

* python

## Executando o código

Para executar esse código, siga os seguintes passos:

1. Instale as dependências do projeto usando o arquivo `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

2. Execute o script main.py:

```bash
python3 main.py
```

3. Para executar um comando, você pode adicioná-lo como um parâmetro na URL, juntamente com uma autenticação basica de usuario e password, segue um curl de exemplo:

```bash
curl -u admin:password -X GET -i http://localhost:5000/?command=ls -la
```

Se o comando for executado com sucesso, você verá a saída do comando no navegador. Se ocorrer algum erro, você verá uma mensagem de erro.