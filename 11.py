import random
def guessing_game():
    secret=random.randint(1,10)
    attempts=5
    print("Enter a number between 1 and 10, you have 5 tries!")
    while attempts>0:
        guess=int(input("Enter a number between 1 and 10:"))
        if guess>10:
            print("The number is invalid")
            break
        if guess==secret:
            print("Congrats!, You win")
            break
        elif guess>secret:
            print("Too high\n")
        else:
            print("Too low\n")
        attempts -=1
        print(f"Number of tries left {attempts}\n")
    if attempts==0:
        print(f"You are out of tries, the secret number is {secret}")
guessing_game()
