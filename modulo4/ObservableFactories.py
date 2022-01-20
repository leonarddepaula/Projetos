# Observable factories
from rx import of

# cria o Observable
source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

source.subscribe(
    on_next= lambda i:  print("Recebido {0}".format(i)),
    on_error= lambda e: print("Erro identificado: {0}".format(e)),
    on_completed= lambda: print("Finalizado"),
)