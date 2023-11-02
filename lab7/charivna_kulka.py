import random
import time
import sys

answers = ["Yes", "No", "Maybe"]
count_of_answers = len(answers)
probabilities = [1/3, 1/3, 1/3]

def printt(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

# Sets the same probability percentage to all answers
def even_probabilities_distribution():
    global answers
    global count_of_answers
    count_of_answers = len(answers)
    global probabilities
    equal_probability = 1 / count_of_answers
    probabilities = [equal_probability] * count_of_answers
    return equal_probability

# Custom probability distribution
def custom_distribution():
    global probabilities
    printt("Enter the chance of the answer from 0 to 1, sum of all answers should add up to 1")

    new_probabilities = [0.0] * count_of_answers
    sum_of_new_chances = 0

    for i in range(count_of_answers):
        while True:
            try:
                text = "\nEnter the new probability for answer '" + answers[i] + "': "
                printt(text)
                custom_prob = float(input())
                new_probabilities[i] = custom_prob
                sum_of_new_chances += custom_prob
                break  # Exit the loop if input is successfully converted to float
            except ValueError:
                printt("\nInvalid input. Please enter a valid float.")

    if sum_of_new_chances == 1:
        probabilities = new_probabilities
        printt("\nNew chances have been set.")
        return 1
    else:
        printt("\nSum of all the chances is not 1, chances have not been saved")
        return 0

# Get answer based on the probabilities
def get_random_answer():
    random_index = random.choices(range(count_of_answers), probabilities)[0]
    return answers[random_index]

# Check string for wrong input
def question_validation(question):
    length = len(question)
    if length < 10:
        return False
    digits = 0
    spaces = 0
    for char in question:
        if char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1

    if spaces == 0:
        return False

    if digits > 0:
        # If 25% or more of the string are numbers
        if digits/length > 0.25:
            return False

    # If 30% or more of the string are spaces
    if spaces/length > 0.3:
        return False
    # If more than 50% of the string are spaces and digits
    if (spaces + digits) / length > 0.5:
        return False

    return True

def charivna_kulka(question):
    # If the question has not been approved by the additional function
    if not question_validation(question):
        printt("Question is invalid, unable to answer.")
        return

    # If the question is legit
    answer = get_random_answer()
    printt('\nAnswer is: ' + answer)

while True:
    printt("\nMenu:\n1. To change probabilities\n2. To Ask a question\n3. Add a new answer\n4. Exit\n")
    printt("Enter your choice (1/2/3/4): ")
    choice = input()

    if choice == '1':
        # Option to change probabilities
        custom_distribution()

    elif choice == '2':
        # Option to ask a question
        question = input("Ask a question: ")
        charivna_kulka(question)

    elif choice == '3':
        # Option to add a new question
        new_answer = input("Enter a new answer: ")
        answers.append(new_answer)
        even_probabilities_distribution()
        printt("New answer added. Chances updated.")

    elif choice == '4':
        # Exit the program
        break

    else:
        printt("Invalid choice. Please select a valid option (1/2/3/4).")


