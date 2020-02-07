def response(divisor, dividendo):
    division = divisor / dividendo
    modulo = divisor % dividendo
    _divmod = divmod(divisor, dividendo)
    return f"{int(division)}\n{modulo}\n{_divmod}"


if __name__ == "__main__":
    divisor = int(input().strip())
    dividendo = int(input().strip())
    print(response(divisor, dividendo))
