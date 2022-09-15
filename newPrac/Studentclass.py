class student:
    def __init__(self, marks):
        print('Initialized')
        print(marks)

    def find_percentage(self):
        total_marks = sum(marks)
        percentage = total_marks/len(marks)
        return percentage

marks = [90, 80, 70]
marks2= [70,56,45]
obj1 = student(marks)
print(obj1.find_percentage())
obj2 = student(marks2)
