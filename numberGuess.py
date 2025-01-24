import os
import random as rd

def hint1(pc_num):
    last_dgt=int(str(pc_num)[-1])
    print("\nHINT 1 : \nThe number ends with :: ",last_dgt) 

def hint2(pc_num):
    sum=0
    for i in str(pc_num):
        sum+=int(i)
    print("\nHINT 2 : \nThe sum of digit of the number is:: ",sum) 

def hint3(pc_num,usr_num):
    if pc_num < usr_num:
        print("\nHINT 3 : \nThe number is less than what you gussed.")
    else:
        print("\nHINT 3 : \nThe number is greater than what you gussed.")

def check_num(usr_num,pc_num):
    for i in range(1,4):
        if usr_num==pc_num:
            print("HURRAY YOU GUESSED IT RIGHT")
            break
        elif i==1:
            hint2(pc_num)
            usr_num=int(input("enter the guessed number(100-999): "))
        elif i==2:
            hint3(pc_num,usr_num)
            usr_num=int(input("enter the guessed number(100-999): "))
        else:
            print("YOU LOST !! \nThe correct number was:",pc_num)
def main():
    ans=True
    while(ans):
        print("\t\t\t THE NUMBER GUESSING GAME")
        print("You have 3 chances. GOOD LUCK!")
        actual_num=rd.randint(100,999)
        hint1(actual_num)
        guess_num=int(input("enter the guessed number(100-999): "))
        check_num(guess_num,actual_num)
        cont=input("do you want to play another game(y/n): ").lower()
        if cont=="n":
            ans=False
        os.system('clear')

if __name__ == "__main__":
    main()