# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
    "make": "audi",
    "model": "A6",
    "year": 2005,
    "color": "white",
}

list = []


def showObjectKeys(object):
    for values in object.values():
        # print(values)
        # print(list)
        list.append(values)
    print(list)


showObjectKeys(audi)
