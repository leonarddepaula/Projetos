from multiprocessing.sharedctypes import Value
from rx import of, operators as op

of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
    op.map(lambda s: len(s)),
    op.filter(lambda i: i >= 5)
    ).subscribe(lambda value: print("recebido {0}".format(value)))

print('\n**********************************************************\n')

import rx

# criando uma sequencia de operações 
def lowercase():
    def _lowercase(source):
        def subscribe(observer, scheduler = None):
            def on_next(value):
                observer.on_next(value.lower())
            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler)
        return rx.create(subscribe)
    return _lowercase

rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
lowercase()
).subscribe(lambda value: print("Recebido {0}".format(value)))