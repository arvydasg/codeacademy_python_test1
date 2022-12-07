# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "filterDogOwers" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filterAdults" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
    {"id": "1", "name": "John Smith", "age": 20, "hasDog": True},
    {"id": "2", "name": "Ann Smith", "age": 24, "hasDog": False},
    {"id": "3", "name": "Tom Jones", "age": 31, "hasDog": True},
    {"id": "4", "name": "Rose Peterson", "age": 17, "hasDog": False},
    {"id": "5", "name": "Alex John", "age": 25, "hasDog": True},
    {"id": "6", "name": "Ronald Jones", "age": 63, "hasDog": True},
    {"id": "7", "name": "Elton Smith", "age": 16, "hasDog": True},
    {"id": "8", "name": "Simon Peterson", "age": 30, "hasDog": False},
    {"id": "9", "name": "Daniel Cane", "age": 51, "hasDog": True},
]

# --------------------------------------------------------------------
# SOLUTION
# --------------------------------------------------------------------
# tik darydamas tokias uzduotis suprantu kiek as is tikro nieko nesuprantu. :)
# daug ismokau beklaidziodamas ir atsakymu ieskodamas.

# 1
def filterDogOwners(x):
    ko_ieskau = [True]
    tik_turintys_suni = [d for d in users if d['hasDog'] in ko_ieskau]
    print(tik_turintys_suni)

filterDogOwners(users)


# 2
def filterAdults(x):
    ko_ieskau2 = 18
    tik_pilnameciai = [d for d in users if d['age'] > ko_ieskau2]
    print(tik_pilnameciai)

filterAdults(users)

# --------------------------------------------------------------------
# TWO HOURS OF FAILED ATTEMPTS BELOW
# --------------------------------------------------------------------

from operator import attrgetter,itemgetter

xampleSet = [
    {'type':'type1'},
    {'type':'type2'},
    {'type':'type2'},
    {'type':'type3'}
]
keyValList = ['type2','type3']
expectedResult = [d for d in exampleSet if d['type'] in keyValList]
print(expectedResult)

filtered = list(filter(lambda x: x['hasDog'] >= False, users))
print(filtered)

ages = [
    {'name': 'Evan', 'age': 25},
    {'name': 'John', 'age': 30},
    {'name': 'Jane', 'age': 27},
    {'name': 'Jack', 'age': 32},
]

filtered = list(filter(lambda x: x['age'] >= 30, ages))
print(filtered)


a_key = "hasDog"

list_of_values = [a_dict[a_key] for a_dict in users]
print(list_of_values)


#list of dictionaries
books = [
    {"title": "Pride and Prejudice ", "author": "Jane Austen"},
    {"title": "David Copperfield", "author": "Charles Dickens"},
    {"title": "Wuthering Heights", "author": "Emily Brontë"},
    {"title": "War and Peace ", "author": "Tolstoy"}
]

#define a key
a_key = "title"

list_of_values = [a_dict[a_key] for a_dict in books]

print(list_of_values)


print(users[0]['id'])


d = [{1: "a"}, {2: "b"}]
any(1 in x for x in d)


print(users)
print(sorted(users, key=itemgetter('id')))

movies = [{'name':'Avengers Endgame','date':'26/4/2019'},
          {'name':'Cron Man 3','date':'26/4/2013'},
          {'name':'Bvengers: Age of Ultron','date':'24/4/2020'}
]

print(sorted(movies, key=itemgetter('name')))


for dictionary in users():
    print(dictionary)

for dictionary in users:
    if some_key in dictionary.keys():
        print('Key Exists')
    else:
        print('Key does not exist')          


def filterDogOwers(masyvas):
    for key, value in user.items():
        if 

filterDogOwers(users)

ages = {'Matt': 30, 'Katie': 29, 'Nik': 31, 'Jack': 43, 'Alison': 32, 'Kevin': 38}
print(ages.get('Jack'))
print(ages.get('Jill'))


# create a nested dictionary with 3
# fields of 3 students
data = {
    'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
    'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
    'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
}


# iterate all the nested dictionaries with
# both keys and values
for i in data:
    # display
    print(data[i])


d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}

for i in d.keys():
    print(i)
    for j in d[i].keys():
        print(j)
