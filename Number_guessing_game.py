import random

print("you have 10 tries")

def computer_number():
    computer_num = random.randint(1, 100)
    return (computer_num)


def human_input():
    while True:
        guess = input("guess a number from 1 to 100: ")
        if guess.isdigit():
            guess= int(guess)
            if 1 <= guess <= 100:
                return(guess)
            else: 
                print('Enter a value inside the correct range: ')
        else:
            print("invalid input")

def difficulty():
    while True:
        choice = input("how difficult would you like the game to be, (1, 2, 3): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                attempts = 10
                break
            elif choice == 2:
                attempts = 5
                break
            elif choice == 3:
                attempts = 1
                break
            else:
                print('enter a valid value')
        else:
            print('enter a number')
        
    return (attempts)   


def guessing(number):
    count = 0
    attempts = difficulty()
    won = False
    while count < attempts:
        guess = human_input()
        if guess == number:
            print("you guessed it")
            won = True
            break
        elif guess < number:
            print("its bigger")
        elif guess > number:
            print("its smaller")
        count += 1
        inv_count = (attempts - count)
        print(f"you have {inv_count} attempts left")
        

    if won:
        print('you won')
    else:
        print(f'you lost, the number was {number}')
    return

def main():
    while True:
        number = computer_number()
        guessing(number)
        play_again = input('do you want to play again, (yes or no): ').lower()
        if play_again in ('yes', 'no'):
            if play_again == 'no':
                break
        else:
            print("please enter a valid answer")
            
main()
