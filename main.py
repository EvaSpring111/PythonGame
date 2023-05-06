import random
import pygame

from pygame.constants import QUIT, K_DOWN, K_RIGHT, K_UP, K_LEFT

pygame.init()

HEIGHT = 600
WIDTH = 1100
FONT = pygame.font.SysFont('freesansbold.ttf', 40)

#I chose this color deliberately
COLOR_PINK = (255, 0, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
PLAYER_SIZE = (20, 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.image.load('player.png').convert_alpha() #pygame.Surface(PLAYER_SIZE)

player_rect = pygame.Rect(55, 45, *PLAYER_SIZE)
score = 0

bg = pygame.transform.scale(pygame.image.load('./img/background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

def create_enemy():
    ENEMY_SIZE = (50, 40)
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(WIDTH, random.randint(70, 500), *ENEMY_SIZE)
    enemy_move = [random.randint(-8, -4), 0]
    return  [enemy, enemy_rect, enemy_move ]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1000)

enemies = []

def create_bonuses():
    BONUSES_SIZE = (35, 55)
    bonus = pygame.image.load('bonus.png').convert_alpha()
    
    bonus_rect = pygame.Rect(random.randint(40, 900), 0,  *BONUSES_SIZE)
    bonus_move = [0, random.randint(4, 8)]
    return [ bonus, bonus_rect, bonus_move]

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

bonuses = []
    
FPS = pygame.time.Clock()

player_move_down = [0, 4]
player_move_right = [4, 0]
player_move_up = [0, -4]
player_move_left = [-4, 0]

playing = True

while playing:
    FPS.tick(240)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonuses())    
            
    # main_display.fill(COLOR_BLACK)  
    bg_X1 -= bg_move
    bg_X2 -= bg_move  
    
    if bg_X1 < - bg.get_width():
        bg_X1 = bg.get_height()
        
    if bg_X2 < - bg.get_width():
        bg_X2 = bg.get_height()    
    
    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))
    
    keys = pygame.key.get_pressed()
    
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
        
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)
    
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)
        
    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left) 
        
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])    
        main_display.blit(enemy[0], enemy[1])
        
        if player_rect.colliderect(enemy[1]):
            playing = False
     
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])   
        main_display.blit(bonus[0], bonus[1])
        
        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))
                                            
    main_display.blit(player, player_rect)  
    main_display.blit(FONT.render(str(score), True, COLOR_PINK), (WIDTH-50, 20))
            
    pygame.display.flip()
    
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
    print(len(enemies))        
    
    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
    print(len(bonuses))        










    # player_rect = player_rect.move(player_speed)    

    # if player_rect.bottom >= HEIGHT:
    #     player_speed = random.choice(([-1, -1], [1, -1] ))
        
    # if player_rect.right >= WIDTH :
    #     player_speed = random.choice(([-1, -1], [-1, 1] ))
         
    # if player_rect.left <= 0 :
    #     player_speed = random.choice(([1, -1], [1, -1]))
        
    # if player_rect.top <= 0 :
    #     player_speed = random.choice(([-1, 1], [1, 1] ))
    
    # if player_rect.bottom >= HEIGHT and player_rect.left < 550:
    #     player_speed = [-1, -1]   
