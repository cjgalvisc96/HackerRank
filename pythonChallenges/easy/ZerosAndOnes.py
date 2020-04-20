import numpy

if __name__ == "__main__":
    nums = tuple(map(int, input().split()))
    print(numpy.zeros(nums, dtype=numpy.int))
    print(numpy.ones(nums, dtype=numpy.int))

