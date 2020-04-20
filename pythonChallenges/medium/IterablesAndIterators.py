import asyncio
from itertools import combinations


async def response(letters: str, indice: int) -> str:
    letter_combinations = list(combinations(letters, indice))
    match_combinations = [
        combination for combination
        in letter_combinations if 'a' in combination
    ]
    print(len(match_combinations)/len(letter_combinations))


if __name__ == "__main__":
    n, letters, indice = input(), input().split(), int(input())
    asyncio.run(response(letters, indice))
