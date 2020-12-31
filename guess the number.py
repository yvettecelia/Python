import random
heart = 100
repeat = 1
num = random.randint(1, 100)
print("Welcome to this game, you start with ", heart, " hearts")
a = int(input("Please guess a number "))
while (1):
    if a < num:
        heart -= 10
        print("Sorry, you guessed it wrong, ", heart, " hearts left")
        a = int(input("Please think another grater number "))
    elif a > num:
        heart -= 10
        print("Sorry, you guessed it wrong, ", heart, " hearts left")
        a = int(input("Please think another smaller number "))
    if a == num:
        print("Congratulation, your score is, ", heart)
        break
    if heart == 0:
        print("Game over")
        break
ans = input("Do you want to play the next round? ")
while (ans=="yes"):
    heart = 100
    repeat+=1
    player = input("Please enter your name")
    name = [""]
    name.append(player)
    num = random.randint(1, 100)
    a = int(input("Please guess a number "))
    while (1):
        if a < num:
            heart -= 10
            print("Sorry, you guessed it wrong, ", heart, " hearts left")
            a = int(input("Please think another grater number "))
        elif a > num:
            heart -= 10
            print("Sorry, you guessed it wrong, ", heart, " hearts left")
            a = int(input("Please think another smaller number "))
        if a == num:
            print("Congratulation, your score is, ", heart)
            break
        if heart == 0:
            print("Game over")
            break
    ans = input("Do you want to play the next round? ")
for a in range (0,repeat):
    c=heart
    if heart>c:
        c=heart
print("Highest score is ", c)