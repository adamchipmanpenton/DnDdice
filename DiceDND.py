import random

print("Enter how many of each die.")
print()

reroll = "y"
while reroll.lower() == "y":

    d100number = []
    d20number = []
    d10number = []
    d8number = []
    d6number = []
    d4number = []
    
    amountd100 = int(input("How many d100:\t"))
    amountd20 = int(input("How many d20:\t"))
    amountd10 = int(input("How many d10:\t"))
    amountd8 = int(input("How many d8:\t"))
    amountd6 = int(input("How many d6:\t"))
    amountd4 = int(input("How many d4:\t"))
    bonus = int(input("Bonus:\t\t"))
    print()

    for i in range(amountd100):
        randomd100 = random.randint(1, 100)
        d20number.append(randomd100)

    print("d100 dice rolls:", d100number)
    totald100 = sum(d100number)
    print("Total d100:\t", totald100)
    print()


    for i in range(amountd20):
        randomd20 = random.randint(1, 20)
        d20number.append(randomd20)

    print("d20 dice rolls:\t", d20number)
    totald20 = sum(d20number)
    print("Total d20:\t", totald20)
    print()

    for i in range(amountd10):
        randomd10 = random.randint(1, 10)
        d10number.append(randomd10)

    print("d10 dice rolls:\t", d10number)
    totald10 = sum(d10number)
    print("Total d10:\t", totald10)
    print()

    for i in range(amountd8):
        randomd8 = random.randint(1, 8)
        d8number.append(randomd8)

    print("d8 dice rolls:\t", d8number)
    totald8 = sum(d8number)
    print("Total d8:\t", totald8)
    print()

    for i in range(amountd6):
        randomd6 = random.randint(1, 6)
        d6number.append(randomd6)

    print("d6 dice rolls:\t", d6number)
    totald6 = sum(d6number)
    print("Total d6:\t", totald6)
    print()

    for i in range(amountd4):
        randomd4 = random.randint(1, 4)
        d6number.append(randomd4)

    print("d4 dice rolls:\t", d4number)
    totald4 = sum(d4number)
    print("Total d4:\t", totald4)
    print()

    total = totald20 + totald10 + totald8 + totald6 + totald4 + bonus
    print("Combined total:\t", total)
    print()
    

    reroll = input("Do you wish to reroll? (y/n): ")
    print()
print()
print("Good Luck!!")


    
