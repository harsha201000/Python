import pygame
import sys

pygame.display.set_caption("Car Game")

car_icon = pygame.image.load("icons8-car-48.png")
pygame.display.set_icon(car_icon)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.car = pygame.image.load('car.png')
        self.image = self.car
        self.rect = self.image.get_rect(center = (640,360))
        self.angle = 0
        self.rotation_speed = 1.0
        self.direction = 0
        self.forward = pygame.math.Vector2(0,-1)
        self.active = False
        
    def set_rotation(self):
        if self.direction == 1:
            self.angle -= self.rotation_speed
        if self.direction == -1:
            self.angle += self.rotation_speed
        
        self.image = pygame.transform.rotozoom(self.car, self.angle,0.25)
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def get_rotation(self):
        if self.direction == 1:
            self.forward.rotate_ip(self.rotation_speed)
        if self.direction == -1:
            self.forward.rotate_ip(-self.rotation_speed)
            
    def accelerate(self):
        if self.active:
            self.rect.center += self.forward * 5
            
    def update(self):
        self.set_rotation()
        self.get_rotation()
        self.accelerate()
        
        
pygame.init()       
window = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
bg_racetrack = pygame.image.load('race_track.png')
car = pygame.sprite.GroupSingle(Car())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                car.sprite.direction += 1
            if event.key == pygame.K_LEFT: 
                car.sprite.direction -= 1
            if event.key == pygame.K_SPACE: 
                car.sprite.active = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: 
                car.sprite.direction -= 1
            if event.key == pygame.K_LEFT: 
                car.sprite.direction += 1
            if event.key == pygame.K_SPACE: 
                car.sprite.active = False
            
    window.blit(bg_racetrack,(0,0))
    car.draw(window)
    car.update()
    pygame.display.update()
    clock.tick(120)