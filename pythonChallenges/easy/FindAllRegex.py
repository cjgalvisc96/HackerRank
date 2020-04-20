import re
if __name__ == "__main__":
    """
    _string = input().strip()
    _regex = r"([^aeiouAEIOU])(?P<vowels>[aeiouAEIOU]{2,})([^aeiouAEIOU])"
    for match in re.finditer(_regex,_string):
        print(match.group("vowels"))
    """
    s = '[qwrtypsdfghjklzxcvbnm]'
    a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I) # re.I for ignore lower and uppercase
    print('\n'.join(a or ['-1']))