from emoji import emojize

def main():
    txt = input("Input: ").strip()
    print("Output:", emojize((txt), language='alias'))

if __name__ == "__main__":
    main()