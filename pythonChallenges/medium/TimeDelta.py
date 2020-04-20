import asyncio
from datetime import datetime as dt


async def response() -> str:
    format_date = '%a %d %b %Y %H:%M:%S %z'
    for _ in range(int(input())):
        print(int(abs((dt.strptime(input(), format_date) -
              dt.strptime(input(), format_date)).total_seconds())))

if __name__ == "__main__":
    try:
        asyncio.run(response())
    except Exception as error:
        print(f"response() error -> {error}")





