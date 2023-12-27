def main():
    grocery = get_list()
    for item in grocery:
        print(f"{grocery.get(item)} {item.upper()}")


def get_list():
    shopping_list = {}
    while True:
        try:
            product = input().strip().lower()
        except EOFError:
            print()
            break
        if product not in shopping_list:
            shopping_list[product] = 1
        else:
            shopping_list[product] += 1
    return dict(sorted(shopping_list.items()))


main()
