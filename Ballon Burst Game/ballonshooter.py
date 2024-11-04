import pygame
import random
import sys
from math import *
import winsound

# setup pygame window
pygame.init()
width = 700
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ballon Shooter Game")
clock = pygame.time.Clock()

# image
ballon_logo = pygame.image.load('ballon.png')
pygame.display.set_icon(ballon_logo)

margin = 100
lowerBound = 100
score = 0

# colors
white = (230, 230, 230)
lightblue = (4, 27, 96)
red = (231, 76, 60)
lightgreen = (25, 111, 61)
darkgray = (40, 55, 71)
darkblue = (64, 178, 239)
green = (35, 155, 86)
yellow = (244, 208, 63)
blue = (46, 134, 193)
purple = (155, 89, 182)
orange = (243, 156, 18)

# font
font = pygame.font.SysFont("Snap ITC", 35)

# Ballon class
class Ballon:
    def __init__(self, speed):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed = -speed
        self.propool= [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([red, green, purple, orange, yellow, blue])
        
    def move(self):
        direct = random.choice(self.propool)
        
        if direct == -1:
            self.angle += -10
        elif direct == 0:
            self.angle += 0
        else:
            self.angle += 10
            
        self.y += self.speed*sin(radians(self.angle))
        self.x += self.speed*cos(radians(self.angle))
        
        if (self.x + self.a > width) or (self.x < 0):
            if self.y > height/5:
                self.x -= self.speed*cos(radians(self.angle))
            else:
                self.reset()
                
        if self.y + self.b < 0 or self.y > height + 30:
            self.reset()
            
            
    def show(self):
        pygame.draw.line(window, darkblue, (self.x + self.a/2, self.y + self.b), (self.x + self.a/2, self.y + self.b + self.length))
        pygame.draw.ellipse(window, self.color, (self.x, self.y, self.a, self.b))
        pygame.draw.ellipse(window, self.color, (self.x + self.a/2 - 5, self.y + self.b - 3, 10, 10))
        
    def pop(self):
        global score
        pos = pygame.mouse.get_pos()
        
        if isonBallon(self.x, self.y, self.a, self.b, pos):
            score += 1
            winsound.PlaySound("pop.wav",winsound.SND_ASYNC)
            self.reset()
            
    def reset(self):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed -= 0.002
        self.propool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([red, green, purple, orange, yellow, blue])
        
# Create a list of ballons and set the value
ballons = []
noballon = 10

# Insert ballons into list using for loop
for i in range(noballon):
    obj = Ballon(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4]))
    ballons.append(obj)
    
# Check the Ballons
def isonBallon(x, y, a, b, pos):
    if (x < pos[0] < x + a) and (y < pos[1] < y + b):
        return True
    else:
        return False
    
# Control cursor to pop ballon
def pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = red
    for i in range(noballon):
        if isonBallon(ballons[i].x, ballons[i].y, ballons[i].a, ballons[i].b, pos):
            color = red
    pygame.draw.ellipse(window, color, (pos[0] - r/2, pos[1] - r/2, r, r), 4)
    pygame.draw.line(window, color, (pos[0], pos[1] - l/2), (pos[0], pos[1] - l), 4)
    pygame.draw.line(window, color, (pos[0] + l/2, pos[1]), (pos[0] + l, pos[1]), 4)
    pygame.draw.line(window, color, (pos[0], pos[1] + l/2), (pos[0], pos[1] + l), 4)
    pygame.draw.line(window, color, (pos[0] - l/2, pos[1]), (pos[0] - l, pos[1]), 4)
    
# Create subplatform
def lowerplatform():
    pygame.draw.rect(window, darkgray, (0, height - lowerBound, width, lowerBound))
    
# Show score on screen
def show_score():
    score_text = font.render("Ballons Popped : " + str(score), True, white)
    window.blit(score_text, (150, height - lowerBound + 50))
    
# Create function to close the game
def close():
    pygame.quit()
    sys.exit()
    
# Create main function
def game():
    global score
    loop = True
    
    pygame.mixer.init()
    pygame.mixer.music.load('ballon_game.mp3')
    pygame.mixer.music.play()
    
    while loop:
        
        for event in pygame.event.get():
            # End the game only when the close button is pressed
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                close()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_q:
                    pygame.mixer.music.stop()
                    close()
                if event.type == pygame.K_r:
                    score = 0
                    game()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(noballon):
                    ballons[i].pop()
                    
                    
        window.fill(white)
        
        for i in range(noballon):
            ballons[i].show()
            
        pointer()
        
        for i in range(noballon):
            ballons[i].move()
            
        lowerplatform()
        show_score()
        pygame.display.update()
        clock.tick(60)
        
game()
    