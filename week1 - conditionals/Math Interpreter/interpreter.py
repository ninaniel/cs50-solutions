#Math Interpreter
def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(" ")

    print(calculator(x,y,z))

#calculating user's input
def calculator(a,b,c):
    a = float(a)
    c = float(c)
    match b:
        case "+":
            return round(float(a + c), 1)
        case "-":
            return round(float(a - c), 1)
        case "*":
            return round(float(a * c), 1)
        case "/":
            if c != 0:
                return round(float(a / c), 1)
            else:
                print("Can't be divided by Zero!")

main()
