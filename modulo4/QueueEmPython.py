# COMUNICAÇÃO ENTRE THREADS
# código adaptado de http://www.learn4master.com/algorithms/python-queue-for-multthreadding
# put(), get(), join() e task_done().

import threading
import time
from queue import Queue

def consumidor(q):
    name = threading.currentThread().getName()
    print("Thread: {0} deseja um item da queue[tamanho atual = {1}] na data = {2} \n".format(name, q.qsize(), time.strftime('%H:%M:%S')))
    item = q.get()
    time.sleep(3) # demora 3 segundos para adicionar um item 
    print("Thread: {0} terminou de processar o item da queue[tamanho atual = {1}] na data = {2} \n".format(name, q.qsize(), time.strftime('%H:%M:%S')))
    q.task_done()

def produtor(q):
    # a thread principal vai adicionar itens para queue

    for i in range(10):
        name = threading.currentThread().getName()
        print("Thread: {0} começou a adicionar um item na queue[tamanho atual = {1}] na data = {2} \n".format(name, q.qsize(), time.strftime('%H:%M:%S')))
        item = "item-" + str(i)
        q.put(item)
        print("Thread: {0} adicionou um item de queue[tamanho atual = {1}] na data = {2} \n".format(name, q.qsize(), time.strftime('%H:%M:%S')))

    q.join()

if __name__ == '__main__':
    q = Queue(maxsize=3)

    threads_num = 3 # Crioação de 3 threads consumidoras
    for i in range(threads_num):
        t = threading.Thread(name= "ThreadConsumidora-" +str(i), target=consumidor, args=(q,))
        t.start()

        # criação de uma thread produtora
        t = threading.Thread(name="Threadprodutora", target=produtor, args=(q,))
        t.start()

        q.join()