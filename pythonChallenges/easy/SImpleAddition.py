def SimpleAdding(num):
    # sum(range(1, num + 1))
    return int((num * (num + 1)) / 2)

if __name__ == "__main__":
    print(SimpleAdding(4))