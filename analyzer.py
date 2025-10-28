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