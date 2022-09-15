import pickle

student = {"Rec1" : {"Name" : "A", "Salary": 2000},"Rec2": {"Name": "B", "Salary": 4000}}

with open('student.dat', 'wb') as stu:
    pickle.dump(student, stu)

with open('student.dat', 'rb') as sturd:
    dsr_data = pickle.load(sturd)

print(dsr_data)
