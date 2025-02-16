import random
import tkinter as tk

# Function to generate a random 4-digit number with no repeats
def random_number():
    return random.sample(range(10), 4)

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

# Function to create the GUI
def create_gui():
    window = tk.Tk()
    window.title("Bulls and Cows")

    global guess_label, guess_entry, submit_button, score_label, result_label

    guess_label = tk.Label(window, text="\n\nEnter your guess (4 digits, no repeats):")
    guess_label.pack()

    guess_entry = tk.Entry(window, width=20)
    guess_entry.pack()

    submit_button = tk.Button(window, text="Submit", command=check_guess)
    submit_button.pack()

    score_label = tk.Label(window, text="Score:")
    score_label.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.geometry("400x200")  # Set the window size to 400x200 pixels

    return window

# Function to check the user's guess
def check_guess():
    global guesses
    guess = guess_entry.get()
    if len(guess) == 4 and len(set(guess)) == 4:
        guess = [int(digit) for digit in guess]
        cows, bulls = cows_and_bulls(number, guess)
        guesses += 1
        result_label.config(text=f"Cows: {cows}, Bulls: {bulls}")
        if bulls == 4:
            result_label.config(text=f"Congratulations! You won in {guesses} guesses.")
            submit_button.config(state="disabled")
    else:
        result_label.config(text="Invalid input. Please try again.")

# Initialize variables
number = random_number()
guesses = 0

# Create the GUI
window = create_gui()

# Start the main loop
window.mainloop()