def fillable(stock, merch, n):
    #print(stock.items(), merch)
    if merch not in stock:
        return False
    if stock.get(merch, False) > n:
        return(True)
    
print(fillable({
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }, "football", 3))