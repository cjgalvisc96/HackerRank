"""
n, m = input().split()

_array = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in _array]))
"""
if __name__ == "__main__":
    print(1 in {1,2,3})