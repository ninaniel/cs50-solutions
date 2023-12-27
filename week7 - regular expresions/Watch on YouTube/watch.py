import re

# >>>>>>>>> https://youtu.be/xvFZjo5PgG0
def main():
    print(parse(input("HTML: ")))


#function checks if user_input matches the html iframe pattern, extracts the video ID from it & returns shortened link
def parse(s):
    pattern = r"<iframe.*></iframe>"
    if re.search(pattern,s):
        if match := re.search(r'https?://(?:www\.)?youtube\.com/embed/([^"]+)', s):
            return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()