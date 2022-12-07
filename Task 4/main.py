# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.


# defining a class
class Movie:
    def __init__(self, title, director, budget):  # defining class parameters
        self.title = title
        self.director = director  # assigning parameters to our attributes
        self.budget = budget

    # creating a method(function related to object)
    def wasExpensive(self):  # passing self parameter to this function makes it a method
        if self.budget > 100000000:
            print(f"{self.title} turi milziniska biudzeta of {self.budget}")
            return True
        else:
            print(f"{self.title} turi maziuka biudzeta of {self.budget}")
            return False


# creating 2 objects(Instances of the class Movie) with different arguments
filmas1 = Movie("Karibu piratai", "Antanas", 20000)
filmas2 = Movie("Titanikas", "Petras", 100000001)

# printing out name of the object followed by the parameter
print(filmas1.title)
print(filmas2.title)

# printing out name of the object fillowed by the name of the method
print(filmas1.wasExpensive())
print(filmas2.wasExpensive())
