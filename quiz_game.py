print("Welcome to the quiz!")

playing = input("Do you want to play? (yes/no): ").lower()

if playing != "yes":
    print("Okay, maybe next time!")
    quit()

print("Great! Let's start the quiz.")
score = 0




print("You got" + str(score) + " questions correct!")