def main():
    camel = input("camelCase: ").strip()
    snake = convert_camel_to_snake(camel)
    print(f"snake_case: {snake}")

def convert_camel_to_snake(word):
    snake = "_"
    for letter in word:
        if letter.isupper():
            word = word.replace(letter, snake + letter.lower())
    return word

main()
