if __name__ == "__main__":
    N, X = map(int, input().split())
    students = []
    for _ in range(X):
        students.append(map(float, input().split()))
    for subject in zip(*students):
        print(sum(subject) / len(subject))
