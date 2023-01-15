<h1 align="center">Remote command execution</h1>

## :information_source:  technologies used

* python3
* flask
* flask_httpauth

## :information_source: Running the code

To run this code, follow these steps:

1. Install the project's dependencies using the `requirements.txt` file:

```bash
pip3 install -r requirements.txt
```

2. Run the main.py script:

```bash
python3 main.py
```

3. To run a command, you can add it as a parameter in the URL, along with a basic username and password authentication, here's an example curl:

```bash
curl -u admin:password -X GET -i http://localhost:5000/?command=ls -la
```

If the command runs successfully, you will see the command output in the browser. If an error occurs, you will see an error message.