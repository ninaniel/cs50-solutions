# changing emoticon with emoji
def main():
    text = input("type ur text here: ")

    print(convert(text))

#function replacing emoticons
def convert(quote):
    return quote.replace(":)", "🙂").replace(":(","🙁")

main()
