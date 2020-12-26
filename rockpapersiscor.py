import random
print ("Welcome to this game")
p = int (input ("Input your pin"))
if p == 12345 :
    print ("Lets start")
    num = random.randint(1, 3)
    if num == 1:
        suit = "rock"
    if num == 2:
        suit = "paper"
    if num == 3:
        suit = "siscor"
    a = int(input("Input your move, 1 for rock, 2 for paper, 3 for siscor"))
    if a == 1:
        if num == 1:
            print("Equivalent")
        if num == 2:
            print("You lost, computer", suit)
        if num == 3:
            print("You win, computer", suit)
    if a == 2:
        if num == 1:
            print("You win, computer", suit)
        if num == 2:
            print("Equivalent")
        if num == 3:
            print("You lost, computer", suit)
    if a == 3:
        if num == 1:
            print("You lost, computer", suit)
        if num == 2:
            print("You win, computer", suit)
        if num == 3:
            print("Equivalent")
    b = str(input("Wanna play again?(yes/no)"))
    while (b=="yes"):
        print("Lets start")
        num = random.randint(1, 3)
        if num == 1:
            suit = "rock"
        if num == 2:
            suit = "paper"
        if num == 3:
            suit = "siscor"
        a = int(input("Input your move, 1 for rock, 2 for paper, 3 for siscor"))
        if a == 1:
            if num == 1:
                print("Equivalent")
            if num == 2:
                print("You lost, computer", suit)
            if num == 3:
                print("You win, computer", suit)
        if a == 2:
            if num == 1:
                print("You win, computer", suit)
            if num == 2:
                print("Equivalent")
            if num == 3:
                print("You lost, computer", suit)
        if a == 3:
            if num == 1:
                print("You lost, computer", suit)
            if num == 2:
                print("You win, computer", suit)
            if num == 3:
                print("Equivalent")
        b = str(input("Wanna play again?(yes/no)"))
else : print ("Sorry, wrong pin")