class Item():
    def __init__(self, share_button, price):
        self.share_button = share_button
        self.price = price

def sortByPrice(minPrice, itemArray):
    listArray = list()
    for x in itemArray:
        if x.price >= minPrice:
            listArray.append(x)
    return listArray

def getCats(array):
    someClicked = False
    depts = list()
    if (len(array) == 10):
        for x in range(1, 10):
            if array[x]:
                someClicked = True
                depts.append(getMaleCat(x-1))
    elif (len(array) == 14):
        for x in range(1, 14):
            if array[x]:
                someClicked = True
                depts.append(getFemaleCat(x-1))
    if someClicked:
        return depts
    else:
        return None

def getMaleCat(x):
    switcher = {
        0:"Accessories",
        1:"Jackets+%26+Coats",
        2:"Jeans",
        3:"Pants",
        4:"Shirts",
        5:"Shoes",
        6:"Shorts",
        7:"Sweaters",
        8:"Swim"
    }
    return switcher.get(x, "Index out of bounds")

def getFemaleCat(x):
    switcher = {
        0:"Accessories",
        1:"Bags",
        2:"Dresses",
        3:"Intimates+%26+Sleepwear",
        4:"Jackets+%26+Coats",
        5:"Jeans",
        6:"Pants",
        7:"Shoes",
        8:"Shorts",
        9:"Skirts",
        10:"Sweaters",
        11:"Swim",
        12:"Tops"
    }
    return switcher.ger(x, "Index out of bounds")