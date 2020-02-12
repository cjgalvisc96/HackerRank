from collections import OrderedDict


if __name__ == "__main__":
    items_ordered = OrderedDict()
    for _ in range(int(input())):
        item_name, item_price = input().rsplit(" ", 1)
        items_ordered[item_name] = items_ordered.get(item_name, 0) + int(item_price)
    for item, price in items_ordered.items():
        print(item, price)
