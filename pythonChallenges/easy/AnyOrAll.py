if __name__ == "__main__":
    N, numbers = input(), input().split()
    print(all([int(x) > 0 for x in numbers]) and any([x == x[::-1] for x in numbers]))
