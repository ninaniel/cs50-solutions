def main():
    division = input("Fraction: ").strip()
    number = convert(division)
    print(gauge(number))

def convert(division):
    x, y  = division.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError

    return round(x/y * 100)

def gauge(n):
    if n >= 99:
        result = "F"
    elif n <= 1:
        result = "E"
    else:
        result = f"{int(n)}%"
    return result


if __name__ == "__main__":
    main()
