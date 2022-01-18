import threading
import time
import random

class TicketSeller(threading.Thread):
    ticketsSold = 0

    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.sem = semaphore
        print("Venda De ingresssos Inicializada!")

    def run(self):
        global ticketsAvailable
        running = True
        while running:
            self.randomDelay()

            self.sem.acquire()
            if(ticketsAvailable <= 0):
                running = False
            else:
                self.ticketsSold = self.ticketsSold +1
                ticketsAvailable = ticketsAvailable - 1
                print("{} acabou de vender 1 ({} restantes)".format(self.getName(), ticketsAvailable))
            self.sem.release()
        print("Venda de ingressos {} Ingressos Vendidos no total {}".format(self.getName(), self.ticketsSold))

    def randomDelay(self):
        time.sleep(random.randint(0,4)/(4))

# definição do nosso semáforo
semaphore = threading.Semaphore()
ticketsAvailable = 200

# os nossos vendedores 
sellers  = []
for i in range(4):
    seller =  TicketSeller(semaphore)
    seller.start()
    sellers.append(sellers)

# joining all our sellers
for seller in sellers:
    seller.join()