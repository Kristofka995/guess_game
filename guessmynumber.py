import random

myNumber = random.randint(1, 20) #choose a number for me
print("My number is between 1 and 20")
guess_count = 0            #counting your guess


for guess in range(1, 6):           #ask the player for guess 6times
    print("What's your number?")
    yourNumber = int(input())


    if yourNumber > myNumber:
        while yourNumber > 20:
            print("Your number is to high, it has to be between 1 and 20")
            print("What's your number?")
            yourNumber = int(input())
        guess_count += 1
        print(f"My number is lower than your, be careful, you can guess {5-guess_count} time!")
    elif yourNumber < myNumber:
        while yourNumber < 1:
            print("Your number is to low, it has to be between 1 and 20")
            print("What's your number?")
            yourNumber = int(input())
        guess_count += 1
        print(f"My number is higher than your, be careful, you can guess {5-guess_count} time!")
    else:
        print("You guessed right")
        break
    if guess_count == 5:
        print("You guessed too many, game end.")
        break
