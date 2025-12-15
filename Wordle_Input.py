from Five_Letter_Words import words

guesses = []

greens = [None, None, None, None, None,]
yellows = {}
greys = set()

letters_found = 0

#Intakes users guesses and does some checking to validate input
def guess_func(i):
        global guess 
        guess = input("Enter your " + str(i+1) + " guess: ").lower().strip()
        if len(guess) != 5:
                print("Invalid input. Please enter a 5 letter word.")
                return guess_func()
        elif not guess.isalpha():
                print("Invalid input. Please enter only letters.")
                return guess_func()
        elif guess not in words:
                print("Invalid input. Word not in list.")
                return guess_func()
        guesses.append(guess)
        color()

#Still need to do error handling and fix the add_yellow() function before this is working properly
def color():
       for i in range(len(guess)):
            color = input("What color was the " + guess[i] + " at position " + str(i+1) + "? (G = green, Y = yellow, B = Grey)")
            if color.lower().strip() == "g":
                   add_greens(guess[i], int(i), greens)
                   print(greens)
            elif color.lower().strip() == "y":
                   add_yellows(guess[i], i, yellows)
            elif color.lower().strip() == "b":
                   add_grey(guess[i], greys)
                   print(greys)
            else:
                   print("Error in color() function")



#Works like a dream
def add_greens(letter, position, dictionary):
        if dictionary[position] == None:
                dictionary[position] = str(letter)
        else:
               print("This position already has a green letter")

#Takes the letter and position it was discovered as yellow at, and creates or updates a dictionary entry tracking letters and their possible positions
def add_yellows(letter, position, dictionary):
        if letter not in dictionary:
            dictionary[letter] = {0,1,2,3,4}
        dictionary[letter].remove(position)


def add_grey(letter, lst):
        lst.add(letter)



#runs the loop of information uptake and checks for solved answer with each loop.
for j in range(2):
    for i in range(len(greens)):
            if greens[i] != None:
                    letters_found += 1
            if letters_found >=5:
                    print("\n")
                    print("Wordle Solved! The answer was: " + str(greens[0]) + str(greens[1]) + str(greens[2]) + str(greens[3]) + str(greens[4]))
                    print("\n")
    guess_func(j)


print("guesses = " + str(guesses))
print("greens = " + str(greens))
print("yellows = " + str(yellows))
print("greys = " + str(greys))