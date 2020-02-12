
from itertools import permutations

def response(_string, n):
    return [print(*p,sep="") for p in list(permutations(sorted(_string), int(n)))]


if __name__ == "__main__":
    _string, n = input().strip().split()
    # print(*('a','b'), sep="")
    response(_string, n)
