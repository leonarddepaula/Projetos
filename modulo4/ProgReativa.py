# Hello World com programação Reativa
import rx
import rx.operators as ops

source = rx.from_iterable([1,2,3,4,5])
# source = rx.from_iterabble([1,2,'a,b,c',4,5])

disposable=source.pipe(
    ops.map(lambda i:i-1),
    ops.filter(lambda i:i%2==0),

).subscribe(
    on_next=lambda i: print("on_nexxt: {}".format(i)),
    on_completed=lambda: print("on_completed"),
    on_error=lambda e : print("on_error: {}".format(e))
)

disposable.dispose()

print("Fim")
