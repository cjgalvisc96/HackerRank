def FirstFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * FirstFactorial(num - 1)


def FirstFactorialTeso(num):
    list_facts = [0] * (num + 1)
    list_facts[0] = 1
    for i in range(1, len(list_facts)):
        list_facts[i] = list_facts[i - 1] * i
    return list_facts[num]


if __name__ == "__main__":
    print(FirstFactorialTeso(8))