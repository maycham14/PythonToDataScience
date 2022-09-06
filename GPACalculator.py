def gpa(no_of_subjects):
    sub_grade = {}
    for i in range(no_of_subjects):
        subject = input("name of the subject?\n")
        grade = (input("enter the grade of the subject.\n"))
        sub_grade[subject] = grade

    grade_gpa = []
    for key, value in sub_grade.items():
        value = int(value)
        if value >= 90:
            grade_gpa.append(4.3)
        elif value >= 80:
            grade_gpa.append(4.0)
        elif value >= 70:
            grade_gpa.append(3.7)
        elif value >= 67:
            grade_gpa.append(3.3)
        elif value >= 65:
            grade_gpa.append(3.0)
        elif value >= 60:
            grade_gpa.append(2.7)
        elif value >= 57:
            grade_gpa.append(2.5)
        elif value >= 55:
            grade_gpa.append(2.0)
        elif value >= 50:
            grade_gpa.append(1.5)
        elif value >= 39:
            grade_gpa.append(1.0)
        else:
            grade_gpa.append(0.0)

    index = 0
    sum_point = 0
    zero = 0
    for key, value in sub_grade.items():
        print(f"Subject: {key} Grade: {value} and point: {grade_gpa[index]}")
        sum_point = sum_point + grade_gpa[index]
        if grade_gpa[index] == 0.0:
            zero += 1

        index += 1
    print(f" Your GPA is {sum_point / (sub_grade.__len__() - zero)}")

gpa(1)
