# -- encoding:utf-8 -- #
"""
4. Crie uma lista com números de 0 a 9 (em qualquer ordem). Com ela, faça:
a. Adicione o número 6
b. Insira o número 7 na 3ª posição da lista
c. Remova o elemento 3 da lista
d. Adicione o número 4
e. Verifique o número de ocorrências do número 4 na lista
"""

lista = [0,2,5,4,6,8,9,3,1,5]
lista.append(6)
print(lista)
lista.insert(0,7)
print(lista)
lista.remove(3)
print(lista)
lista.append(4)
print(lista)
print(lista.count(4))

"""
5. Ainda com a lista criada na questão anterior, faça:
a. Retorne os primeiros 3 elementos da lista
b. Retorne os elementos que estão da 3ª posição até a 7ª posição da lista
c. Retorne os elementos da lista de 3 em 3 elementos
d. Retorne os 3 últimos elementos da lista
e. Retorne todos os elementos menos os 4 últimos da lista
"""

print(lista[0:3])
print(lista[2:8])
print(lista[::3])
print(lista[-3:])
print(lista[:-4])

#6. Com a lista das questões anteriores, retorne o 6º elemento da lista.
print(lista[5])

#7. Altere o valor do 7º elemento da lista para o valor 12.
lista[6] = 12
print(lista)

#8. Inverta a ordem dos elementos na lista.
print(lista[::-1])

#9. Ordene a lista.
lista_2 = lista.sort()
print(lista_2)
