def fibonacci(n):
    response = [0, 1, 1]
    if n == 0:
        return []
    elif n in [1, 2, 3]:
        return response[:n]
    else:
        for i in range(4, n + 1):
            response.append(response[i - 3] + response[i - 2])
    return response


if __name__ == "__main__":
    print(list(map(lambda x: x ** 3, fibonacci(int(input())))))

