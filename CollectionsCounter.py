from collections import Counter

if __name__ == "__main__":
    total_shoes = int(input())
    shoes_sizes_list = Counter(map(int, input().split()))
    total_spends = 0
    stock = 0
    for i in range(int(input())):
        size, price = map(int, input().split())
        if (shoes_sizes_list[size]) and \
           (shoes_sizes_list[size] != 0):
            shoes_sizes_list[size] = shoes_sizes_list[size] - 1
            total_spends += price
    print(total_spends)

