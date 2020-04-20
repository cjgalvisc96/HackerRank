import asyncio


async def merge_the_tools(string: str, k: int) -> str:
    async def removeDuplicateLetters(string: str) -> str:
        return ''.join(sorted(set(string), key=string.index))

    for i in range(0, len(string), k):
        print(await removeDuplicateLetters(string[i: i + k]))

if __name__ == "__main__":
    try:
        string, k = input(), int(input())
        asyncio.run(merge_the_tools(string, k))
    except Exception as error:
        print(f"removeDuplicateCharacters() error -> {error}")
