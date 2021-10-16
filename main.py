import time # For using time.sleep

# Function For Marking the answer, and making code less repetitive
def markAnswer(input, answer, score, option):
    
    input = input.upper() # if user input is lowercase
    answer = answer.upper() # if user input is lowercase
    
    if input == answer:
        score = score + 10
        print(f"Well Done! Your Score is: {score}")
        return score
    else: 
        score = score - 5
        print(f"You have lost, the correct answer is: {option}\n The Score is: {score} \n" )
        return score
        


print("Welcome To The Quiz!")

#Declaring Variables

quizQuestion = "Who is the Prime Minister of India?"
optionA = "Sonia Gandhi"
optionB = "Rahul Gandhi"
optionC = "Narendra Modi"
optionD = "Amit Shah"
score = 0

#Printing  First Question \n = newline and {} words in these brackets are variables. f before string to format it.

print(f"{quizQuestion}\nA. {optionA}\nB.{optionB}\nC. {optionC}\nD. {optionD}")

userInput = input("What's is the answer?\n")

score = markAnswer(userInput, 'C', score, optionC)


time.sleep(2) # For Emphasis and suspense for next question

print("Second Question: \n")

quizQuestion = "What language does the computer understand?"
optionA = "Java"
optionB = "atomic"
optionC = "Python"
optionD = "Byte Code"

print(f"{quizQuestion}\nA. {optionA}\nB.{optionB}\nC. {optionC}\nD. {optionD}")

userInput = input("What is the answer?\n")

score = markAnswer(userInput, 'D', score, optionD)