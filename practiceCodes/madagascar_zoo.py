from practiceCodes.parent_class import zoo_entry


class child_zoo(zoo_entry):
    def __init__(self):
        zoo_entry.__init__(self, 'goat', 'cow')

    def eating_habit_of_animals(self, food1, food2):
        print(self.animal1 + " eats "+food1)
        print(self.animal2 + " eats " +food2)

child_zoo_obj = child_zoo()
child_zoo_obj.eating_habit_of_animals('grass', 'hay')
