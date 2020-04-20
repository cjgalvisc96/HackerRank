def print_formatted(n):
    w = len(bin(n)[2:])
    for number in range(1, n + 1):
        print(f"{str(number).rjust(w,' ')} "
              f"{oct(number)[2:].rjust(w,' ')} "
              f"{hex(number).upper()[2:].rjust(w,' ')} "
              f"{bin(number)[2:].rjust(w,' ')}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)