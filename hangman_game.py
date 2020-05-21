import random

def man_created(count):
    if count == 9:
        print("             ")
        print("    O        ")
        print("             ")
    if count  == 8:
        print("             ")
        print("    O        ")
        print("    |        ")
    if count == 7:
        print("             ")
        print("    O /      ")
        print("    |        ")
    if count == 6:
        print("              ")
        print("  \ O /       ")
        print("    |         ")
    if count == 5:
        print("              ")
        print("  \ O /       ")
        print("    |         ")
        print("   /          ")
    if count == 4:
        print("              ")
        print("  \ O /       ")
        print("    |         ")
        print("   / \        ")
    if count == 3:
        print("    -----     ")
        print("  \ O /       ")
        print("    |         ")
        print("   / \        ")
    if count == 2:
        print("    ------    ")
        print("  \ O /  |    ")
        print("    |         ")
        print("   / \        ")
    if count == 1:
        print("    ------    ")
        print("  \ O / -|    ")
        print("    |        ")
        print("   / \        ")
    if count == 0:
        print("    ------    ")
        print("    O----|    ")
        print("  / | \      ")
        print("   / \        ")
        print("good man is no more")


#random word generator
def word_generator():
    list_of_words = ["hell","loggerhead","helper","tiger","superman","student","killer","baby","dog","nemesis"]
    return random.choice(list_of_words)

def hangman_require(word_generated):
    valid_lettters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    #initially  guess is empty
    guess_by_user = ''
    while len(word_generated) > 0:
        main = ""
        missed = 0
        for letter in word_generated:
            if letter in guess_by_user:
                main = main + letter
            else:
                main = main + "-"+" "
        if main == word_generated:
            print(main)
            print("you win")
            break
        print("guess the word",main)
        guess = input()

        if guess in valid_lettters:
            guess_by_user = guess_by_user + guess
        else:
            print("enter a valid character")
        if guess not in word_generated:
            turns = turns -1
            if turns == 9:
                man_created(turns)
            if turns == 8:
                man_created(turns)
            if turns == 7:
                man_created(turns)
            if turns == 6:
                man_created(turns)
            if turns == 5:
                man_created(turns)
            if turns == 4:
                man_created(turns)
            if turns == 3:
                man_created(turns)
            if turns == 2:
                man_created(turns)
            if turns == 1:
                man_created(turns)
            if turns == 0:
                man_created(turns)
                break
#creating the interface
name = input("what is your name: ")
print(" Welcome to the Hangman game %s ! Hope you can save the good man from dying"%name)
print("\n")
print("we have decided a word for you to guess in less than 10 attempts, hope you can save the man")
print("\n")
word_generated = word_generator()
hangman_require(word_generated)
