# -- encoding:utf-8 -- #
'''
Crie uma variável com a string “ instituto de ciências matemáticas e de computação” e faça:
a. Concatene (adicione) uma outra string chamada “usp”
b. Concatene (adicione) uma outra informação: 2021
c. Verifique o tamanho da nova string (com as informações adicionadas das questões a e b), com referência a caracteres e espaços
d. Transforme a string inteiramente em maiúsculo
e. Transforme a string inteiramente em minúsculo
f. Retire o espaço que está no início da string e imprima a string
g. Substitua todas as letras ‘a’ por ‘x’
h. Separe a string em palavras únicas
i. Verifique quantas palavras existem na string
j. Separe a string por meio da palavra “de”
k. Verifique agora quantas palavras/frases foram formadas quando houve a separação pela palavra “de”
l. Junte as palavras que foram separadas (pode usar a separação resultante da questão h ou j)
m. Junte as palavras que foram separadas, mas agora separadas por uma barra invertida, não por espaços (pode usar a separação resultante da questão h ou j)
'''
texto = " instituto de ciências matemáticas e de computação"

#a)
texto = texto + " usp"
print(texto)

#b)
texto = texto + " 2021"
print(texto)

#c)
tamanho = len(texto)
print(tamanho)

#d)
print(texto.upper())

#e)
print(texto.lower())

#f)
print(texto[1:])
print(texto.strip())

#g)
print(texto.replace('a', 'x'))

#h
separar = texto.split()
print(separar)

#i)
print(separar)

#j)
separar2 = texto.split('de')
print(separar2)

#k)
print(len(separar2))

#l)
juntar = " ".join(separar)
print(juntar)

#m)
juntar2 = "/".join(separar)
print(juntar2)
