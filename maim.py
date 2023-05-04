import pygame

from pygame.constants import QUIT

pygame.init()

HEIGHT = 600
WIDTH = 1100
# HALF_W = 550

#I chose this color deliberately
COLOR_PINK = (255, 0, 255)
COLOR_BLACK = (0, 0, 0)
PLAYER_SIZE = 20, 20

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface((PLAYER_SIZE))
player.fill(COLOR_PINK)

player_rect = player.get_rect()
player_speed = [1, 1]
FPS = pygame.time.Clock()

playing = True

while playing:
    FPS.tick(240)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
            
    if player_rect.bottom >= HEIGHT:
        player_speed = [1, -1] 
        
    if player_rect.right >= WIDTH :
        player_speed = [-1, -1] 
         
    if player_rect.left <= 0 :
        player_speed = [1, 1] 
        
    if player_rect.top <= 0 :
        player_speed = [-1, 1]   
    
    if player_rect.bottom >= HEIGHT and player_rect.left < 450:
        player_speed = [-1, -1]   
    
    # if player_rect.left < 1 and player_rect.top < 300:
    #     player_speed = [1, -1]    
           
 
                  
    main_display.fill(COLOR_BLACK) 
    print(player_rect.bottom)   
    
    main_display.blit(player, player_rect)   
        
    player_rect = player_rect.move(player_speed)    
    
    pygame.display.flip()
    