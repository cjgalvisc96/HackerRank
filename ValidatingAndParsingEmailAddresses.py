import re

if __name__ == "__main__":
    _regex = r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>"
    for _ in range(int(input().strip())):
        username, email = input().split()
        if re.match(_regex, email):
            print(f"{username} {email}")
