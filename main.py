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

    return amo

def get_number_of_lines():
    while True:
        lines = input("How many lines do you want to bet on (1-" + str(MAX_LINES) + ")? ")
        # isdigit() returns True if the input string is a digit >= 0
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines must be between 1 and {MAX_LINES}")
        else:
            print("Please enter a valid number of lines.")

    return lines

def main():
    balance = deposit()

    return balance

if __name__ == "__main__":
    result = main()
    print(f'Deposited amount = {result}')