import pygame
import sys
from random import randint

pygame.init()

size = width, height = 640, 640
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

black = 0, 0, 0


class Animal(pygame.sprite.Sprite):
    def __init__(self, image, action='walk', direction='north', x=0, y=0):
        super().__init__()
        self.png = 1
        self.image_base = image
        self.action = action
        self.direction = direction
        self.image = pygame.image.load(f'{self.image_base}{self.action}{self.direction}{self.png}.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.up = True
        self.loop_end = False
        self.pick_action = 0

    def update(self):
        self.counter += 1
        if self.counter == 5 and self.loop_end:
            if self.pick_action == 1:
                self.pick_direction()
            elif self.pick_action == 2:
                self.eat()
            elif self.pick_action == 3:
                self.loop_end = False
                self.png = 1
            self.counter = 0
        elif self.counter == 5 and self.png != 4 and self.up:
            self.png += 1
            self.counter = 0
            self.movement()
        elif self.counter == 5 and self.png == 4:
            self.png -= 1
            self.up = False
            self.counter = 0
            self.movement()
        elif self.counter == 5 and self.png != 1:
            self.png -= 1
            self.counter = 0
            self.movement()
        elif self.counter == 5 and self.png == 1:
            self.png = 1
            self.counter = 0
            self.up = True
            self.loop_end = True
            self.movement()
            self.pick_action = randint(1, 3)
        positionx = self.rect.x
        positiony = self.rect.y
        self.image = pygame.image.load(f'{self.image_base}{self.action}{self.direction}{self.png}.png')
        self.rect = self.image.get_rect()
        self.rect.x = positionx
        self.rect.y = positiony

    def pick_direction(self):
        if randint(0, 9) % 2 != 0:
            pick = randint(0, 3)
            directions = ['north', 'south', 'east', 'west']
            self.direction = directions[pick]
        self.loop_end = False
        self.png = 1

    def movement(self):
        self.action = 'walk'
        if self.direction == 'north':
            self.rect.y -= 3
        if self.direction == 'south':
            self.rect.y += 3
        if self.direction == 'east':
            self.rect.x += 3
        if self.direction == 'west':
            self.rect.x -= 3

    def eat(self):
        self.action = 'eat'
        if self.counter == 5 and self.png != 4 and self.up:
            self.png += 1
            self.counter = 0
        elif self.counter == 5 and self.png == 4:
            self.png -= 1
            self.up = False
            self.counter = 0
        elif self.counter == 5 and self.png != 1:
            self.png -= 1
            self.counter = 0
        elif self.counter == 5 and self.png == 1:
            self.png = 1
            self.counter = 0
            self.loop_end = False


animal_group = pygame.sprite.Group()
