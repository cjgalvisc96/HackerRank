import re
if __name__ == "__main__":
    # ?= capture match with overlapped
    _string1 = input().strip()
    _string2 = input().strip()
    _regex = re.compile(f'(?={_string2})')
    if not re.search(_regex,_string1):
        print((-1, -1))
    else:
        for match in re.finditer(_regex, _string1):
            print((match.start(), match.end() +len(_string2)-1))

"""

aabcdeffgabcdef
abcdef
"""