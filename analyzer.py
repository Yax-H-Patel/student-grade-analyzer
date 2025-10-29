def read_students(filename):
    file = open(filename, 'r')
    data = []
    for line in file.readlines():
        data.append([line.split(',')[0], int(line.split(',')[1].strip())])
    file.close()
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

def main():
    while(True):
        print("1. Show all students")
        print("2. Show average mark")
        print("3. Show top student")
        print("4. Add new student")
        print("5. Save report to file")
        print("6. Exit")
        
        choice = int(input("Your Choice: "))
        
        students = read_students("students.txt")
        student_analysis = analyze_students(students)

        average = 0 # stores the average mark
        high = 0 # stores the highest mark
        low = 0 # stores the lowest mark
        highIdx = 0 # stores the index of the student with highest mark
        lowIdx = 0 # stores the index of the student with lowest mark
        for i in range(0, len(students)):
            average += students[i][1]
            if students[i][1] > students[highIdx][1]:
                highIdx = i
                high = students[i][1]
            if students[i][1] < students[lowIdx][1]:
                lowIdx = i
                low = students[i][1] 
        average /= len(read_students("students.txt"))

        print()
        if choice == 1:
            for student in student_analysis:
                print(student)
        elif choice == 2:
            print(f"Average mark = {average}")
        elif choice == 3:
            print(f"{students[highIdx][0]} is the topper with mark equal to {students[highIdx][1]}")
        elif choice == 4:
            text = input("Enter students name: ") + "," + input("Enter students mark: ") + '\n'
            with open("students.txt", 'a') as file:
                file.write(text)
        elif choice == 5:
            with open("report.txt", 'w') as file:
                file.write("Student Grade Report\n")
                file.write("--------------------\n")
                for student in student_analysis:
                    file.write(f"{student['name']:<12} : {student['mark']:>3} -> {student['grade']}\n")
                file.write(f"\nClass Average  : {average}\n")
                file.write(f"Highest Mark    : {high}\n")
                file.write(f"Lowest Mark     : {low}\n")
            print("The report has been saved in the file 'report.txt'.")
        else:
            break
        print()

if __name__ == "__main__":
    main()