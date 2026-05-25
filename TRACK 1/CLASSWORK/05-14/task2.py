import random

l=["rock","paper","scissor"]


while True:
    com=random.choice(l)
    print("""
Press 1 for Playing
press 2 for Quitting
""")
    choice=int(input("Enter your  choice: "))
    if choice==1:
        print("""
Press 1 for Rock
Press 2 for Paper
Press 3 for Scissor
""")
        num=int(input("Enter your choice: "))
        if num==1:
            if com=="paper":
                print(f"You lost,computer chose {com}")
            elif com=="rock":
                print(f"Its a tie,com chose {com} too")
            else:
                print(f"You won,com chose {com}")
        elif num==2:
            if com=="scissor":
                print(f"You lost,com chose {com}")
            elif com=="paper":
                print(f"Its a tie,com chose {com} too")
            else:
                print(f"You won,com chose {com}")
        elif num==3:
            if com=="rock":
                print(f"You lost,com chose {com}")
            elif com=="scissor":
                print(f"Its a tie,com chose {com} too")
            else:
                print(f"You won,com chose {com}")
        else:
            print("Invalid choice!!")
            break
             
    else:
        print("Exiting!!")
        break