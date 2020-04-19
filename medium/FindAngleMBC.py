import math
import asyncio


async def get_angle(AB: int, BC: int) -> str:
    print(f"{int(round(math.degrees(math.atan2(AB,BC))))}°")


if __name__ == "__main__":
    try:
        AB = int(input())
        BC = int(input())
        asyncio.run(get_angle(AB, BC))
    except Exception as error:
        print(f"removeDuplicateCharacters() error -> {error}")
