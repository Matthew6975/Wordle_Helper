#This is a wordle bot that helps you solve wordles by suggesting possible words based on your inputs.
#The goal is to have it provide the most probable words based on the current information recieved from previous guesses.

import math
import tkinter as tk
from tkinter import ttk
from Five_Letter_Words import FiveLetterWords as words

unknown = "0"
pos1 = unknown
pos2 = unknown
pos3 = unknown
pos4 = unknown
pos5 = unknown

word = pos1 + pos2 + pos3 + pos4 + pos5
guessed_words = []

# def get_possible_words(word_list, pattern):
#         possible_words = []
#         for w in word_list:
#                 match = True
#                 for i in range(5):
#                         if pattern[i] != unknown and pattern[i] != w[i]:
#                                 match = False
#                                 break
#                 if match:
#                         possible_words.append(w)
#         return possible_words

# --- Color cycle logic ---
COLORS = [
    ("grey",   "#3a3a3c"),
    ("yellow", "#b59f3b"),
    ("green",  "#538d4e")
]

def cycle_color(index):
    """Cycle a button through grey → yellow → green → grey."""
    states[index] = (states[index] + 1) % 3
    color_name, color_hex = COLORS[states[index]]
    buttons[index].config(bg=color_hex, activebackground=color_hex)

def submit():
    guess = entry_guess.get().strip().lower()

    if len(guess) != 5 or not guess.isalpha():
        status_label.config(text="Enter a valid 5-letter word.")
        return

    # Update letters on buttons
    for i in range(5):
        buttons[i].config(text=guess[i].upper())

    # Build result
    result = []
    for i in range(5):
        color_name, _ = COLORS[states[i]]
        result.append((guess[i], color_name))

    status_label.config(text=f"Result: {result}")
    print(result)  # For console output


# --- Main window settings (Dark Mode) ---
root = tk.Tk()
root.title("Wordle GUI")
root.geometry("400x300")
root.configure(bg="#1e1e1e")

style = ttk.Style(root)
style.theme_use("clam")

# Make ttk widgets dark too
style.configure("TLabel", background="#1e1e1e", foreground="white")
style.configure("TButton", background="#333333", foreground="white")
style.configure("TEntry",  fieldbackground="#2b2b2b", foreground="white")

# --- Guess input ---
label = ttk.Label(root, text="Enter 5-letter guess:")
label.pack(pady=10)

entry_guess = ttk.Entry(root, font=("Arial", 16), justify="center")
entry_guess.pack()

# --- Buttons for colors ---
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=20)

states = [0, 0, 0, 0, 0]  # 0=grey, 1=yellow, 2=green
buttons = []

for i in range(5):
    color_name, color_hex = COLORS[0]  # default = grey
    btn = tk.Button(
        button_frame,
        text="",
        font=("Arial", 18, "bold"),
        width=3,
        height=1,
        bg=color_hex,
        fg="white",
        activebackground=color_hex,
        command=lambda i=i: cycle_color(i)
    )
    btn.grid(row=0, column=i, padx=5)
    buttons.append(btn)

# --- Submit button ---
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

status_label = ttk.Label(root, text="", font=("Arial", 10))
status_label.pack()

root.mainloop()
