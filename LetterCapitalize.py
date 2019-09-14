def LetterCapitalize(string):
    string_to_list = string.split(' ')
    for i, word in enumerate(string_to_list):
        string_to_list[i] = word[:1].upper() + word[1:]
    return " ".join(string_to_list)

if __name__ == "__main__":
    test = "chris alan !"
    print(LetterCapitalize(test))
