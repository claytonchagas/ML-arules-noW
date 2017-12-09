# from subprocess import call
# # call(["ls", "-l"])
# script = "teste2.py"
# call(["python3", script])

import os

from subprocess import call
from timeit import default_timer as timer

start = timer()

pathdir = '/home/clayton/Documentos/input/scriptsall'

print(pathdir)

os.listdir(pathdir)


def encontraArquivosEmPastaRecursivamente(pasta, extensao):
    arquivosPy = []
    caminhoAbsoluto = os.path.abspath(pasta)
    # print(caminhoAbsoluto)
    for pastaAtual, subPastas, arquivos in os.walk(caminhoAbsoluto):
        arquivosPy.extend([os.path.join(pastaAtual,arquivo) for arquivo in arquivos if arquivo.endswith('.py')])
    return arquivosPy


arquivosPy2Run = encontraArquivosEmPastaRecursivamente(pathdir, '.py')

print(len(arquivosPy2Run))
print(arquivosPy2Run)
arquivosPy2Run.sort()
print(arquivosPy2Run)
#
count = 0

for script in arquivosPy2Run:
    count+=1
    print(count, script)
    call(["python3", script])
    # call(["now", "run", "-v", script])

end = timer()
print(end - start, "seg.")
