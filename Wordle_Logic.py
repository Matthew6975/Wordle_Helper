from Five_Letter_Words import words

guesses = []

greens = [None, None, None, None, None,]
yellows = {}
greys = set()

#pretty sure this variable is being incrimented wrong and grows when it shouldn't. Look into this.
letters_found = 0

potential_answers = set()

#Intakes users guesses and does some checking to validate input
def guess_func(i):
        global guess 
        guess = input("Enter your " + str(i+1) + " guess: ").lower().strip()
        if len(guess) != 5:
                print("Invalid input. Please enter a 5 letter word.")
                return guess_func(i)
        elif not guess.isalpha():
                print("Invalid input. Please enter only letters.")
                return guess_func(i)
        elif guess not in words:
                print("Invalid input. Word not in list.")
                return guess_func(i)
        guesses.append(guess)
        color()

def color():
       for i in range(len(guess)):
            color = input("What color was the " + guess[i] + " at position " + str(i+1) + "? (G = green, Y = yellow, B = Grey) ")
            if color.lower().strip() == "g":
                   add_greens(guess[i], i)
                   align_lists()
                   print(greens)
            elif color.lower().strip() == "y":
                   add_yellows(guess[i], i)
                   align_lists()
            elif color.lower().strip() == "b":
                   add_grey(guess[i])
                   align_lists()
                   print(greys)
            else:
                   print("Error in color() function")


#Tracks correct letter for each position
def add_greens(letter, position):
       if letter in yellows: 
              if position in yellows[letter]:
                     print(str(letter) + " is yellow at this position. Do you want to overwrite it as green instead?")
                     global yellow_choice
                     yellow_choice = input("Y = yes, N = no \n")
                     if yellow_choice.strip().lower() == "y":
                            greens[position] = str(letter)
                            yellows.setdefault(letter, set()).add(position)
                     elif yellow_choice.strip().lower() =="n":
                            return
                     else:
                            print("Invalid input. Keeping original value")
       elif letter in greys:
              print(str(letter) + " is marked as grey. Do you want to overwrite it as green in position: " + str(position+1) + "?")
              global grey_choice 
              grey_choice = input("Y = yes, N = no \n")
              if grey_choice.lower().strip() == "y":
                     greens[position] = str(letter)
                     greys.remove(letter)
              elif grey_choice.lower().strip() == "n":
                     return
              else:
                     print("Invalid input. Keeping original value")
       elif greens[position] != None and greens[position] != letter:
              print("Position " + str(position+1) + " already has the green letter: " + str(greens[position]) + ". Do you want to overwrite this with letter: " + str(letter) + "?")
              global green_choice
              green_choice = input("Y = yes, N = no \n")
              if green_choice.lower().strip() == "y":
                      greens[position] = str(letter)
              elif green_choice.lower().strip() == "n":
                     return
              else:
                     print("Input not valid. Keeping original value.")          
       else:
              greens[position] = str(letter)


#Tracks the positions the letter CANNOT be in,
def add_yellows(letter, position):
       if letter in greys:
              print(str(letter) + " is marked as grey. Do you want to overwrite it as yellow in position: " + str(position+1) + "?")
              global yellow_choice 
              yellow_choice = input("Y = yes, N = no \n")
              if yellow_choice.lower().strip() == "y":
                     yellows.setdefault(letter, set()).add(position)
                     greys.remove(letter)
              elif yellow_choice.lower().strip() == "n":
                     return
              else:
                     print("Invalid input. Keeping original value") 
       elif greens[position] == letter:
              print(str(letter) + " is marked as green in position " + str(position+1) + ". Do you want to overwrite it as yellow in position: " + str(position+1) + " instead?")
              global green_choice
              green_choice = input("Y = yes, N = no \n")
              if green_choice.strip().lower() == "y":
                    yellows.setdefault(letter, set()).add(position)
                    greens.remove(letter)
              elif green_choice.strip().lower() == "n":
                     return
              else:
                     print("Invalid input. Keeping original value")
       
       else:
              if letter in yellows and len(yellows[letter]) < 4:
                     yellows.setdefault(letter, set()).add(position)
              elif letter not in yellows:
                     yellows.setdefault(letter, set()).add(position)
              else:
                     print("This letter is marked as yellow in all 5 positions. This is an error. You should restart the solver program.")


#Tracks the letters that are not present in the answer
def add_grey(letter):
       if letter not in greens and letter not in yellows:
              greys.add(letter)
       elif letter in greens:
              print(str(letter) + " is marked green in position " + str(greens.index(letter)+1) + ". Do you want to overwrite " + str(letter) + " as a grey letter instead?")
              global green_choice
              green_choice = input("Y = yes, N = no \n")
              if green_choice.lower().strip() == "y":
                      ltr_pos = greens.index(letter)
                      greens[ltr_pos] = None
                      greys.add(letter)
              elif green_choice.lower().strip() == "n":
                     return
              else:
                     print("Input not valid. Keeping original value.") 
       elif letter in yellows:
              print(str(letter) + " is yellow at this position. Do you want to overwrite it as grey instead?" )
              global yellow_choice
              yellow_choice = input("Y = yes, N = no \n")
              if yellow_choice.strip().lower() == "y":
                     greys.add(letter)
                     del yellows[letter]
              elif yellow_choice.strip().lower() =="n":
                     return
              else:
                     print("Invalid input. Keeping original value")

#Flesh this out with a bunch of logical checks that confirm each list is as it should be. i.e. if a letter is discovered green, make sure it is removed from greys
# as to not interfere with the logic.
def align_lists(): #Align? Harmonize? Validate? Normalize? synchronize? Reconcile? Resolve? align_constraints()? So many good word choices!
       print("Aligning Lists . . .")


def find_answers():
       for word in words:
              if all(
                     greens[i] is None or greens[i] == word[i]
                     for i in range(len(word))
              ) and all(
                     letter in word and
                     all(word[pos] != letter for pos in bad_pos)
                     for letter, bad_pos in yellows.items()
              ) and all(
                     letter not in greys
                     for letter in word
              ):
                     potential_answers.add(word)
       print("There are " + str(len(potential_answers)) + " potential answers. They are: " + str(potential_answers))
       potential_answers.clear()


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
    find_answers()


print("guesses = " + str(guesses))
print("greens = " + str(greens))
print("yellows = " + str(yellows))
print("greys = " + str(greys))