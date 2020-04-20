from collections import deque

if __name__ == "__main__":
    _deque = deque()
    for _ in range(int(input())):
        command = input().split()
        if len(command) == 2:
            eval(f"_deque.{command[0]}({command[1]})")
        else:
            eval(f"_deque.{command[0]}()")
    print(*_deque)
