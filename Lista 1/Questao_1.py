# -- encoding:utf-8 -- #

#1. Crie três variáveis e atribua os valores a seguir: a=1, b=5.9 e c=‘teste’. A partir disso, retorne o tipo de cada uma das variáveis.

a = 1;
b = 5.9;
c = 'teste'

print(type(a))
print(type(b))
print(type(c))

#2. Troque o valor da variável a por ‘1’ e verifique se o tipo da variável mudou.

a = '1'
print(type(a))

#3. Faça a soma da variável b com a variável c. Interprete a saída, tanto em caso de execução correta quanto em caso de execução com erro.

#print(b + c) #dá erro
print(str(b) + c)
