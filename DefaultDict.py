from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    d = defaultdict(list)
    for i in range(n):
        d[input()].append(i + 1)
    # {'a': [1, 2, 4], 'b': [3, 5]}
    # print(*[1, 2, 3]) -> 1 2 3
    for i in range(m):
        print(*d.get(input(), [-1]))
