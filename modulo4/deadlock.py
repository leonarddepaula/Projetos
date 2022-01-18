import threading
import time
import random 

class FIlosofos(threading.Thread):

    def __init__(self, name , leftFork, rightFork):
        print("{} sentou a mesa" .format(name))
        threading.Thread.__init__(self, name=name)
        self.lefFork = leftFork
        self.rightFork = rightFork

    def run(self):
        print("{} começõu a pensar".format(threading.currentThread().getName()))
        while True:
            time.sleep(random.randint(1,5))
            print("{} parou de pensar".format(threading.currentThread().getName()))
            self.lefFork.acquire()
            time.sleep(random.randint(1,5))
            try:
                print("{} pegou o garfo da esquerda.".format(threading.currentThread().getName()))

                self.rightFork.acquire()
                try:
                    print("{} pegou os dois garfos e começou a comer.".format(threading.currentThread().getName()))
                finally:
                    self.rightFork.release()
                    print("{} soltou o garfo da direita.".format(threading.currentThread().getName()))
            finally:
                self.lefFork.release()
                print("{} soltou o garfo da esquerda.".format(threading.currentThread().getName()))

fork1 = threading.RLock()
fork2 = threading.RLock()
fork3 = threading.RLock()
fork4 = threading.RLock()
fork5 = threading.RLock()

philosopher1 = FIlosofos("Kant", fork1, fork2)
philosopher2 = FIlosofos("Aristotle", fork2, fork3)
philosopher3 = FIlosofos("Spinoza", fork3, fork4)
philosopher4 = FIlosofos("Marx", fork4, fork5)
philosopher5 = FIlosofos("Russell", fork5, fork1)

philosopher1.start()
philosopher2.start()
philosopher3.start()
philosopher4.start()
philosopher5.start()

philosopher1.join()
philosopher2.join()
philosopher3.join()
philosopher4.join()
philosopher5.join()
