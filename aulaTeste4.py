import re

#\d -> Qualquer caractere que SEJA algarismo de 0 a 9
#\D -> Qualquer caractere que NÃO SEJA algarismo de 0 a 9

texto = 'urubu2009'
padrao1 = re.compile(r'\d') #uso o r 'raw string' para evitar problemas com a contra barra
padrao2 = re.compile(r'[\D]')

check1 = padrao1.findall(texto)
check2 = padrao2.findall(texto)

print(check1)
print(check2)