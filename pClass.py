class Item():
    def __init__(self, share_button, price):
        self.share_button = share_button
        self.price = price

def sortByPrice(minPrice, itemArray):
    print(minPrice)
    listArray = list()
    for x in itemArray:
        if x.price >= minPrice:
            listArray.append(x)
    return listArray