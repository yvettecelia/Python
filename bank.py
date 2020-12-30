namem = ["Fred","Tom"]
pinm = [234567, 345678]
moneym = [20000, 30000]
def data ():
    a = input("What is your name? ")
    f = int(input("Make your 6 digit pin "))
    v = int(input("How much money you want to save? "))
    namem.append(a)
    pinm.append(f)
    moneym.append(v)
def findp(pin):
    e=0
    for k in pinm:
        if k==pin:
            y=k
            break
        e+=1
    return(e)
def findn(name):
    e=0
    for k in namem:
        if k==name:
            y=k
            break
        e+=1
    return(e)
def trans(name, pin):
    e = findn(name)
    f = findp(pin)
    if e == f:
        c = int(input("Please enter destination pin "))
        d = int(input("Please enter the nominal "))
        h = findp(c)
        if d < moneym[f]:
            moneym[f] -= d
            moneym[h] += d
        else:
            print("Sorry, you're out of money ")
    else:
        print("Sorry your pin is wrong ")
def check(name):
    d = findp(name)
    print (namem[d]," ",pinm[d], " ",moneym[d])
def add(name,pin, nom):
    a = findn(name)
    b = findp(pin)
    if a==b:
        moneym[a] += nom
    else:
        print("Sorry, wrong pin")
def take(name,pin,nom):
    a = findn(name)
    b = findp(pin)
    if a == b:
        if moneym[a]>=nom:
            moneym[a] -= nom
        else:
            print("Sorry, you're out of money")
    else:
        print("Sorry, wrong pin")
def do():
    print("Menu :\n1. Register new membership\n2. Transfer\n3. Check data\n4. Save money\n5. Take money")
    b = int(input("Please choose the menu "))
    if b == 1:
        data()
    elif b == 2:
        a = str(input("Please enter your name "))
        b = int(input("Please enter your pin "))
        trans(a,b)
    elif b == 3:
        a = int(input("Please enter your pin "))
        check(a)
    elif b == 4:
        c = str(input("Please enter your name "))
        a = int(input("Please enter your pin "))
        b = int(input("How much money you want to save? "))
        add(c, a, b)
    elif b == 5:
        c = str(input("Please enter your name "))
        a = int(input("Please enter your pin "))
        b = int(input("How much money you want to take? "))
        take(c, a, b)
    else:
        print("Sorry, wromg input ")
    c = str(input("Do you want to do another transaction "))
print("Welcome")
do()
while (c.lower()=="yes"):
    do()