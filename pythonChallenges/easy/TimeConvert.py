def TimeConvert(num):
    return f"{int(num / 60)}:{num % 60}"


# keep this function call here 
print(TimeConvert(int(input())))
