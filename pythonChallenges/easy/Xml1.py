from html.parser import HTMLParser

total = 0


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global total
        total += len(attrs)


if __name__ == "__main__":
    MyParser = MyHTMLParser()
    MyParser.feed("".join([input().strip() for _ in range(int(input()))]))
    print(total)

