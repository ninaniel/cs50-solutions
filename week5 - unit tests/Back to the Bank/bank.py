def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        result = 0
    elif greeting.startswith("h"):
        result = 20
    else:
        result = 100
    return result

if __name__ == "__main__":
    main()
