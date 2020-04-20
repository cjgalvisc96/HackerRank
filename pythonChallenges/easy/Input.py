if __name__ == "__main__":
    x, y = map(int, input().split())
    result = eval(input().replace("x", str(x)))
    if result == y:
        print(True)
    else:
        print(False)
