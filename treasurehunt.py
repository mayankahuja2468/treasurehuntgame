print("Welcome to treasure island")
print("Your mission is to find the treasure")

d1 = input("Your at a cross road where do you want to go? Type left or right\n")

if d1=="left":
    d2=input("You have come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across\n")
    if d2=="wait":
        d3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and blue. Which colour do you choose ?\n")
        if d3=="yellow":
            print("You found the treasure\n")
        elif d3=="red":
            print("It is a room full of fire game over\n")
        elif d3=="blue":
            print("It is a room full of beasts game over\n")
    elif d2=="swim":
        print("You are eaten by a shark. Game Over!\n")
elif d1=="right":
    print("You fell in a hole game over\n")

    

