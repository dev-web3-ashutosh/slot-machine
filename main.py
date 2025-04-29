# take user input for amount deposited
def deposit():
    while True:
        amount = input("How much would you like to deposit?")
        # check if the input string is a positive digit
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Amount must be greater than 0")

    return amount

