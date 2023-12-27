# month-day-year order: 9/8/1636 or September 8, 1636 >> should be formatted in year-month-day (YYYY-MM-DD)
def main():
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    YY, MM, DD = format_user_input(months)
    print(f"{YY}-{MM:02}-{DD:02}")


def format_user_input(months):
    while True:
        try:
            user_input = input("Date: ").strip().lower()
            if "/" in user_input:
                mm, dd, yy = user_input.split("/")
            else:
                mm, dd, yy = user_input.split()
                dd, _ = dd.split(",")
                mm = months.index(mm.title()) + 1
            if int(mm) <=12 and int(dd) <= 31:
                return int(yy), int(mm), int(dd)
        except ValueError:
            pass

main()
