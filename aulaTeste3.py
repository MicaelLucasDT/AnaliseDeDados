import re

# ^ -> Ele vai olhar para o início da string
# [^] -> Conciderará todos os caracteres exceto o indicado

texto = 'urubu'
padrao1 = re.compile(r'^u') #checa se o primeiro carater é u
padrao2 = re.compile(r'[^u]') #procura os caracteres diferentes de u

check1 = padrao1.findall(texto)
check2 = padrao2.findall(texto)

print(check1)
print(check2)