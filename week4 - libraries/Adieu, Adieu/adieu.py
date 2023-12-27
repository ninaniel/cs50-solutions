import inflect

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            user_input = input("Name: ").strip()
            if user_input.isalpha():
                names.append(user_input.title())
        except EOFError:
            print()
            break

    print("Adieu, adieu, to", p.join(names))

main()
