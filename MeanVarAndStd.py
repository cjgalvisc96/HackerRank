import numpy as np

if __name__ == "__main__":
    N, M = map(int, input().split())
    _array = np.array([input().split() for _ in range(N)], int)
    np.set_printoptions(legacy="1.13")
    print(np.mean(_array, axis=1))
    print(np.var(_array, axis=0))
    print(np.std(_array, axis=None))
