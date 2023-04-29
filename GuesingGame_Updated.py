
from getpass import getpass
import random

#Creates an function that lets you guess the computers randomly generated number
def computer_player():
    #generates a random number between 1 and 100
    computer_num = random.randint(1,100)
        
    #takes users input and converts the string into a interger
    player_two_num = int(input("Guess The Computers Number: "))
    
    #asks the user to guess the computer number checks to see if the number is between 1 and 100
    
    p2_tries = 0    
    while True:
        player_two_num = int(input("Enter a number between 1 and 100: "))
        #tells player two if their number is too low
        if player_two_num >= 1 and player_two_num <=100:
            if (player_two_num < computer_num):
                print("Too Low")
                print("\n")       
        #tells player two if their number is too high    
            elif(player_two_num > computer_num):
                print("Too High")
                print("\n")
            #tells player two they won    
            else:
                print("You're Correct")
                print("\n")
                break
            p2_tries += 1
            #if p2_tries is greater than or equal to 5 player two is notified that the game is over and what player one number was.
            while p2_tries >= 5:
                print("Game Over")
                print("Player Ones Number was "+str(computer_num))
                return 1
        else:         
            player_two_num = int(input("You have to enter a number between 1 and 100: "))

#Creates an function that lets you guess the computers randomly generated number                 
def player_one():
    #getpass allows for player_one to hide their input
    player_one_num = int(getpass("Player One Enter a Number between 1 and 100: "))
           
    # counts the number of times player one enters a number less than 1 or greater than 100
    p1_tries = 0
    while True:     
        if player_one_num >=1 and player_one_num <= 100 :
            break      
        else:
            player_one_num = int(getpass("Please enter a Number between 1 and 100: "))
            
        
    #if player two enters a number less than 1 or greater than 100 they are asked to re-enter a number        
    #counts the number of attempts that player two made
    p2_tries = 0
    while True:
        player_two_num = int(input("Enter a number between 1 and 100: "))
        #tells player two if their number is too low
        if player_two_num >= 1 and player_two_num <=100:
            if (player_two_num < player_one_num):
                print("Too Low")
                print("\n")       
        #tells player two if their number is too high    
            elif(player_two_num > player_one_num):
                print("Too High")
                print("\n")
            #tells player two they won    
            else:
                print("You're Correct")
                print("\n")
                break
            p2_tries += 1
            #if p2_tries is greater than or equal to 5 player two is notified that the game is over and what player one number was.
            while p2_tries >= 5:
                print("Game Over")
                print("Player Ones Number was "+str(player_one_num))
                return 1
        else:         
            player_two_num = int(input("You have to enter a number between 1 and 100: "))    

#lets players select between two games 1 for computer and 2 for human player        
game_selector = int(input("To Play Against Computer Enter 1 or 2 to Play Against Another Player: "))
print("\n")
if game_selector == 1:
    computer_player()  
    
if game_selector == 2:
    player_one()    

input("Press Enter to End")