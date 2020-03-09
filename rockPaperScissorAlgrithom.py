'''
Created on Feb 1, 2020

@author: ITAUser
'''

#PSEUDOCODE:
#set variable keepPlaying to true
#While keepPlaying is true:
keepPlaying = True 
while (keepPlaying == True):
   

    #print statement welcoming players to the game
    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)
    #make a key that assigns a number to each choice for the computer
    #(rock is 1, paper is 2, scissor is 3)
    print("welcome player")
    print("(best 2 out of 3 Press 'q' to quit")


    #import the random function - the computer makes its choice randomly from this function

import random 

    #set computer's score to 0
    #set player's score to 0
    #while player's score is less than 2 and computer's score is less than 2:-- this means that the game is still on 
scoreOfComputer = 0 
scoreOfPlayer= 0

      
        
    #computer's choice = random number between 1 and 3 (random function gets used here)
    #players choice = input(ask player to select Rock, Paper, or scissor)
while(scoreOfPlayer<2) and (scoreOfComputer < 2):
    computerChoice = random.randint(1,3)
    playerChoice = input("pick rock, paper, or scissor")

        
    #start checking user options
    #userChocie = userChoice.lower()
    #if player inputs 'q' : -- players wants to end the game
    #    set keepPlaying to False -- ends the loop
    #    stop the loop -- Whoo! break statement
    if (playerChoice == "q"):
        keepPlaying = False
        break

    #else if (player inputs rock and computer chooses rock) or 
    #(player inputs paper and computer chooses paper and computer chooses paper) or
    #(player inputs scissors and computer chooses scissors):
    # print out DRAW
    # print out player's score and computer's score
    elif((playerChoice == "rock" ) and (computerChoice == 1)) or ((playerChoice == "paper" ) and (computerChoice == 2)) or ((playerChoice == "scissors" ) and (computerChoice == 3)):
        print("Computer's Score: ", + scoreOfComputer )
        print("Your Score: ", + scoreOfPlayer)   
    
    #else if (player inputs rock and computer chooses paper)or
    #(player inputs scissors and computer chooses paper) or
    #player inputs paper and computer chooses scissors):
    # add one to the computer's score
    # print out player's score and computer's score
    elif((playerChoice == "rock" ) and (computerChoice == 2)) or ((playerChoice == "paper" ) and (computerChoice == 3)) or ((playerChoice == "scissors" ) and (computerChoice == 1)):
        print("Computer wins")
        scoreOfComputer = scoreOfComputer + 1
        print("Computer's Score: ", + scoreOfComputer)
        print("Your Score: ", + scoreOfPlayer)
    

    #else if (player inputs rock and computer paper) or
    #(player inputs scissors and computer chooses rock) or 
    #(player inputs paper and computer chooses scissors):
    # add one to the player's score
    # print out player's score and computer's score
    elif((playerChoice == "rock" ) and (computerChoice == 3)) or ((playerChoice == "paper" ) and (computerChoice == 1)) or ((playerChoice == "scissors" ) and (computerChoice == 2)):
        print("You win")
        scoreOfPlayer = scoreOfPlayer + 1
        print("Computer's Score: ", + scoreOfComputer)
        print("Your Score: ", + scoreOfPlayer)
    
    #else:
    # tell the user their input was not valid
    else :
        print("Input not valid")
        
    #print statement thanking player for playing 
    #if player's score is 2:
    # print out statement saying player win
    #if computer's score is 2:
    #print statement letting player know computer win
    # print out player's score and computer's score
else:
    if (scoreOfPlayer ==2):
        print("player win")

    if (scoreOfComputer==2):
        print ("Computer Win")
        print("Computer's Score: ", + scoreOfComputer)
        print("Your Score: ", + scoreOfPlayer)
