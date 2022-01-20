from rx import create

stocks = [
    {'TCKR': 'APPL', 'PRICE':  200},
    {'TCKR': 'GOOG', 'PRICE':  90},
    {'TCKR': 'TSLA', 'PRICE':  120},
    {'TCKR': 'MSFT', 'PRICE':  150},
    {'TCKR': 'INTL', 'PRICE':  70},
]

def buy_stock_events(observer, scheduler):
    for stock in stocks:
        if(stock['PRICE'] > 100):
            observer.on_next(stock['TCKR'])
    observer.on_completed()

source = create(buy_stock_events)

source.subscribe(on_next=lambda value: print("Instruçoes recebidas para acomprar {0}".format(value)),
                 on_completed=lambda: print("Instruções de compra finalizadas"),
                 on_error=lambda e: print(e))