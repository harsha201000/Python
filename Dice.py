dice = 1,2,3,4,5,6
import random
x= random.choice(dice)
print(x)

dice2 = 1,2,3,4,5,6
y= random.choice(dice2)
print(y)

if (x+y)==10:
    print("You Win!")
else:
    print("You Lose!")