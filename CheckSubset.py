if __name__ == "__main__":
    for _ in range(int(input())):
        _, set_A = input(), set(input().split())
        _, set_B = input(), set(input().split())
        print(set_A.issubset(set_B))