def read_students(filename):
    file = open(filename, 'r')
    data = []
    for line in file.readlines():
        data.append([line.split(',')[0], int(line.split(',')[1].strip())])
    return data

def calculate_grade(mark):
    if mark > 90:
        return 'A'
    elif mark > 80:
        return 'B'
    elif mark > 70:
        return 'C'
    elif mark > 60:
        return 'D'
    else:
        return 'F'

def analyze_students(students):
    analysis = []
    for student in students:
        analysis.append({"name": student[0], "mark": student[1], "grade": calculate_grade(student[1])})
    return analysis