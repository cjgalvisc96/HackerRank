import asyncio


async def response(athletes: list, _index: int) -> str:
    print("\n".join(
        map(lambda x: " ".join(map(str, x)),
        sorted(athletes, key=lambda x: x[_index])))
    )


def read_line():
    return map(int, input().strip().split())


if __name__ == "__main__":
    try:
        athletes = []
        total_athletes, total_attributes = read_line()
        for _ in range(total_athletes):
            athletes.append(list(read_line()))
        _index = int(input().strip())
        asyncio.run(response(athletes, _index))
    except Exception as error:
        print(f"response() error -> {error}")
