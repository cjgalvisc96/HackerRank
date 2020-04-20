
if __name__ == "__main__":
    """
    n = int(input())
    s = set(map(int, input().split()))
    for _ in range(int(input())):
        operation_split = input().split(' ')
        if "pop" in operation_split[0]:
            s.pop()
        elif "remove" in operation_split[0]:
            s.remove(int(operation_split[1]))
        else:
            s.discard(int(operation_split[1]))
    print(sum(s))
    """
    n = int(input())
    s = set(map(int, input().split()))
    for _ in range(int(input())):
        operation_split = input().split(' ')+['']
        eval(f"s.{operation_split[0]}({operation_split[1]})")
    print(sum(s))
