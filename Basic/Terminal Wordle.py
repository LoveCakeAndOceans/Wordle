
import creating_list
words, t = creating_list.ordered_words(5, "C:\\Users\Surface\Desktop\Stuff\Wordle Project\words.txt")
valid_letters = "abcdefghijklmnopqrstuvwxyz"
new = words[:]
remove_letters = ""
letters_in = ""



def letter_position(colour, input1_col, input2_col):
    global words
    print(input1_col, end="")
    while True:     #The loop of asking for orange letters
        letter = " "
        position = ""
        
        #Get a letter. 
        while letter not in valid_letters:    
            letter = input("Give a " + colour + " letter or type '!' to cancel: ")
            if len(letter) != 1: #Resets letter to a space if the input is longer than one so we can ask again
                letter = " "
            elif letter == "!":
                print(end = "\n")
                break
            
        if letter == "!": #Break the loop of asking for orange
            break


        #Get a valid index for where the orange letter occurs
        while True: #Keep looping until we get an input that can be converted to an int
            print(input2_col, end="")
            try:
                position = input("What position is the letter at? ").replace(" ", "", -1)
                print(end = "\n")
                if position == "!":
                    break
                position = int(position)
            except ValueError:
                print("Not an integer.")
                print(position)
                continue
            else:
                break
            
        if position == "!":  #Break the loop of asking for orange
            break
        
        
        if colour == "ORANGE":
            for j in words:
                if (letter in j[position - 1]) or (letter not in j):
                    new.remove(j)
            words = new[:]
            
        elif colour == "GREEN":
            for j in words:
                if letter not in j[position - 1]:
                    new.remove(j)
            words = new[:]
            
            

while True:
    
# =============================================================================
#     Suggests the best word and decides when to break out of the loop
# =============================================================================
    print("\x1b[1;35m", end="")
    if len(new):
        print("The most optimal word is, \x1b[0;45m", new[0], "\x1b[1;35;49m" )
    else:
        print("\x1b[1;31mThe program has failed to find your word.")
        print("\x1b[1;37m")
        break

    
    guess = input("Was this the correct word [y/n]? ")
    print(end="\n")
    if guess == "y":
        break
    
# =============================================================================
#     GREY INCORRECT
#     
# =============================================================================
    print("\x1b[1;34m", end="")
    remove_input = input("What letters are incorrect? ").replace(" ", "", -1) 
    print(end ="\n")
    for i in words:                 
        for j in remove_input:
            if j in i:
                new.remove(i)
                break
    words = new[:]                  #Words is not shortened so searches through it are faster, and we don't need to keep checking if something in words is in new: it has to be


# =============================================================================
#     POSITION LETTERS -- GREEN AND ORANGE
# =============================================================================
    

    letter_position("GREEN", "\x1b[1;32m", "\x1b[1;32m")
    letter_position("ORANGE", "\x1b[1;33m", "\x1b[1;33m")