import pygame
from pygame import mixer
import time
import random
import winsound
pygame.font.init()

WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

#Set icon photo
icon = pygame.image.load("starfall_arcade_game.png")
pygame.display.set_icon(icon)

bg_pic = pygame.transform.scale(pygame.image.load("background.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 70

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comisans", 30)

def draw(player, elapsed_time, stars):
    WINDOW.blit(bg_pic, (0, 0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10,10))
    
    pygame.draw.rect(WINDOW, "green", player)
    
    for star in stars:
        pygame.draw.rect(WINDOW, "white", star)
    
    pygame.display.update()

def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    
    mixer.init()
    mixer.music.load('summer_music.ogg')
    mixer.music.play()
    
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(5):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                
            star_add_increment = max(200, star_add_increment - 50)    
            star_count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mixer.music.stop()
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
            
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
            
        if hit:
            lost_text = FONT.render("YOU LOST!", 1, "red")
            WINDOW.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.mixer.music.stop()
            winsound.PlaySound("lose.wav",winsound.SND_ASYNC)
            pygame.time.delay(4000)
            break
            
        draw(player, elapsed_time, stars)
            
    pygame.quit()
    
if __name__ == "__main__":
    main()