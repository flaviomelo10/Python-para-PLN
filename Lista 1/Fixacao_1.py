# -- encoding:utf-8 -- #

arquivo_dados = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Aula 3 - Exercício do final da aula qbdata.txt", 'r')
arquivo_novo = open("C:/Users/Flávio/Desktop/Workspace/Python para PLN/Lista 1/Fixacao_2.txt", 'w')
arquivo_novo.write("Rating de cada QB \n\n")
for inf in arquivo_dados:
	print(inf.split()[1] + " teve valor " + inf.split()[10])
	arquivo_novo.write(inf.split()[1] + " teve valor " + inf.split()[10] + '\n')
arquivo_dados.close()
arquivo_novo.close()

