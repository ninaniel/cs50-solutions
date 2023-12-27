import sys
import csv
from tabulate import tabulate

def main():
    # program should receive exactly one command-line argument
    l = len(sys.argv)
    try:
        if l < 2:
            sys.exit("Too few command-line arguments")
        elif l > 2:
            sys.exit("Too many command-line arguments")
        else:
            # when received 1 command-line arg, checking it to be a csv file
            if not sys.argv[1].endswith(".csv"):
                sys.exit("Not a CSV file")
            else:
                print(pizza_menu(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")

# function takes as argument a CSV file of menu data  and returns the menu table formatted
def pizza_menu(arg):
    with open(arg) as file:
        reader = csv.DictReader(file)
        return tabulate(reader, headers="keys", tablefmt="grid")

if __name__ == "__main__":
    main()