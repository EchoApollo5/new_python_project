import random

print("you have 10 tries")

def computer_number():
    computer_num = random.randint(1, 100)
    computer_num = int(computer_num)
    return (computer_num)


def human_input():
    while True:
        guess = input("guess a number from 1 to 100: ")
        if guess.isdigit():
            guess= int(guess)
            if guess > 100:
                print('Enter a value inside the correct range: ')
            break
        else:
            print("invalid input")
    return(guess)


def guessing(number):
    count = 0
    def difficulty():
        choice = input("how difficult would you like the game to be, (1, 2, 3): ")
        if choice.isdigit:
            if choice == 1:
                attempts = 10
            elif choice == 2:
                attempts = 5
            elif choice == 3:
                attempts = 1
        return (attempts)
    
    attempts = difficulty()
    condition = 0
    while count < attempts:
        guess = human_input()
        if guess == number:
            print("you guessed it")
            condition = True
            break
        elif guess < number:
            print("its bigger")
            inv_count = (attempts - count)-1
            print(f"you have {inv_count} attempts left")
            count += 1
            condition = False
        elif guess > number:
            print("its smaller")
            inv_count = (attempts - count)-1
            print(f"you have {inv_count} attempts left")
            count += 1
            condition = False

    if condition:
        print('you won')
    else:
        print(f'you lost, the number was {number}')
    return

def main():
    while True:
        number = computer_number()
        guessing(number)
        play_again = input('do you want to play again, (yes or no): ')
        if play_again == "yes" or "no":
            if play_again == 'no':
                break
        else:
            print("please enter a valid answer")
            
        
        



main()

