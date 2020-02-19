import re
if __name__ == "__main__":
    _regex = r"^[+|-]?[0-9]*\.[0-9]+$"
    for i in range(int(input())):
        print(bool(re.match(_regex, input())))
        
