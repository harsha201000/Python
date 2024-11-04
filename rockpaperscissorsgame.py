import random

items = ["ROCK","PAPER","SCISSORS"];
print("Welcome to rock, paper, scissors game");
player = '';

while player not in items:
  player = input("Choose rock, paper, or scissors : ").upper();
  
print ("You chose",player);
computer = items[random.randint(0,2)];
print("Computer chooses",computer);

rules = {"ROCK":"SCISSORS","PAPER":"ROCK","SCISSORS":"PAPER"};

if player == computer:
  print("We drew");
elif rules[player] == computer:
  print("You won");
else:
  print("Computer wins");
