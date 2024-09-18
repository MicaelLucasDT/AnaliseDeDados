import re

#\w -> Qualquer caractere que SEJA alfanumérico
#\W -> Qualquer caractere que NÃO SEJA alfanumérico

texto = '''

urubu!_@ 2019-*%

'''
padrao1 = re.compile(r'\w') #uso o r 'raw string' para evitar problemas com a contra barra
padrao2 = re.compile(r'[\W]')

check1 = padrao1.findall(texto)
check2 = padrao2.findall(texto)

print(check1)
print(check2)