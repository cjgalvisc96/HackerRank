import asyncio
from collections import Counter


async def response(words: list) -> str:
    counts = Counter(words)
    print(len(counts))
    for word, frecuence in counts.items():
        print(frecuence, end=" ")


if __name__ == "__main__":
    try:
        words = []
        for _ in range(int(input().strip())):
            words.append(input().strip())
        asyncio.run(response(words))
    except Exception as error:
        print(f"response() error -> {error}")
