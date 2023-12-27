import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # check input to match the pattern & extract groups (assigning minutes to zero if there's only hours presented)
    if pattern := re.match(r'(\d+):?(\d{2})?\s(AM|PM)\sto\s(\d+):?(\d{2})?\s(AM|PM)', s):

        hour1 = int(pattern.group(1))
        minutes1 = int(pattern.group(2) or 0)
        meridiem1 = pattern.group(3)
        hour2 = int(pattern.group(4))
        minutes2 = int(pattern.group(5) or 0)
        meridiem2 = pattern.group(6)

    # raising ValueError if input doesn't match the pattern
    else:
        raise ValueError("Invalid input format!")

    # raising ValueError for out-of-range times
    if not (0 <= hour1 <= 12 and 0 <= minutes1 < 60 and 0 <= hour2 <= 12 and 0 <= minutes2 < 60):
        raise ValueError("Invalid time!")

    # converting hours to 24-hour format
    if meridiem1 == "PM" and hour1 != 12:
        hour1 += 12
    if meridiem1 == "AM" and hour1 == 12:
        hour1 = 0

    if meridiem2 == "PM" and hour2 != 12:
        hour2 += 12
    elif meridiem2 == 'AM' and hour2 == 12:
        hour2 = 0

    # formating hours and minutes as strings with leading zeros where needed
    return f"{hour1:02}:{minutes1:02} to {hour2:02}:{minutes2:02}"


if __name__ == "__main__":
    main()