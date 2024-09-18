import re;

# . -> entende qualquer valor exceto uma nova linha
# \. -> Busca o caractere "."

texto = 'O macaco é malaco'

padrao = re.compile(r'ma.aco')
check = padrao.findall(texto)

print(check)