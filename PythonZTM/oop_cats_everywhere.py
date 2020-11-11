class Pets():
    # animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def sing(self, sound):
        for animal in self.animals:
            print(animal.sing(sound))

class Cat():
    # is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

    def sing(self, sounds):
        return (f'{self.name} said {sounds}')


#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Cat("Simon", 2), Cat("Sally", 3), Cat("Amurg", 2)]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()

#5 Output all of the cats singing miau using the my_pets instance
my_pets.sing('miau')

#6 Output one cat singing miau
print(my_cats[1].sing('miau'))