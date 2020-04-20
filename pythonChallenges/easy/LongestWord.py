import re


def count_word(sentence):
    list_words = re.findall(r'\w+', sentence)
    return max(list_words, key=len)

if __name__ == "__main__":
    s = "many   fancy word hello    hi"
    print(count_word(s))
