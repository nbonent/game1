import pygame
import math
from actor_script import actor
from item_script import weapon, weapon_list

main_screen = pygame.display.set_mode((500,500)) #размер экрана

actor_1 = actor(color = (0,255,0), x=0, y=400)
actor_enemy = actor(x=400, y=400)
weapon_1 = weapon(x=200,y=480, size=(50,15))

button_skill_1 = pygame.Rect(100,400,50,50) #расположение и размер кнопки

stone = pygame.Rect(0,480,20,20) #расположение и размер камня

deltax=0
deltay=0
flag_stone_throw= False
t=0

while True:
    pygame.time.delay(40)
    main_screen.fill((30, 130, 255))

    actor_1.rendering(rendering_surf=main_screen) #рендеринг на мейн экране
    actor_enemy.rendering(rendering_surf=main_screen)
    weapon_1.rendering(rendering_surf=main_screen)

    pygame.draw.rect(main_screen, color = (255,0,0), rect = button_skill_1) #цвет кнопки
    pygame.draw.rect(main_screen, color=(155,110,180),rect=stone) #цвет камня


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #ДВИЖЕНИЕ ПО КЛАВИШАМ
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                deltax = 20
            elif event.key == pygame.K_LEFT:
                deltax = -20
            if event.key == pygame.K_UP:
                deltay = -20
            elif event.key == pygame.K_DOWN:
                deltay = 20

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                deltax = 0
            elif event.key == pygame.K_LEFT:
                deltax = 0
            if event.key == pygame.K_UP:
                deltay = 0
            elif event.key == pygame.K_DOWN:
                deltay = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_skill_1.collidepoint(event.pos):
                flag_stone_throw = True

        #формула движения камня
    if flag_stone_throw:
        stone.x = 100*t*math.cos(math.radians(45))
        stone.y = 480-(50*t*math.sin(math.radians(45))-(9.81*t**2)/2)
        t+=1
    if stone.y > 480:
        stone.x=0
        stone.y = 480
        flag_stone_throw = False
        t=0

    actor_enemy.get_hit(projectile=stone)
    actor_1.take_item(item_list=weapon_list)

    actor_1.actor_body.x += deltax
    actor_1.actor_body.y += deltay

    pygame.display.update()
