from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    today = date.today()
    birth_date = get_date()
    print(minutes_from(birth_date, today))

#getting birth date in YYYY-MM-DD format, else - exiting
def get_date():
    try:
        birth = input("Date of Birth: ").strip()
        yy, mm, dd = map(int, birth.split("-"))
        return date(yy, mm, dd)

    except ValueError:
        sys.exit("Invalid date")

# taking as an input the date object and outputing total minutes(in words) passed from that date untill today
def minutes_from(birthday, today):
    days_between = (today - birthday).days   #instance attribute(read-only)
    minutes = days_between * 24 * 60
    words = p.number_to_words(minutes, andword="")

    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
