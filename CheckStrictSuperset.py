if __name__ == "__main__":
    set_base = set(input().split())
    print(all(set_base > set(input().split()) for _ in range(int(input()))))