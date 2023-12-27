import sys

def main():
    # measuring length of args to get only 1 command-line argument & checking the extension to be ".py"
    l = len(sys.argv)
    try:
        if l == 1:
            sys.exit("Too few command-line arguments")
        elif l >= 3:
            sys.exit("Too many command-line arguments")
        elif l  == 2:
            if not sys.argv[1].endswith(".py"):
                sys.exit("Not a Python file")
            else:
                # outputing the number of lines of code in the file.py
                print(lines_of_code(sys.argv[1]))

    except FileNotFoundError:
        sys.exit("File does not exist")

# takes Python file as an arg & returns the number of the lines of code, excluding comments and blank lines(docstring included)
def lines_of_code(doc):
    with open(doc, "r") as file:
        n = 0
        for line in file:
            line = line.lstrip()
            if not line.startswith("#") and line:
                n += 1
        return n

if __name__ == "__main__":
    main()