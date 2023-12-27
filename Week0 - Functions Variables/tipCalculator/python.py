#tip calculator
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#converting dollars to float
def dollars_to_float(d):
    d = float(d.removeprefix("$"))
    return round(d, 1)

#converting percents to float
def percent_to_float(p):
    p = float(p.removesuffix("%"))
    return p/100


main()