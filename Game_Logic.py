import random

# Function to generate a random 4-digit number with no repeats
def random_number():
    return random.sample(range(10), 4)

# Function for the user to input their guess
def user_guess():
    while True:
        guess = input("Enter your guess (4 digits, no repeats): ")
        if len(guess) == 4 and len(set(guess)) == 4:
            return [int(digit) for digit in guess]
        print("Invalid input. Please try again.\n")

# Function to calculate the number of cows and bulls in the guess
def cows_and_bulls(number, guess):
    cows = 0
    bulls = 0
    for n, g in zip(number, guess):
        if n == g:
            bulls += 1  # Count bulls (correct digit in correct position)
    for n in guess:
        if n in number:
            cows += 1  # Count cows (correct digit in wrong position)
    cows -= bulls
    return cows, bulls



def display_score(cows, bulls):
    print(f"Cows: {cows}, Bulls: {bulls}\n")# Function to display the score (number of cows and bulls)

print(''' 
    ██████╗ ██████╗ ██╗    ██╗███████╗       █████╗ ███╗   ██╗██████╗       ██████╗ ██╗   ██╗██╗     ██╗     ███████╗
   ██╔════╝██╔═══██╗██║    ██║██╔════╝      ██╔══██╗████╗  ██║██╔══██╗      ██╔══██╗██║   ██║██║     ██║     ██╔════╝
   ██║     ██║   ██║██║ █╗ ██║███████╗      ███████║██╔██╗ ██║██║  ██║      ██████╔╝██║   ██║██║     ██║     ███████╗
   ██║     ██║   ██║██║███╗██║╚════██║      ██╔══██║██║╚██╗██║██║  ██║      ██╔══██╗██║   ██║██║     ██║     ╚════██║
   ╚██████╗╚██████╔╝╚███╔███╔╝███████║      ██║  ██║██║ ╚████║██████╔╝      ██████╔╝╚██████╔╝███████╗███████╗███████║
    ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝      ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝       ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝''')

print('''\n
* Enter a 4-digit number with no repeats.
* You will get feedback on how many cows and bulls you have.
* A cow is a digit that is correct but in the wrong position.
* A bull is a digit that is correct and in the right position.
* Try to guess the number in as few attempts as possible.\n
''')

# Generate a random number
number = random_number()

# Main game loop
guesses = 0
while True:
    guess = user_guess()
    guesses += 1
    cows, bulls = cows_and_bulls(number, guess)
    display_score(cows, bulls)
    if bulls == 4:
        print(f"Congratulations! You won in {guesses} guesses.")
        break # Exit the loop and end the game