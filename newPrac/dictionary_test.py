# student = {"Name":"Jason",
#            "Marks":90,
#            "Gender": 'Male'}
#
# student['Name'] = "Mark"
#
# print(student.keys())

song = {'artist': 'John Lennon', 'name': 'Imagine Dragons'}

song.update({'artist':'John Mayer'})

for k,v in song.items():
    print(f'keys : {k} , value : {v}')

print(song.items())