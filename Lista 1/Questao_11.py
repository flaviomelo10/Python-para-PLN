# -- encoding:utf-8 -- #
"""
Crie um dicionário com 5 entradas e suas respectivas chaves e valores. Faça:
a. Imprima todas as chaves do dicionário
b. Imprima todos os valores do dicionário
c. Imprima todos os itens do dicionário
d. Imprima o 2º item do dicionário
e. Imprima o dicionário completo
f. Percorra o dicionário, imprimindo para cada entrada o modelo “(chave) tem como valor (valor)”
"""

dicionario = {'Ana': 10, 'Joana': 8, 'Manoel': 9, 'Tomás': 7.9, 'Úrsula': 8.5}
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
print(dicionario['Joana'])
print(dicionario)
for chave, valor in dicionario.items():
	print(chave, "tem nota", valor)
