import re

if __name__ == "__main__":
    _regex = r"^[789]\d{9}$"
    for _ in range(int(input().strip())):
        if re.match(_regex, input().strip()):
            print("YES")
        else:
            print("NO")
