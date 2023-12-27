def main():
    coke_price = 50
    change = buy_coke(coke_price)
    print(f"Change Owed: {abs(change)}")

def buy_coke(price):
    coins = [5, 10, 25]
    while price > 0:
        print(f"Amount Due: {price}")
        coin = int(input("Insert Coin: "))
        if coin in coins:
            price -= coin
    return price

main()
