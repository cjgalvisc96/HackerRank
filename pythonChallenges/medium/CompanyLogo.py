import asyncio
from collections import Counter


async def response(company_name: str) -> str:
    [print(*c) for c in Counter(sorted(company_name)).most_common(3)]

if __name__ == "__main__":
    try:
        company_name = input().strip()
        asyncio.run(response(company_name))
    except Exception as error:
        print(f"response() error -> {error}")
