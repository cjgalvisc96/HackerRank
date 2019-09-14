def count_substring(string, sub_string):
    len_string, len_substring = len(string), len(sub_string)
    if len_substring > len_string:
        return 0
    else:
        total = 0
        for index in range(0, len_string - (len_substring - 1)):
            if string[index:(index + len_substring)] == sub_string:
                total += 1
        return total

if __name__ == '__main__':
    string, sub_string = (input().strip() for _ in range(2))
    print(count_substring(string, sub_string))
