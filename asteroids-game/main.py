import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

drawable = pygame.sprite.Group()
updatable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Asteroid.containers = (asteroids,drawable,updatable)
AsteroidField.containers = (updatable)
asteroid_field = AsteroidField()

Player.containers = (drawable,updatable)
Shot.containers = (shots,drawable,updatable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

   
    
    player = Player(SCREEN_WIDTH/2 ,SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)
        
        for drawings in drawable:
            drawings.draw(screen)
        
        pygame.display.flip()

        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
        
        dt = clock.tick(60) / 1000
         
          
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()