# -- encoding:utf-8 -- #
"""
Crie um arquivo e:
a. Escreva nele os números de 1 a 10
b. Depois de escrito, imprima na tela todos os números do arquivo
c. Escreva no arquivo os números de 11 a 20, substituindo os números que estavam antes no arquivo
d. Escreva no arquivo os números de 21 a 30, adicionando os números no final do arquivo (sem apagar o que já estavam lá)
e. Imprima na tela todos os números do arquivo novamente (de 11 a 30)
f. Imprima na tela todos os números do arquivo novamente, mas agora linha por linha
"""

arquivo_escrita = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Questao_12.txt", 'w')
arquivo_escrita.write("Números de 1 a 10 \n")
for i in range(1, 11):
    arquivo_escrita.write(str(i) + '\n')
arquivo_escrita.close()

arquivo_escrita = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Questao_12.txt", 'r')
print(arquivo_escrita.read())

arquivo_escrita = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Questao_12.txt", 'w')
arquivo_escrita.write("Números de 11 a 20 \n")
for i in range(11, 21):
    arquivo_escrita.write(str(i) + '\n')
arquivo_escrita.close()

arquivo_escrita = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Questao_12.txt", 'a')
arquivo_escrita.write("Números de 21 a 30 \n")
for i in range(21, 31):
    arquivo_escrita.write(str(i) + '\n')
arquivo_escrita.close()

arquivo_escrita = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Questao_12.txt", 'w')
arquivo_escrita.write("Números de 11 a 30 \n")
for i in range(11, 31):
    arquivo_escrita.write(str(i) + '\n')
arquivo_escrita.close()

arquivo_escrita = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Questao_12.txt", 'r')
print(arquivo_escrita.read())
arquivo_escrita.close()

arquivo_escrita = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Questao_12.txt", 'r')
print(arquivo_escrita.readlines())
arquivo_escrita.close()

arquivo_escrita = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Questao_12.txt", 'r')
for i in range(11, 31):
	print(arquivo_escrita.readline())
arquivo_escrita.close()	
