#This is a wordle bot that helps you solve wordles by suggesting possible words based on your inputs.
#The goal is to have it provide the most probable words based on the current information recieved from previous guesses.

import math
from Five_Letter_Words import FiveLetterWords as words

unknown = "_"  #Represents an unknown letter in the pattern.
#The first position can be either a known letter or unknown(_), and the second is an array of possible letters (yellows from other locations).
#Add third element to track known incorrect letters for that position?
pos1 = ["h", ["h"]]
# pos1 = [unknown, {"p", "s"}]
pos2 = [unknown, {"p", "s"}]
pos3 = [unknown, {"p", "s"}]
pos4 = [unknown, {"s"}]
pos5 = [unknown, {"p"}]
pattern = [pos1, pos2, pos3, pos4, pos5]

known_letters = pos1[0] + pos2[0] + pos3[0] + pos4[0] + pos5[0]

guessed_words = []

# def guess_func():
#         global guess 
#         guess = input("Enter your guess of 5 letters: ").lower().strip()
#         if len(guess) != 5 or not guess.isalpha() or guess not in words:
#                 print("Invalid input. Please enter a 5 letter word from the list.")
#                 guess_func()
#         guessed_words.append(guess)

# guess_func()

possible_words = []
greens_passed = []
yellows_passed = []
duplicates_removed = [] #here for testing purposes. Can be removed once log is solidand tested.
print("Pattern:", pattern) #here for testing purposes. Can be removed once log is solidand tested.
print("Known letters:", known_letters) #here for testing purposes. Can be removed once log is solidand tested.
print("Guessed words:", guessed_words) #here for testing purposes. Can be removed once log is solidand tested.

#Main logic loop. Goes through each word in the list and checks against the pattern.
guess = "helps"  #Here for testing purposes. Replace with input function later.
if guess in words:
        for w in words:
                print("Checking word:", w)
                for p in range(5):
                        #Checks for yellows. This needs to expand and will get A LOT more complex as it grows. Not sure how to deal with duplicates yet.
                        if w[p] in pattern[p][1] and w not in yellows_passed:
                                yellows_passed.append(w)
                        #Checks for greens. This may need to expand but will likely be very simple.
                        if pattern[p][0] != unknown and w[p] == pattern[p][0] and w not in greens_passed:
                                greens_passed.append(w)

# Combines results and rempoves duplicates. duplocates_removed is for testing purposes and should be removed once logic is complete.
if greens_passed or yellows_passed:
        shorter = greens_passed if len(greens_passed) < len(yellows_passed) else yellows_passed
        for word in shorter:
                if word in greens_passed and word in yellows_passed:
                        duplicates_removed.append(word)
        possible_words = list(set(greens_passed) | set(yellows_passed))



print("greens passed:", greens_passed)
print(len(greens_passed))
print("\n")
print("yellows passed:", yellows_passed)
print(len(yellows_passed))
print("\n")
print("duplicates removed:", duplicates_removed)
print(len(duplicates_removed))
print("\n")
print("possible words", possible_words)
print(len(possible_words))
