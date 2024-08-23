def update_coins(coins):
    total_coins2 = 0
    total_coins2=coins+total_coins2
    return total_coins2

def main():
    # defaults
    coke_price = 50
    coins = 0
    total_coins = 0
    acceptable_coins = [25,10,5]

    # take in user input,
    while total_coins < 50:
        coins = int(input("Insert Coin "))

        # user input control
        if coins in acceptable_coins:
            total_coins = update_coins(coins)+total_coins
        print("Amount Due:", coke_price - total_coins)

        if total_coins >= coke_price:
                print("Change Owed:", total_coins - coke_price)

main()

