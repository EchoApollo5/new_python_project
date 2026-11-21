import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROW = 3
COL = 3

symbol_count = {

    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}

def spin(rows, cols, symbols):
    all_symbols = []
    for symbols, symbol_count in symbols.items:
        for _ in range(symbol_count):
            all_symbols.append(symbols)
            


def deposite():
    while True:
        amount = input("enter an amount: ")
        if amount.isdigit:
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("enter valid amount above 0")
        else:
            print("enter a number")
    return amount

def get_num_lines():
    while True:
            lines = input("enter number of lines (1-" + str(MAX_LINE) +")? ")
            if lines.isdigit:
                lines = int(lines)
                if 1 < lines <= MAX_LINE:
                    break
                else:
                    print("Enter a valis number of lines")
            else:
                print("enter a number")
    return lines

def get_bet():
    while True:
            bet = input("enter an amount to bet: ")
            if bet.isdigit:
                bet = int(bet)
                if MIN_BET <= bet <= MAX_BET:
                    break
                else:
                    print(f"amount must be between {MIN_BET} AND {MAX_BET}")
            else:
                print("enter a number")
    return bet




def main():
    balance = deposite()
    
    lines = get_num_lines()
    while True:
        bet= get_bet()
        total_bet =bet*lines
        if total_bet > balance:
            print(f" you do not have neought to bet that amount your current balance is {balance}")
        else:
            break
    print(f'you are betting {bet} on {lines} lines, your total bet is {total_bet}')

main()

