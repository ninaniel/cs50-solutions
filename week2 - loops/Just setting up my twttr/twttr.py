def main():
    text = input("Input: ").strip()
    result = remove_vowels(text)
    print(f"Output: {result}")

def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    for v in text:
        if v.lower() in vowels:
            text = text.replace(v, "")
    return text

main()