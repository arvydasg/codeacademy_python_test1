# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
    {"id": "1", "name": "John Smith", "age": 20},
    {"id": "2", "name": "Ann Smith", "age": 24},
    {"id": "3", "name": "Tom Jones", "age": 31},
    {"id": "4", "name": "Rose Peterson", "age": 17},
    {"id": "5", "name": "Alex John", "age": 25},
    {"id": "6", "name": "Ronald Jones", "age": 63},
    {"id": "7", "name": "Elton Smith", "age": 16},
    {"id": "8", "name": "Simon Peterson", "age": 30},
    {"id": "9", "name": "Daniel Cane", "age": 51},
]

# 1
def getUserAverageAge(x):
    total_age = sum(d["age"] for d in users)
    print(f"Total age of all users: {total_age}")
    average_age = round(total_age / len(users))
    print(f"Average age of all users: {average_age} ")
    print(type(average_age))


getUserAverageAge(users)


# 2
def getUsersNames(x):
    # for user in users:
    #     print(user)

    new_list = []
    for user in users:
        new_list.append(user["name"])

    print(sorted(new_list))

    # for item in sorted(users, key=lambda x: x["name"]):
    #     print(item)


getUsersNames(users)
