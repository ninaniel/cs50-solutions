#  Einstein's equation
def main():
    m = int(input("m: "))
    E = equation(m)
    print("E:", E)

# calculating an energy
def equation(m):
    return m*(300000000**2)

main()
