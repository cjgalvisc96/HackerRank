if __name__ == "__main__":
    _, set_A = input(), set(map(int, input().split()))
    for _ in range((int(input()))):
        eval(f"set_A.{input().split()[0]}({set(map(int, input().split()))})")
    print(sum(set_A))

