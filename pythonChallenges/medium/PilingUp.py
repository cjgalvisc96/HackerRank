import asyncio


async def response(side_cubes: list) -> str:
    if side_cubes:
        side_cubes_len = len(side_cubes)
        i = 0
        while i < side_cubes_len - 1 and side_cubes[i] >= side_cubes[i+1]:
            i += 1
        while i < side_cubes_len - 1 and side_cubes[i] <= side_cubes[i+1]:
            i += 1
        print("Yes" if i == side_cubes_len - 1 else "No")

if __name__ == "__main__":
    try:
        words = []
        for _ in range(int(input().strip())):
            n = input()
            asyncio.run(response(list(map(int, input().strip().split()))))
    except Exception as error:
        print(f"response() error -> {error}")
