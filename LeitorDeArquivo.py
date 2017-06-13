arq = open('C:/Users/Cassio/Desktop/ProjetoExtratorDadosAlunos/AgenteExtrator_DadosAlunos/testedeleituradearquivo.txt', 'a')
texto = []
texto.append('\nEstá será alista de alunos\n')
texto.append('--------------------------\n')
texto.append('Começando agora os textes com o PYTHON')
texto.append('Continuando com os teste de leitura/escrita/gravacao com PYTHON')

arq.writelines(texto)
arq.close()

