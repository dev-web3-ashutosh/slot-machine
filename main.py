import random

MAX_LINES = 3

MIN_BET = 1
MAX_BET = 1000

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# generate slot machine with values
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # _ in python is an anonymous variable
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # copies one list to another
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# print values of slot machine
def print_slot_machine(columns):
    # transpose the columns to print it like rows
    for row in range(len(columns[0])): # gets num of elements in first column
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")

        print()

# check winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# take user input for amount deposited
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
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

# take user input for number of lines to bet on
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

# take user input for amount to bet on each line
def get_bet_amount():
    while True:
        bet = input("How much do you want to bet between ($" +str(MIN_BET) +" - $" + str(MAX_BET) + ") on each line? $")
        # isdigit() returns True if the input string is a digit >= 0
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a valid bet amount.")

    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()

    # check that total bet is less than or equal to balance
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You cannot bet more than your balance amount. Your current balance is ${balance}')
        else:
            break

    print(f'Balance = ${balance} | Number of Lines = {lines} | Total Bet = ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUES)
    new_balance = balance - total_bet + winnings
    print(f"You won ${winnings}. New Balance (Deposit - Total Bet + Winnings) = ${new_balance}")
    print(f"You won on line(s): ", *winning_lines)

if __name__ == "__main__":
    main()
