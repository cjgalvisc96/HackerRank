import numpy as np

if __name__ == "__main__":
    N = int(input())
    _array_a = np.array([input().split() for _ in range(N)], int)
    _array_b = np.array([input().split() for _ in range(N)], int)
    print(np.matmul(_array_a, _array_b))
