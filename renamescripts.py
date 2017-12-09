import os

pathdir = '/home/clayton/Documentos/input/scriptsall'

print(pathdir)

os.listdir(pathdir)

for nome in os.listdir(pathdir):
    pos = nome.find("_")
    print(nome)
    print(pos)
    if pos == 2:
        novo_nome = '0' + nome
        print(novo_nome)
    elif pos == 1:
        novo_nome = '00' + nome
        print(novo_nome)
    elif pos == 3:
        novo_nome = ''+nome
        print(novo_nome)
    os.rename(os.path.join(pathdir, nome), os.path.join(pathdir, novo_nome))





# def encontraArquivosEmPastaRecursivamente(pasta, extensao):
#     arquivosPy = []
#     caminhoAbsoluto = os.path.abspath(pasta)
#     # print(caminhoAbsoluto)
#     for pastaAtual, subPastas, arquivos in os.walk(caminhoAbsoluto):
#         arquivosPy.extend([os.path.join(pastaAtual,arquivo) for arquivo in arquivos if arquivo.endswith('.py')])
#     return arquivosPy
#
#
# arquivosPy2Run = encontraArquivosEmPastaRecursivamente(pathdir, '.py')
#
# print(len(arquivosPy2Run))
# print(arquivosPy2Run)
# arquivosPy2Run.sort()
# print(arquivosPy2Run)
#
# count = 0
#
# for script in (arquivosPy2Run):
#     count+=1
#     print(count, script)