import random
print("Welcome to the number guessing game!")

while True:
    max_number = input("You now get to choose how many numbers you'd like to guess from: ")
    if max_number.isdigit() and int(max_number) > 0:
        max_number = int(max_number)
        correct_number = random.randint(1, max_number)
        print("Great! You have chosen to guess from 1 to " + str(max_number))
        break
    else:
        print("Please enter a valid number above 0")

while True:
    max_attempts = input("You now get to choose how many attempts you'd like to have: ")
    if max_attempts.isdigit() and int(max_attempts) > 0:
        print("Great! You will get " + max_attempts + " attempts")
        print("Now, let's start guessing!")
        max_attempts = int(max_attempts)
        break
    else:
        print("Please enter a valid number above 0")


while max_attempts > 0:
    try:
        user_number = int(input("You have " + str(max_attempts) + " attempts left. What is your guess? "))
    except ValueError:
        print("Please enter a valid number above 0")
        continue

    if user_number <1 or user_number > max_number:
        print("Please enter a number between 1 and " + str(max_number))
        continue

    if user_number == correct_number:
        print("Congratulations, you guessed right!")
        quit()
    else:
        print("That is not the right number.")
        max_attempts -= 1

print("You have no more guesses. The correct number was " + str(correct_number))