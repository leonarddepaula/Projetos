import multiprocessing
print(multiprocessing.cpu_count(), "núcleos") # conta a quantidade de núcleos disponpives no sistema

# processamento senquancial
import threading # módulo para a a contrução de threads
import urllib.request # módulo para a requição da url
import time # módulo para tratar o tempo 

# função criada para realização do dowload das imagens
def downloadImangens(imagepath, fileName):
    print("Realizando Dowload......", imagepath)
    urllib.request.urlretrieve(imagepath, fileName) # Realiza a requisição para pagina da Web

t0 = time.time() # armazena o tempo inicial da execução
for i in range (10):
    imageName = "imagens/image-" +str(i) +".jpg" # coloca o nome em cada uma das imagens baixadas
    downloadImangens("http://lorempixel.com.br/400/200/sports", imageName) # aplica o download da imagem 

t1 = time.time() # tempo final após a execução
totalTime = t1 - t0 # diferença de tempo entre o valor inicial de execução e o final
print("Tempo tiotal de execuções {}".format(totalTime))