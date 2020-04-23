import re
import asyncio


async def response() -> str:
    for _ in range(int(input())):
        line = input()
        line = re.sub(r" \&\&(?= )", " and", line)
        line = re.sub(r" \|\|(?= )", ' or', line)
        print(line)


if __name__ == "__main__":
    try:
        asyncio.run(response())
    except Exception as error:
        print(f"response() error -> {error}")
