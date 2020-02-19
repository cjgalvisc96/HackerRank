import re


class ExtractPII:
    def __init__(self, text=""):
        self.text = text
        self.regexs = {
            "ssn_with_stripe": r"(^|[^\d])(?P<number>(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4})($|[^\d])",
            "ssn_without_stripe": r"(^|[^\d])(?P<number>(?!000|666)[0-8][0-9]{2}(?!00)[0-9]{2}(?!0000)[0-9]{4})($|[^\d])",
            "credit_cards": {
                "visa": r"(^|[^\d])(?P<number>4[0-9]{12}(?:[0-9]{3})?)($|[^\d])",
                "mastercard": r"(^|[^\d])(?P<number>(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12})($|[^\d])",
                "amex": r"(^|[^\d])(?P<number>3[47][0-9]{13})($|[^\d])",
                "dinners_club": r"(^|[^\d])(?P<number>3(?:0[0-5]|[68][0-9])[0-9]{11})($|[^\d])",
                "discover": r"(^|[^\d])(?P<number>6(?:011|5[0-9]{2})[0-9]{12})($|[^\d])",
                "jcb": r"(^|[^\d])(?P<number>(?:2131|1800|35\d{3})\d{11})($|[^\d])",
            },
            "playvox_subdomain": (
                r"(http://|HTTP://|https://|HTTPS://)?(www\.|WWW\.)?"
                r"(?P<playvox_subdomain>[-\w]+)"
                r"(\.\S+)?"
            ),
        }

    def extract_ssn(self, stripe=True):
        reponse = []
        if stripe:
            _regex = re.compile(self.regexs.get("ssn_with_stripe", ""))
        else:
            _regex = re.compile(self.regexs.get("ssn_without_stripe", ""))
        for match in _regex.finditer(self.text):
            reponse.append(
                (
                    match.group("number"),
                    f"{match.start('number')}:{match.end('number') - 1 }",
                )
            )
        return reponse

    def extract_credit_card_numbers(self):
        response = []
        for credit_card_name, credit_card_regex in self.regexs["credit_cards"].items():
            _regex = re.compile(credit_card_regex)
            dic_response = {}
            dic_response[credit_card_name] = []
            for match in _regex.finditer(self.text):
                dic_response[credit_card_name].append(
                    (
                        match.group("number"),
                        f"{match.start('number')}:{match.end('number') - 1 }",
                    )
                )
            response.append(dic_response)
        return response

    def extract_playvox_subdomain(self, text):
        return re.search(self.regexs.get("playvox_subdomain", ""), text.strip()).group(
            "playvox_subdomain"
        )
