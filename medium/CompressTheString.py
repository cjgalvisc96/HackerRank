import asyncio
from itertools import groupby


async def response(_string: str) -> str:
    for k, g in groupby(_string):
        print(f"({len(list(g))}, {k})", end=" ")


if __name__ == "__main__":
    asyncio.run(response(input()))
