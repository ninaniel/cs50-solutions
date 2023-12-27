import sys
from random import choice
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    f = ["-f", "--font"]

    if len(sys.argv) == 1:
        font = choice(figlet.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in f and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font = font)
    user_input = input("Input: ").strip()
    print("Output:", figlet.renderText(user_input), sep = "\n")

if __name__ == "__main__":
    main()