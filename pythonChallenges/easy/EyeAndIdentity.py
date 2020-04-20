import numpy

if __name__ == "__main__":
    print(
        str(numpy.eye(*map(int, input().split()))).replace("1", " 1").replace("0", " 0")
    )

