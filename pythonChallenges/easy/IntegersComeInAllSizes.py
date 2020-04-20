def response(a, b, c, d):
    return f"{(a**b) + (c**d)}"

if __name__ == "__main__":
    a, b, c, d = (int(input().strip()) for _ in range(4))
    print(response(a, b, c, d))
