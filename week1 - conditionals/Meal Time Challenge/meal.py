def main():
    time = input("what time is it? ").strip()
    result = convert(time)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")

# converting time to float
def convert(time):
    if time.endswith(" a.m."):
        hours, minutes_A = time.removesuffix(" a.m.").split(":")
        hours = float(hours)
        minutes_A = float(minutes_A)/60
        result = hours + minutes_A        
    elif time.endswith(" p.m."):
        hours, minutes_P = time.removesuffix(" p.m.").split(":")
        minutes_P = float(minutes_P)/60
        hours = float(hours)
        if hours == 12.0:
            result = hours + minutes_P
        else:
            result = 12 + hours + minutes_P
    else:
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)/60
        result = hours + minutes
        
        return result


if __name__ == "__main__":
    main()