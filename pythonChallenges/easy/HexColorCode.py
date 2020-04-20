import re

if __name__ == "__main__":
    _regex = r"[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]"
    _string = ""
    for _ in range(int(input().strip())):
        _string += input()
    print("\n".join(re.findall(_regex, _string, re.I)))
