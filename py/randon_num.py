import random
def main():
    correct_number = random.randint(1, 20)
    chances = 5
    
    print("Welcome to the Number Guessing Game!")
    print("You have 5 chances to guess the correct number between 1 and 20.")

    while chances > 0:
        guess = int(input("Enter your guess: "))

        if guess == correct_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < correct_number:
            print("The correct number is higher.")
        else:
            print("The correct number is lower.")
        
        chances -= 1
        print(f"You have {chances} chances left.")

    if chances == 0:
        print(f"Sorry, you've run out of chances. The correct number was {correct_number}.")

if __name__ == "__main__":
    main()
