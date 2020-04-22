import asyncio
import re


async def response(emails: list) -> str:
    def check_email(email: str) -> bool:
        """
        Validations
            1. It must have the username@websitename.extension format type.
            2. The username can only contain letters, digits, dashes and underscores.
            3. The website name can only have letters and digits.
            4. The maximum length of the extension is 3
        """
        _regex = r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
        return bool(re.match(_regex, email))

    print(sorted(list(filter(check_email, emails))))


if __name__ == "__main__":
    try:
        emails = []
        total_emails = int(input().strip())
        for _ in range(total_emails):
            emails.append(input().strip())
        asyncio.run(response(emails))
    except Exception as error:
        print(f"response() error -> {error}")
