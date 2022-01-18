# CONTANDO THREADS ATIVAS

from concurrent.futures import thread
import threading
import time
import random


def minhaThread(i):
    print("Thread {}: inicializada".format(i))
    time.sleep(random.randint(1,5))
    print("\nThread {}: finalizada".format(i))

for i in range(random.randint(2,50)):
    thread=threading.Thread(target=minhaThread,args=(i, ))
    thread.start()
time.sleep(4)
print("Total de Threads ativas: {}".format(threading.active_count()))