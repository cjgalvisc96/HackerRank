def response(a, b, m):
    output_1 = pow(a, b)
    output_2 = pow(a, b, m)
    return f"{output_1}\n{output_2}"


if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())
    m = int(input().strip())
    print(response(a, b, m))
