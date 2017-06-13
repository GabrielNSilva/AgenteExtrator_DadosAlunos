arquivo = open('C:/Users/Cassio/Desktop/ProjetoExtratorDadosAlunos/AgenteExtrator_DadosAlunos/rasbackup.txt','r')

for linha in arquivo:
    print('\nlendo conteúdo!\n')
    valores = linha.split()
    print ('\nRA do Aluno: ',valores[0])
    
valores.append('\nNome do aluno será inserido aqui: ')
valores.append('\nE-mail do aluno será inserido aqui: ')

arquivo = open('C:/Users/Cassio/Desktop/ProjetoExtratorDadosAlunos/AgenteExtrator_DadosAlunos/rasbackup.txt','w')

arquivo.writelines(valores)
arquivo.close()

