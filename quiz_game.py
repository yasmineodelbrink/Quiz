print("Welcome to the quiz!")

playing = input("Do you want to play? (yes/no): ").lower()

if playing != "yes":
    print("Okay, maybe next time!")
    quit()

print("Great! Let's start the quiz.")
score = 0

Questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the chemical symbol for gold?": "Au"
}

for question, answer in Questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is " + answer)

print("You got " + str(score) + " questions correct!")