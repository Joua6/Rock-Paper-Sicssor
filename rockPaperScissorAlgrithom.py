'''
Created on Feb 1, 2020

@author: ITAUser
'''
from builtins import input


#PSEUDOCODE:
#set variable keepPlaying to true
#While keepPlaying is true:
keepPlaying = True 
while keepPlaying is True: 
   
    #print statement welcoming players to the game
    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)
    #make a key that assigns a number to each choice for the computer
    #(rock is 1, paper is 2, scissor is 3)
    print("Welcome")
    print("Best out of 3 wins, Press 'q' to quit")  
def  pickRandomNumber(): 
    randomNumber = random.radiant(1,3)
    return randomNumber 



    #import the random function - the computer makes its choice randomly from this function

import random 

    #set computer's score to 0
    #set player's score to 0
    #while player's score is less than 2 and computer's score is less than 2:-- this means that the game is still on 
computerScore = 0
playerScore = 0 
while (playerScore < 2) and (computerScore < 2):
    keepPlaying = True 
      
        
    #computer's choice = random number between 1 and 3 (random function gets used here)
    #players choice = input(ask player to select Rock, Paper, or scissor)
def  computerChoice(randomNumber):
    if randomNumber ==1:
        computerChoice = "Rock"
    elif randomNumber == 2:
        computerChoice = "Paper"
    elif randomNumber == 3:
        computerChoice = "scissor"
    return computerChoice 

def getPlayerChoice():
    playerChoice = input("Select Rock, Paper, or Scissor")
    return playerChoice
        
    #start checking user options
    #userChocie = userChoice.lower()
    #if player inputs 'q' : -- players wants to end the game
    #    set keepPlaying to False -- ends the loop
    #    stop the loop -- Whoo! break statement
while playerChoice = userChioce.lower()
    if input ("q"):
        keepPlaying = False 
        break 
   
    #else if (player inputs rock and computer chooses rock) or 
    #(player inputs paper and computer chooses paper and computer chooses paper) or
    #(player inputs scissors and computer chooses scissors):
    # print out DRAW
    # print out player's score and computer's score
    if (playerChocie == "rock" and randomNumber == "rock") or 
    (playerChocie == "paper" and randomNumber "paper") or
    (playerChocie == "scissor" and randomNumber == "scissor"):
    print ("DRAW")
    print (computerScore, playerScore)
    
    #else if (player inputs rock and computer chooses paper)or
    #(player inputs scissors and computer chooses paper) or
    #player inputs paper and computer chooses scissors):
    # add one to the computer's score
    # print out player's score and computer's score
else:  
    if (playerChoice == "rock" and randomNumber == "paper")or
    (playerChoice == "scissors" and randomNumber == "rock") or
    (playerChocie == "paper" and randomNumber == "scissors"):
    print ("Computer Wins")
    computerScore += 1
    print (computerScore, playerScore)
    

    #else if (player inputs rock and computer paper) or
    #(player inputs scissors and computer chooses rock) or 
    #(player inputs paper and computer chooses scissors):
    # add one to the player's score
    # print out player's score and computer's score
    else:  
    if (playerChoice == "paper" and randomNumber == "rock")or
    (playerChoice == "rock" and randomNumber == "scissors") or
    (playerChocie == "scissors" and randomNumber == "paper"):
    print ("Player Wins")
    playerScore += 1
    print (computerScore, playerScore)
    
    #else:
    # tell the user their input was not valid
    else: 
        print("Invalid input")
    #print statement thanking player for playing 
    #if player's score is 2:
    # print out statement saying player win
    #if computer's score is 2:
    #print statement letting player know computer win
    # print out player's score and computer's score
    print("Thank you for playing")
    if 
    playerScore ==2:
        print("player win")
    else:
    if 
    computerScore==2:
        print ("Computer Win")
    
