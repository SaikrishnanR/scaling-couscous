# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:29:45 2022

@author: Saikrishnan R
"""
############   WELCOME TO THE HANGMAN GAME #################

import random
import time
import pandas as pd


# Initial Steps to invite in the game:
print("\n\t Welcome to Hangman game \n\t".expandtabs(20))
name = input("Enter your User ID : ")
print("Hey " + name + " your unique varification code is XXXX347 \n")
print("The PASSWORD for the hangman vault is : X360QWERTY \n")
print("\t Hello " + name + " All the very best ####\n \t".expandtabs(20))
time.sleep(5)
print("\t  The game is about to start! \n\t".expandtabs(25))
print("\t  Let's play Hangman! \t \n".expandtabs(15))
time.sleep(3)


# To define the parameters for gusseing and correction

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    # words_to_guess = ["film","promise","kids","lungs","doll","rhyme","damage"
    #                ,"plants" , "python", "sairam", "brindavan" , "parthi","trayee"]
    # words_to_guess = pd.read_table("D:\python\words_for_hangman.txt.txt",sep="\s+")
    words_to_guess =pd.read_table("D:\\python\\words_for_hangman.txt.txt",sep="\s+") 
    
    
    
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = " "

    print(words_to_guess)

# A loop to re-execute the game when the first round ends:

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again! Keep the password and user id safe with you")
        
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 6
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter , This letter was already guessed .\n\t".expandtabs(10))

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "=====    \n")
            print("Wrong guess. " + str(limit - count) + "You only have " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "=====    \n")
            print("Wrong guess. " + str(limit - count) + "You only have " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     O \n"
                 "  |     |\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "=====    \n")
           print("Wrong guess. " + str(limit - count) + "You only have " + str(limit - count) + " guesses remaining\n")
           
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "=====    \n" )
            print("Wrong guess. " + str(limit - count) + "You only have " + str(limit - count) + " Guesses remaining \n")
            

        elif count ==5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "=====    \n")
            print("Wrong guess. " + str(limit - count) + " last chance to guess it correcttly , Otherwise your chance will be taken OFF  if you guess the wrong aplhabet \n")

        elif count ==6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |        \n"
                  "=====    \n")
            print("Wrong guess. You are hanged!!!\n")
            print("The Correct word was:", already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        print("\n Unknown user XXXX347 you have successfully completed the objective your revard will be credited to your hidden acc soon\n ")
        print(name + " Dont forget the user id and pass for future refferences !!!!!\n")
        print("The game will auto delete when you type N \n\t".expandtabs(25))
        time.sleep(3)
        play_loop()

    elif count != limit:
       hangman()

main()
hangman()