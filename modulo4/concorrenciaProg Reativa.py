from ast import Return
import multiprocessing
import random
import time
from threading import current_thread
import rx 
from rx.scheduler import ThreadPoolScheduler
from rx import operators as ops

def intense_calculation(value):
    # função sleep para "dormir" e simular uma tarefa de longa duração 
    time.sleep(random.randint(5,20)* 0.1)
    return value

# calcula a quantidade de CPUs, e cria ThreadPoolSchedule com o numero de threads
optimal_tread_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(optimal_tread_count)

# cria o processo 1
rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
    ops.map(lambda s: intense_calculation(s)), ops.subscribe_on(pool_scheduler)
).subscribe(
    on_next=lambda s:print("PROCESSO 1:{0} {1}".format(current_thread().name, s)),
    on_error=lambda e:print(e),
    on_completed=lambda:print("PROCESSO 1 Finalaizado!"),
)

# Cria o Processo 2
rx.range(1, 10).pipe(
    ops.map(lambda s: intense_calculation(s)), ops.subscribe_on(pool_scheduler)
).subscribe(
    on_next=lambda i: print("PROCESSO 2: {0} {1}".format(current_thread().name, i)),
    on_error=lambda e: print(e),
    on_completed=lambda: print("PROCESSO 2 FINALIZADO"), 
)

# cria o porcesso 3 com o loop infinito
rx.interval(1).pipe(
    ops.map(lambda i: i* 100),
    ops.observe_on(pool_scheduler),
    ops.map(lambda s: intense_calculation(s))
).subscribe(
    on_next=lambda i: print("PROCESSO 3: {0} {1}".format(current_thread().name, i)),
    on_error=lambda e: print(e),
)


input("Pressione alguma telca paara sair \n")