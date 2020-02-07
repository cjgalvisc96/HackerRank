import cmath


def response(input):
    return cmath.polar(complex(input))


if __name__ == "__main__":
    print(*response(input().strip()), sep='\n')
