import pygame

screen_size = [360,600]
screen = pygame.display.set_mode(screen_size)

background_image = pygame.image.load('Game Resource/background.png')
spaceship = pygame.image.load('Game Resource/spaceship.png')
bullet = pygame.image.load('Game Resource/bullet.png')
bullet_y = 500
fired = False

planets = ('Game Resource/one.png', 'Game Resource/two.png', 'Game Resource/three.png')
p_index = 0
planet = pygame.image.load(planets[p_index])
planet_x = 140
move_direction = 'right'

keep_alive = True
clock = pygame.time.Clock()

while keep_alive:
    # Do game stuff here .
    screen.blit(background_image,[0,0])
    screen.blit(bullet,[180, bullet_y])
    screen.blit(spaceship,[160,500])

    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True:
        fired = True

    if fired is True:
        bullet_y = bullet_y - 5
        if bullet_y == 50:
            fired = False
            bullet_y = 500

    if move_direction == 'right':
        planet_x = planet_x + 5
        if planet_x == 300:
            move_direction = 'left'
    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = 'right'

    screen.blit(planet,[planet_x,50])

    if bullet_y <80 and planet_x > 120 and planet_x < 180:
        p_index = p_index + 1
        if p_index < len(planets):
            planet = pygame.image.load(planets[p_index])
            planet_x = 10
        else:
            print('YOU WIN')
            keep_alive = False

    
    pygame.display.update()
    clock.tick(60)
    
    

    

# 4 things you have to do to display something on screen
    #1. Create a loop variable.
    #2. Create the never ending while loop (game loop).
    #3. Set the image on screen .
    #4. Tell pygame to update the display .


# To access event in pygame, call get_pressed function on pygame.keys .
# This will return a list of all the keys, every key will be False.
# Only the button user pressed will be True.
