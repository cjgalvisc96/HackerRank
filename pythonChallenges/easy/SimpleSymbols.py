import re

"""
def SimpleSymbols(string):
    count_regex_1 = len(re.findall(r'(?=([+][\w][+]))', string))
    count_regex_2 = len(re.findall(r'(?=([=][\w][=]))', string))
    count_simbol_1 = string.count("+")
    count_simbol_2 = string.count("=")

    if len(string) == 1 or len(string) == 2:
        return False

    for i in range(1, len(string) - 1):
        if (string[i] != '+') and (string[i] != '='):
            if ((string[i - 1] == '+') and (string[i + 1] == '+')) \
                or \
               ((string[i - 1] == '=') and (string[i + 1] == '=')):
                pass
            else:
                return False
    return True
"""


def SimpleSymbols(string):
    if (len(string) < 3) or (string[0].isalpha()) or (string[-1].isalpha()):
        return 'false'
    for i in range(1, len(string)-1):
        if string[i].isalpha():
            if string[i-1] != '+' or string[i+1] != '+':
                return 'false'
    return 'true'


if __name__ == "__main__":
    test = "g+="
    print(SimpleSymbols(test))
