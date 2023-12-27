from random import randint
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                guess(randint(1, level))
            else:
                continue
        except ValueError:
            pass

def guess(number):
    while True:
        try:
            num = int(input("Guess: "))
            if num > 0:
                print("Too large!") if num > number else print("Too small!")
                if num == number:
                    sys.exit("Just right!")
            else:
                continue
        except ValueError:
            pass

main()
