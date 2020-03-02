from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if "\n" in comment:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(comment)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)


if __name__ == "__main__":
    MyParser = MyHTMLParser()
    MyParser.feed("".join([input().rstrip() + "\n" for _ in range(int(input()))]))

