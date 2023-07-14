import random

start_number = int(input("Enter starting number: "))
end_number = int(input("Enter end number: "))
value = random.randint(start_number, end_number)

for i in range(0, 5):
    guess = int(input("Enter a number: "))
    if guess == value:
        print("Congratulations, You Win!")
        break
    elif guess > value:
        print("{} is high!".format(guess))
    elif guess < value:
        print("{} is low!".format(guess))
