import random


num = 0
def oyeah(idk):
    num = random.randrange(1, 105)
    
    
    if num<20:
        print("Hey, I like shorts")
    elif num<10:
        print("DO A BARREL ROLL")
    elif num<15:
        print("Science isnt about why, its about why not!")
    elif num<35:
        print("What is a man? A miserable little pile of secrets.")
    else:
        print("I used to be an adventurer like you. Then I took an arrow in the knee...")


choice = 'a'
while choice !='q':
    print("press any number! (on your keyboard)")
    choice = input()
    if choice != 'q':
        oyeah(int(choice))
