import numpy

if __name__ == "__main__":
    matrix = []
    N, M = map(int, input().split())
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    numpy_array = numpy.array(matrix)
    print(numpy.transpose(numpy_array))
    print(numpy_array.flatten())
