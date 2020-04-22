import asyncio


async def check_even_number(number: int) -> bool:
    if (number % 2 == 0):
        return True
    else:
        return False


async def response(words: list) -> str:
    score = 0
    vowels_frecuency = {
        "a": 0,
        "e": 0,
        "i": 0,
        "0": 0,
        "u": 0,
    }
    for word in words:
        for vowel, frequency in vowels_frecuency.items():
            vowels_frecuency[vowel] = word.count(vowel)
        if await check_even_number(sum(vowels_frecuency.values())):
            score += 2
        else:
            score += 1
    print(score)

if __name__ == "__main__":
    try:
        total_words = input().strip()
        words = list(map(str, input().strip().split()))
        asyncio.run(response(words))
    except Exception as error:
        print(f"response() error -> {error}")
