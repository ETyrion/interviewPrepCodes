class zoo_entry:
    def __init__(self, animal1, animal2):
        self.animal1 = animal1
        self.animal2 = animal2
        print("This is the default constructor of parent class")
        print("Animals in the zoo are "+animal1 + " and "+animal2)

    def sound_of_animals(self, sound1, sound2):
        print("Sound of " +self.animal1 + "is " +sound1)
        print("Sound of "+self.animal2 + " is "+sound2)


delhi_zoo = zoo_entry('Horse', 'Cow')
delhi_zoo.sound_of_animals('neigh', 'moo')