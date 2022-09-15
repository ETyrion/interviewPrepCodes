class Student_data:
    objCount=0

    def __init__(self, name, marks):
        print("I am under constructor")
        self.name = name
        self.total_marks = marks
        Student_data.objCount+=1

    def __del__(self):
        print('Objects are deleted')

    def __str__(self):
        my_str = 'Name of the student is '+ str(self.name) + ' Marks are ' + str(self.total_marks)
        return my_str

    def avg_marks(self):
        percentage_obtained = sum(self.total_marks) / len(self.total_marks)

        return percentage_obtained


marks1 = [40,50, 60]
marks2 = [80, 60, 90]

obj1 = Student_data('Babar', marks1)
print(obj1.avg_marks())

obj2 = Student_data('Virat', marks2)
print(obj2.avg_marks())
print(Student_data.objCount)

print(obj1)
print(obj2)

print(obj1.__dict__)
