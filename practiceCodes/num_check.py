# num = [1,2,3,4,5,6,7,8]
# num_type = {}
#
# for i in num:
#     if i%2 ==0:
#         num_type[i] = 'even'
#     else:
#         num_type[i] = 'odd'
#
# print(num_type)
#
# name = 'Abhishek reads a book'
#
# for char in name:
#     print(char, end=' ')

# list1 = list(range(-10,99,3))
# print(list1)
#
# student = {'A': [50,60,70,80], 'B' : [60, 50, 80, 95], 'C' : [80,50, 45, 60]}
# perc = {}
# total_marks = []
#
# for keys in student.keys():
#     marks = sum(student[keys])
#     print(f'{keys}, {marks}')
#     perc[keys] = marks
#     print(perc)
#
# total_marks = perc.values()
# maximum_marks = max(list(total_marks))
#
# for i,v in perc.items():
#     if v == maximum_marks:
#         print(i, v  )


student_marks = {}

student_marks['Virat'] = [90,80,70]
student_marks['Rohit'] = [50,60,40]
student_marks['Ishan'] = [20,30,10]

print(student_marks)

for name, marks in student_marks.items():
    student_marks[name] = sum(student_marks[name])
    #print(student_marks)

print(student_marks)
marks = max(list(student_marks.values()))

for name, total_marks in student_marks.items():
    if total_marks == marks:
        print(f'{name}  {marks}' )


