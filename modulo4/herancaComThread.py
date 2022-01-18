from threading import Thread

# Define a Classe como filha da Classe Thread
class MinhaClasseThread(Thread):
    def __int__(self):
        print('Ola construtor thread!!')
        Thread.__init__(self)
    
    # Define a função run() que é chamada quando thread.start()
    def run(self):
        print("\n Thread em execução.")

# istanciamento de um objeto da classe criada
minhaThread = MinhaClasseThread()
print("Objeto Criado")
minhaThread.start()
print("Thread Inicializada")
minhaThread.join()
print("Thread finalizada")