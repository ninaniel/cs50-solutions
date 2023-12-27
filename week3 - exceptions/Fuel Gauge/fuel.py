def main():
    div = get_correct_input("Fraction: ")
    print(get_percentage(div))

def get_correct_input(prompt):
    while True:
        try:
            x, y  = input(prompt).strip().split("/")
            if int(x) <= int(y):
                return round(int(x)/int(y),2)
            else:
                continue
        except (ValueError, ZeroDivisionError):
            pass

def get_percentage(n):
    if n*100 >= 99:
        result = "F"
    elif n*100 <= 1:
        result = "E"
    else:
        result = f"{int(n*100)}%"
    return result


main()