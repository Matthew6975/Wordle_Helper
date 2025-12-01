#This is a wordle bot that helps you solve wordles by suggesting possible words based on your inputs.
#The goal is to have it provide the most probable words based on the current information recieved from previous guesses.

import math
from Five_Letter_Words import FiveLetterWords as words

unknown = "_"  #Represents an unknown letter in the pattern.
#Each position can be either a known letter, an array of possible letters (yellows from other locations), or unknown (_).
#Add third element to track known incorrect letters for that position?
# pos1 = ["h", ["h"]]
pos1 = [unknown, {"p", "s"}]
pos2 = [unknown, {"p", "s"}]
pos3 = [unknown, {"p", "s"}]
pos4 = [unknown, {"s"}]
pos5 = [unknown, {"p"}]
pattern = [pos1, pos2, pos3, pos4, pos5]

known_letters = pos1[0] + pos2[0] + pos3[0] + pos4[0] + pos5[0]

guessed_words = []

def guess_func():
        global guess 
        guess = input("Enter your guess of 5 letters: ").lower().strip()
        if len(guess) != 5 or not guess.isalpha() or guess not in words:
                print("Invalid input. Please enter a 5 letter word from the list.")
                guess_func()
        guessed_words.append(guess)

guess_func()

possible_words = []
greens_passed = []
yellows_passed = []
# print("Pattern:", pattern)
# print("Known letters:", known_letters)
# print("Guessed words:", guessed_words)

if guess in words:
        for w in words:
                print("Checking word:", w)
                for p in range(5):
                        if w[p] in pattern[p][1]:
                                yellows_passed.append(w)
                        if pattern[p][0] != unknown and w[p] == pattern[p][0]:
                                greens_passed.append(w)
if greens_passed or yellows_passed:
        possible_words = list(set(greens_passed) & set(yellows_passed))



print("greens passed:", greens_passed)
print("yellows passed:", yellows_passed)
print("possible words", possible_words)
print(len(possible_words))












                        # print("Pos" + str(p+1) + ":" + str(pattern[p]), end="")
                        # print("\n")
                        # for i in range(2):
                        #         print(pattern[p][i] + ",", end="")
