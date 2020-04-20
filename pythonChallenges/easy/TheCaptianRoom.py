from collections import Counter
if __name__ == "__main__":
    K = int(input())
    rooms = Counter(map(int, input().split()))
    for key, value in rooms.items():
        if value != K:
            print(key)