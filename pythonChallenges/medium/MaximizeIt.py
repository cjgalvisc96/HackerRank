import asyncio
from itertools import product


async def response(_lists: list, M: int) -> int:
    results = map(lambda x: sum(i**2 for i in x) % M, product(*_lists))
    print(max(results))


if __name__ == "__main__":
    k, M = map(int, input().strip().split())
    _lists = (
        list(map(int, input().split()))[1:]
        for _ in range(k)
    )
    asyncio.run(response(_lists, M))
