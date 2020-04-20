if __name__ == "__main__":
    _, students_english, _, students_french = (set(input().split()) for _ in range(4))
    print(len(students_english & students_french))
