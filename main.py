MAX_LINES = 3

# take user input for amount deposited
def deposit():
    while True:
        amount = input("How much would you like to deposit? ")
        # isdigit() returns True if the input string is a digit >= 0
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")

    return amount

def main():
    balance = deposit()

    return balance

if __name__ == "__main__":
    result = main()
    print(f'Deposited amount = {result}')