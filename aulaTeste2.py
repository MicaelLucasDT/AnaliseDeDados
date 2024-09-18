import re;

texto = '''
cahcaça
cathaça
cabhaça
caxhaça
'''

padrao = re.compile(r'ca.haça')
check = padrao.findall(texto)
print(check)