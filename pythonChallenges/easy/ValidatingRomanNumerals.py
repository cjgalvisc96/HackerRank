import re

if __name__ == "__main__":
    _regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    _string = input().strip()
    print(bool(re.match(_regex, _string)))
