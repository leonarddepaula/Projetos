from concurrent.futures import thread
from sqlite3 import Time
import threading
import time
import random

# função que recebe um numero e cria uma thread
def executeThread(i):
    print("Thread {} inicializada \n". format(i))
    sleepTime = random.randint(1,10)
    time.sleep(sleepTime)
    print("Thread {} finalizoou a execução".format(i))

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i, ))
    thread.start()

    print("número de threads ativas: ", threading.enumerate())