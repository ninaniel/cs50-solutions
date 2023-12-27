from validator_collection import checkers

def main():

    print("Valid") if is_valid_email() else print("Invalid")

def is_valid_email(prompt = "What's your email address? "):
    return checkers.is_email(input(prompt))

if __name__ == "__main__":
    main()
