import re


def LetterChangesTeso(string):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"
    changes = "bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWZ"
    mapping = {k: v for (k, v) in zip(string + letters, string + changes)}
    return "".join([mapping[c] for c in string])


def LetterChangesCris(string):
    result = ''
    for letter in string:
        if re.match(r"^[a-zA-Z]", letter):
            next_letter = chr(ord(letter) + 1)
            if next_letter in ['a', 'e', 'i', 'o', 'u']:
                result += next_letter.upper()
            else:
                result += next_letter
        else:
            result += letter
    return result

if __name__ == "__main__":
    test = "hello*3"
    print(LetterChangesTeso(test))
