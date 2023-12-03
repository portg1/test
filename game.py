import random

# ----------------------------
def new_game():

    guesses = []
    correct_answers = []
    correct_guesses = 0
    question_number = 1

    for key in questions.keys():
        print("--------------------++++++======-")
        print(key)

        my_list = list(answers[question_number - 1].values())
        random.shuffle(my_list)

        sum_ = 0
        for key_ in answers[question_number-1].keys():
            print(key_, end=". ")
            print(my_list[sum_])
            sum_ += 1

        if my_list[0] == questions.get(key):
            correct_answers.append("A")
        elif my_list[1] == questions.get(key):
            correct_answers.append("B")
        elif my_list[2] == questions.get(key):
            correct_answers.append("C")
        elif my_list[3] == questions.get(key):
            correct_answers.append("D")

        guess = input("What is you answer? (A, B, C or D): ").upper()
        guesses.append(guess)

        if guess == "A":
            guess = my_list[0]
        elif guess == "B":
            guess = my_list[1]
        elif guess == "C":
            guess = my_list[2]
        elif guess == "D":
            guess = my_list[3]

        correct_guesses += check_answer(questions.get(key), guess)

        question_number += 1

    display_score(correct_guesses, guesses, correct_answers)


# ----------------------------
def check_answer(answer_, guess):

    if answer_ == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# ----------------------------
def display_score(correct_guesses, guesses, correct_answers):

    print("----------------------------")
    print("RESULT")
    print("----------------------------")
    print("Answers: ", end="")
    for i in correct_answers:
        print(i, end=" ")
    print("\nGuesses: ", end="")
    for i in guesses:
        print(i, end=" ")

    score = (correct_guesses/len(questions))*100
    print("\nYour score is {}%".format(int(score)))

# ----------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ").upper()

    if response == "YES":
        return True
    else:
        return False


# ----------------------------


questions = {"How old is Mohsen?": "18",
             "Where is Mohsen from?": "Iran",
             "How tall is Mohsen?": "186cm",
             "Where does Mohsen want to go?": "Australia"}

answers = [{"A":"18", "B":"17", "C":"16", "D":"19"},
           {"A":"USA", "B":"Canada", "C":"Germany", "D":"Iran"},
           {"A":"180cm", "B":"181cm", "C":"186cm", "D":"190cm"},
           {"A":"Afghanistan", "B":"Australia", "C":"Japan", "D":"Egypt"}]

while True:
    new_game()

    response = play_again()
    if not response:
        break

print("Bye!")