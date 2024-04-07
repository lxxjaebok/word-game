import random

def get_user_name():
    user = input("What is your name? ")
    print("Good Luck! %s" % user)

def get_random_word():
    words = ["hello world", "computer science", "south korea", "python programming"]
    return random.choice(words)    

def guessing(word):
    print("")
    print("We are going to play a guess the word game. The word will be chosen by the computer.")
    print("")

    idx = ['_' for _ in word]
    
    turns = 10

    while turns != 0:
        print("You have %d turns left." % turns)
        
        userInput = input("Guess a character: ")
        turns -= 1

        if userInput == word:
            print("You succeeded the game :)")
            break
        elif len(userInput) > 1:
            print("Failed!")
            continue
        else:
            for c in range(len(word)):
                if word[c] == userInput:
                    idx[c] = word[c]

        print(*idx)

        if(turns == 0):
            print("GAME OVER !")

get_user_name()
guessing(get_random_word())