def fillable(stock, merch, n):
    if merch not in stock:
        return False
    if stock.get(merch, False) > n:
        return(True)
    else:
        return False
    
print(fillable({
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }, "leggos", 3))