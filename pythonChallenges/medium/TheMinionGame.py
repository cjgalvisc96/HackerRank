
import asyncio


async def response(_string: str) -> str:
    stuart_score = 0
    kevin_score = 0
    _string_len = len(_string)
    vowels = 'AEIOU'
    for i in range(_string_len):
        if _string[i] in vowels:
            kevin_score += _string_len - i
        else:
            stuart_score += _string_len - i
    if stuart_score > kevin_score:
        print('Stuart', stuart_score)
    elif stuart_score == kevin_score:
        print('Draw')
    else:
        print('Kevin', kevin_score)


if __name__ == "__main__":
    try:
        _string = input().strip()
        asyncio.run(response(_string))
    except Exception as error:
        print(f"response() error -> {error}")
