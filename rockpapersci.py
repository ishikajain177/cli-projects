import os
import time
import random as rd

def play_game(pts):
    pc_pts=0
    user_pts=0
    rps=["rock","paper","scissor"]
    while pc_pts!=pts and user_pts!=pts:
        print("\n")
        user_choice=input("rock paper scissor :: ").lower()
        comp_choice=rd.choice(rps)
        print("Computer played :: ",comp_choice)
        if user_choice==comp_choice:
            print("Its a DRAW!!!")
        elif user_choice=="rock" and comp_choice=="scissor":
            user_pts+=1
            print("YOU WON!! ",user_pts," points")
        elif user_choice=="paper" and comp_choice=="rock":
            user_pts+=1
            print("YOU WON!! ",user_pts," points")
        elif user_choice=="scissor" and comp_choice=="paper":
            user_pts+=1
            print("YOU WON!! ",user_pts," points")
        else:
            pc_pts+=1
            print("COMPUTER WON!! ",pc_pts," points")
    print("\n")
    if pc_pts==pts:
        print("!!!COMPUTER WON THE GAME!!!")
    else:
        print("!!!YOU WON THE GAME!!!")

def main():
        while(True):
            print("\t\tTHE ROCK PAPER SCISSOR GAME")
            print("\n1. Play Game")
            print("2. Exit")
            choice=input("Enter your choice: ")
            if choice=="1":
                pts=int(input("How many points game you wish to play: "))
                play_game(pts)
            elif choice=="2":
                print("Exiting the game") 
                exit(0)
            else:
                print("!!! Enter valid choice !!!") 
            time.sleep(2)
            os.system('clear')

if __name__ == "__main__":
    main()
