def main():
    text = input("Input: ").strip()
    result = shorten(text)
    print(f"Output: {result}")

def shorten(text):
    vowels = ["a", "e", "i", "o", "u"]
    for v in text:
        if v.lower() in vowels:
            text = text.replace(v, "")
    return text

if __name__ == "__main__":
    main()
