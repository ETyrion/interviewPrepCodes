def avg_Score(student_marks, query):
    for name, marks in student_marks.items():
        if name == query:
            avg_marks = float(sum(marks)/len(marks))
            return avg_marks

if __name__ == '__main__':
    student_marks = {}
    student_marks['Josh'] = [90, 80, 70, 60]
    student_marks['Jaddu'] = [70, 60, 60, 80]
    student_marks['DJ'] = [90, 54, 80, 20]
    avg_marks = avg_Score(student_marks, 'DJ')
    print('%.2f'%avg_marks )
