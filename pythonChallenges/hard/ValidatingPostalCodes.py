import asyncio
import re


async def response(number: str) -> str:
    regex_integer_in_range = r"^[1-9][\d]{5}$"
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
    print(
        bool(re.match(regex_integer_in_range, number))
        and len(
            re.findall(regex_alternating_repetitive_digit_pair, number)
            ) < 2
    )

if __name__ == "__main__":
    try:
        number = input().strip()
        asyncio.run(response(number))
    except Exception as error:
        print(f"response() error -> {error}")
