def wrapper(sort_phone):
    def extract_phone(phones):
        return sort_phone([f"+91 {phone[-10:-5]} {phone[-5:]}" for phone in phones])

    return extract_phone


@wrapper
def sort_phone(phones):
    print(*sorted(phones), sep="\n")


if __name__ == "__main__":
    phones = [input() for _ in range(int(input()))]
    sort_phone(phones)

