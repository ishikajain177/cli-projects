import os
import time
def addTask():
    print("\n------------LET`S ADD SOME NEW TASKS---------------\n")
    task=input("Enter new task to add\n").capitalize()
    toDoList.append(task)
    print("\n------------ADDED NEW TASK--------------n")

def viewTask():
    if not toDoList:
        print("\n-----------NO TASK TO VIEW----------\n")
    else:
        print("\n------------LETS SEE YOUR TO-DO LIST ---------------\n")
        for task in toDoList:
             print("->",task)

def deleteTask():
    print("\n------------LET`S DELETE SOME NEW TASKS---------------\n")
    info=input("\nDo you wish to delete all tasks (yes/no):").lower()
    if info=="yes":
        toDoList.clear()
    else:
        viewTask()
        task=input("\nEnter task to delete\n").capitalize()
        toDoList.remove(task)

def main():
    while(1):
        print("\n1.VIEW")
        print("\n2.ADD")
        print("\n3.DELETE")
        print("\n4.EXIT")
        choice=int(input("\nEnter action to perform:: "))
        os.system('clear')
        match choice:
            case 1: viewTask()
            case 2: addTask()
            case 3: deleteTask()
            case 4: exit(0)
            case _: print("please enter valid choice")
        time.sleep(1)
        os.system('clear')

if __name__ == "__main__":
    toDoList=[]
    main()
    