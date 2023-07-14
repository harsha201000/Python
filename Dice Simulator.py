import random
min = 1
max = 6

roll_again = "yes"

#while roll_again == "yes" or roll_again == "y":
    #print("Rolling the dices")
    #print("The values are...")
    #print(random.randint(min, max))
    #print(random.randint(min, max))

    #roll_again = input("Roll the dices again?")

while 1 == 1:
    print("Rolling the dices")
    print("The values are...")
    print(random.randint(1, 6))
    print(random.randint(1, 6))
        
    roll_again = input("Roll the dices again?")
    if roll_again == "n" or roll_again == "no":
        break
