arquivo = open('C:/Users/Cassio/Desktop/ProjetoExtratorDadosAlunos/AgenteExtrator_DadosAlunos/rasbackup.txt','r')
for linha in arquivo:
        print('Ra do aluno: \n',linha,'Nome do aluno:  \n',linha,'E-mail: ',linha)

arquivo.close()
