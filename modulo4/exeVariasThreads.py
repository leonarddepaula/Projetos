# execução de download de imagens via multiplas threads
from ast import arg
import threading
import urllib.request
import time

def downloadImagens(imagePath, fileName):
    print("Realizando o Download...", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("dowlnload Finalizado")

def executeThread(i):
    imageName = "imagens_thread/image-" + str(i) + ".jpg" 
    downloadImagens("http://lorempixel.com.br/400/200/sports", imageName) 

t0 = time.time()

threads = [] #lista vazia que vai receber todas as threads criadas.

# Cria das 10 threads, cada uma delas será responsável por realizar oo download.
for i in range(10):
    thread =threading.Thread(target=executeThread, args=(i,))
    threads.append(thread)
    thread.start()

# garante que as execuções foram finalizadas.
for i in threads:
    i.join()

# calcula o tempo de execução 
t1 = time.time()
totalTime = t1 -t0
print("tempo total de execução {}".format(totalTime))