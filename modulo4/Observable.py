# implementando observers
# rx.Observer implementa todas as principais funções necessárias para construção do observer (on_next, on_completed, on_error)
# on_next -> chama sempre que o "observer" recebe umnovo evento
# on_completed -> chama quando o "observable" notifica que finalizou a tarefa
# on_error -> Utilizada para capturar o error gerado
#import rx
from rx import create, disposable


# função que rece os observer
def push_five_strings(observer, scheduler):
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()
# Classe filha da classe Observer
class PrintObserver(disposable.Disposable):

    def on_next(self, value):
        print("recebido {0}".format(value))
    
    def on_completed(self):
        print("Fim!")

    def on_error(self, error):
        print("Erro Identificado: {0}".format(error))

# Cria o Observable
source = create(push_five_strings)
# Defeine o observer
source.subscribe(PrintObserver())