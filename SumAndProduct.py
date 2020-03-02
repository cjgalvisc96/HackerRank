import numpy as np

if __name__ == "__main__":
    N, M = map(int, input().split())
    _array = np.array([input().split() for _ in range(N)], int)
    print(np.prod(np.sum(_array, axis=0)))
