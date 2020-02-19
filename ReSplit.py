import re
if __name__ == "__main__":
    _regex = r'[,.]+'
    # print(*re.split(_regex, input()), sep='\n')
    print("\n".join(re.split(_regex, input())))