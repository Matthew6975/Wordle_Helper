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
                   add_greens(guess[i], int(i))
                   print(greens)
            elif color.lower().strip() == "y":
                   add_yellows(guess[i], i)
            elif color.lower().strip() == "b":
                   add_grey(guess[i])
                   print(greys)
            else:
                   print("Error in color() function")



#Works like a dream
def add_greens(letter, position):
        if greens[position] == None:
               greens[position] = str(letter)
        elif letter in yellows: 
               if position not in yellows[letter]:
                      print() #Need to fill this logic in to handle if a green is assigned a position it was previously said to be yellow at. Logical error, or maybe user updating earlier incorrect input.
        else:
               print("Position " + str(position+1) + " already has the green letter: " + str(greens[position]) + ". Do you want to overwrite this with letter: " + str(letter) + "?")
               global choice
               choice = input("Y = yes, N = no")
               if choice.lower().strip() == "y":
                      greens[position] = str(letter)
               elif choice.lower().strip() == "n":
                      return
               else:
                      print("Input not valid. Keeping original value.")


#Takes the letter and position it was discovered as yellow at, and creates or updates a dictionary entry tracking letters and their possible positions
def add_yellows(letter, position):
        if letter not in yellows:
            yellows.setdefault(letter, set()).add(position)



def add_grey(letter):
        greys.add(letter)

#Flesh this out with a bunch of logical checks that confirm each list is as it should be. i.e. if a letter is discovered green, make sure it is removed from yellows
# as to not interfere with the logic.
def validate_lists():
       print("Validating Lists . . .")



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