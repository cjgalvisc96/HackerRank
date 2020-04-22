import asyncio


async def response(_string: str) -> str:
    lowercase = []
    uppercase = []
    odd = []
    even = []
    for character in _string:
        if character.islower():
            lowercase.append(character)
        elif character.isupper():
            uppercase.append(character)
        elif character.isnumeric() and int(character) % 2 == 0:
            odd.append(character)
        else:
            even.append(character)
    print(
        f"{''.join(sorted(lowercase))}"
        f"{''.join(sorted(uppercase))}"
        f"{''.join(sorted(even))}"
        f"{''.join(sorted(odd))}"
    )

if __name__ == "__main__":
    try:
        _string = input().strip()
        asyncio.run(response(_string))
    except Exception as error:
        print(f"response() error -> {error}")
