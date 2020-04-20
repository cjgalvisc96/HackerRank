from itertools import combinations_with_replacement


def response(_string, n):
    return [
        print(*p, sep="")
        for p in list(combinations_with_replacement(sorted(_string), int(n)))
    ]


if __name__ == "__main__":
    _string, n = input().strip().split()
    # print(*('a','b'), sep="")
    # for i in range(int(n)):
    response(_string, n)
