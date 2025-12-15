#This is a wordle bot that helps you solve wordles by suggesting possible words based on your inputs.
#The goal is to have it provide the most probable words based on the current information recieved from previous guesses.

from Five_Letter_Words import FiveLetterWords as words

unknown = "_"  #Represents an unknown letter in the pattern.
#The first position can be either a known letter or unknown(_), and the second is an array of possible letters (yellows from other locations).
#Add third element to track known incorrect letters for that position?
# pos1 = ["h", {"h"}]
# pos2 = [unknown, {"p", "s"}]
# pos3 = [unknown, {"p", "s"}]
# pos4 = [unknown, {"s"}]
# pos5 = [unknown, {"p"}]

pos1 = [unknown, set()]
pos2 = [unknown, set()]
pos3 = [unknown, set()]
pos4 = [unknown, set()]
pos5 = [unknown, set()]

answer = "crake"  #paper would pair well with apple as testing double letters. #Here for testing purposes. Replace with input function later once GUI is done.

pattern = [pos1, pos2, pos3, pos4, pos5]

guessed_words = []

yellow_letters = set() #Not sure if I want or need these sets yet. Probably want Grey at the minimum

grey_letters = set()

greeen_letters = set() 

def guess_func():
        global guess 
        guess = input("Enter your guess of 5 letters: ").lower().strip()
        if len(guess) != 5:
                print("Invalid input. Please enter a 5 letter word.")
                guess_func()
        elif not guess.isalpha():
                print("Invalid input. Please enter only letters.")
                guess_func()
        elif guess not in words:
                print("Invalid input. Word not in list.")
                guess_func()
        guessed_words.append(guess)

guess_func()

for i in range(len(guess)):
        #if green
        if guess[i] == answer[i]:
                pattern[i][0] = guess[i]
        #if yellow
        if guess[i] in answer and guess[i] != answer[i]:
                for j in range(len(guess)):
                        if j != i and pattern[j][0] == unknown:
                                pattern[j][1].add(guess[i])
        for i in range(len(pattern)):
                if pattern[i][0] != unknown:
                        pattern[i][1] = set()


known_letters = pos1[0] + pos2[0] + pos3[0] + pos4[0] + pos5[0]


possible_words = []
greens_passed = []
yellows_passed = []
duplicates_removed = [] #here for testing purposes. Can be removed once log is solidand tested.
print("Pattern:", pattern) #here for testing purposes. Can be removed once log is solidand tested.
print("Known letters:", known_letters) #here for testing purposes. Can be removed once log is solidand tested.
print("Guessed words:", guessed_words) #here for testing purposes. Can be removed once log is solidand tested.

# #Main logic loop. Goes through each word in the list and checks against the pattern.
# if guess in words:
#         for w in words:
#                 for p in range(len(pattern)):
#                         #Checks for yellows. This needs to expand and will get A LOT more complex as it grows. Not sure how to deal with duplicates yet.
#                         if w[p] in pattern[p][1] and w not in yellows_passed:
#                                 yellows_passed.append(w)
#                         #Checks for greens. This may need to expand but will likely be very simple.
#                         if w[p] == pattern[p][0] and w not in greens_passed:
#                                 greens_passed.append(w)


if guess in words:
        for w in words:
                for p in range(len(pattern)):
                        if w[p] == pattern[p][0] and w not in possible_words:
                                greens_passed.append(w)
for w in greens_passed:
        for p in range(len(pattern)):
                if w[p] in pattern[p][1] and w not in yellows_passed:
                        yellows_passed.append(w)



#Combines results and rempoves duplicates. duplocates_removed is for testing purposes and should be removed once logic is complete.
if greens_passed or yellows_passed:
        shorter = greens_passed if len(greens_passed) < len(yellows_passed) else yellows_passed
        for word in shorter:
                if word in greens_passed and word in yellows_passed:
                        duplicates_removed.append(word)
        possible_words = list(set(greens_passed) | set(yellows_passed))
        for i in guessed_words:
                if i in possible_words:
                        possible_words.remove(i)



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
