import asyncio
import re


async def response(credit_cards: list) -> str:
    """
    Validations
        ► It must start with a 4,5 or 6.
        ► It must contain exactly 16 digits.
        ► It must only consist of digits (0-9 ).
        ► It may have digits in groups of 4, separated by one hyphen "-".
        ► It must NOT use any other separator like ' ' , '_', etc.
        ► It must NOT have 4 or more consecutive repeated digits.
    """
    _regex = r'^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$'
    _repeat_digits = r"([\d])\1\1\1"
    for credit_card in credit_cards:
        if (re.match(_regex, credit_card) and not
           re.search(_repeat_digits, credit_card.replace("-", ""))):
            print("Valid")
        else:
            print("Invalid")

if __name__ == "__main__":
    try:
        credit_cards = []
        total_credit_cards = int(input().strip())
        for _ in range(total_credit_cards):
            credit_cards.append(input().strip())
        asyncio.run(response(credit_cards))
    except Exception as error:
        print(f"response() error -> {error}")
