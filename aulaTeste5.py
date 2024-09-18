import re

#\s Conta os vazios
#\S Conta todos os outros caracteres

texto = '''

urubu 2019

'''

padrao1 = re.compile(r'\s')
padrao2 = re.compile(r'\S')

check1 = padrao1.findall(texto)
check2 = padrao2.findall(texto)

print (check1)
print (check2)