if __name__ == '__main__':
    students = [[input(), float(input())] for _ in range(int(input()))]
    students_sorted = sorted(students, key=lambda x: x[1])
    print(students_sorted)
    last_grade = students_sorted[0][1]
    second_grade = last_grade
    for student in students_sorted:
        if student[1] != last_grade:
            second_grade = student[1]
            break
    names = [student[0] for student in students if student[1] == second_grade]
    print('\n'.join(sorted(names)))
