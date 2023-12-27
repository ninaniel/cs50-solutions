def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(word):
    length = len(word)
    if 2 <= length <= 6:
        if word.isalpha():
            return True
        elif word.isalnum() and word[0:2].isalpha():
            for i in range(length):
                if word[i].isdigit():
                    if word[i] != "0" and word[i:length].isdigit():
                        return True
                    else:
                        return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
