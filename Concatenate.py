import numpy as np

if __name__ == "__main__":
    matrix_1 = []
    matrix_2 = []
    N, M, P = map(int, input().split())
    arrA = np.array([input().split() for _ in range(N)], int)
    arrB = np.array([input().split() for _ in range(M)], int)
    print(np.concatenate((arrA, arrB), axis=0))

