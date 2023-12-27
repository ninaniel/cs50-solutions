import random

def main():
    level = get_level()
    score = 0
    tries = 3
    for _ in range(10):
        x, y = generate_integer(level)
        sum = x + y
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == sum:
                    score += 1
                    break
                else:
                    raise ValueError

            except ValueError:
                print("EEE")
                tries -= 1
                if tries == 0:
                    print(f"{x} + {y} = {sum}")
                    break

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            l = int(input("level: "))
            if 1 <= l <= 3:
                return l
            else:
                continue
        except ValueError:
            pass
        
def generate_integer(n):
    start = 10**(n-1) if n != 1 else 0
    end = 10**n
    x = random.randrange(start, end)
    y = random.randrange(start, end)
    return x, y

if __name__ == "__main__":
    main()