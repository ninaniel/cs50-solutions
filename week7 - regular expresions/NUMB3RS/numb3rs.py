import re

def main():
    print(validate(input("IPv4 Address: ")))

#function checks if ip matches the pattern #.#.#.# for # in range 0-255
def validate(ip):
    if re.search(r"^(\d+\.){3}(\d+)$", ip):
        nums = ip.split(".")
        if all(0 <= int(n) <= 255 for n in nums):
            return True

    return False

if __name__ == "__main__":
    main()
