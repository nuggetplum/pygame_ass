import pygame
from player import *
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *
import sys
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clk= pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers=(shots,drawable,updatable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)


    player= Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2,20)
    dt =0
    loop=1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collides_with(player):
                 print("Game over!")
                 sys.exit()

            for shot in shots:
                if obj.collides_with(shot):
                    shot.kill()
                    obj.split()



        #player.update(dt)
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        #player.draw(screen)
        pygame.display.flip()
        dt = clk.tick(60)/1000
       
        

if __name__ == "__main__":
    main()
