from collections import namedtuple

if __name__ == "__main__":
    """
    Cris->
    total_students = int(input().strip())
    student_tuple = namedtuple("Student", input().strip())
    sum_marks = 0
    for _ in range(total_students):
        student = student_tuple(*input().split())
        sum_marks += int(student.MARKS)
    print(f"{(sum_marks / total_students):.2f}")
    """
    n, categories = int(input()), input().split()
    Grade = namedtuple("Grade", categories)
    marks = [int(Grade(*input().split()).MARKS) for _ in range(n)]
    print(f"{(sum(marks) / len(marks)):.2f}")
