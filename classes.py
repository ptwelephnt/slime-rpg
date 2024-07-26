import pygame
from utils import boundary_top, boundary_left, boundary_bottom, boundary_right
from tavern import battle_characters
import time

size = width, height = 640, 640
screen = pygame.display.set_mode(size)

w, h = pygame.display.get_window_size()


def narrate(text):
    bar = pygame.image.load('images/battle/NarrateBar.png')
    image_sprite = pygame.sprite.Sprite()
    image_sprite.image = bar
    image_sprite.rect = bar.get_rect()
    image_sprite.rect.x = 0
    image_sprite.rect.y = 20

    text_font = pygame.font.Font('freesansbold.ttf', 15)
    text_surface = text_font.render(text, True, [255, 255, 255])
    text_sprite = pygame.sprite.Sprite()
    text_sprite.image = text_surface
    text_sprite.rect = text_surface.get_rect()
    text_sprite.rect.x = 10
    text_sprite.rect.y = 25

    sprite_group = pygame.sprite.Group()
    sprite_group.add(image_sprite, text_sprite)

    return sprite_group


class Background:
    def __init__(self, image, x=0, y=0):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        screen.blit(self.image, self.rect)


class Character:
    def __init__(self, image, action, png=1, direction='north', x=0, y=0):
        super().__init__()
        self.png = png
        self.direction = direction
        self.imagesource = image
        self.action = action
        self.image = pygame.image.load(f'{self.imagesource}{self.action}{self.direction}{str(self.png)}.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = x, y
        self.move = 0
        self.bot = self.rect.bottom
        self.top = self.rect.top
        self.right = self.rect.x + 32
        self.left = self.rect.left

    def show(self):
        screen.blit(self.image, self.rect)

    def walk_animate(self, new_direction):
        if self.direction != new_direction:
            self.direction = new_direction
            self.png = 1
        else:
            self.png += 1
        self.image = pygame.image.load(f'{self.imagesource}{self.action}{self.direction}{str(self.png)}.png')
        if self.png == 9:
            self.png = 1

    def step_counter(self, direction):
        self.move += 1
        if self.move == 5:
            self.move = 0
            self.walk_animate(direction)

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.right < width:
                    self.rect.x += 3
                    self.right = self.rect.right
                    self.left = self.rect.left
                    self.step_counter('east')
                    return True
                if event.key == pygame.K_LEFT and self.left > 0:
                    self.rect.x -= 3
                    self.right = self.rect.right
                    self.left = self.rect.left
                    self.step_counter('west')
                    return True
                if event.key == pygame.K_DOWN and self.bot < height:
                    self.rect.y += 3
                    self.top = self.rect.top
                    self.bot = self.rect.bottom
                    self.step_counter('south')
                    return True
                if event.key == pygame.K_UP and self.top > 0:
                    self.rect.y -= 20
                    self.top = self.rect.top
                    self.bot = self.rect.bottom
                    self.step_counter('north')
                    return True

    def change_direction(self, direction, action='walk'):
        self.action = action
        self.direction = direction
        self.png = 1
        self.image = pygame.image.load(f'{self.imagesource}{self.action}{self.direction}{str(self.png)}.png')

    def collides_with_right(self, objects):
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                if self.right > obj.left and self.bot > obj.top and self.top < obj.bot:
                    return True
        return False

    def collides_with_left(self, objects):
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                if self.left < obj.right and self.bot > obj.top and self.top < obj.bot:
                    return True
        return False

    def collides_with_top(self, objects):
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                if self.top < obj.bot and self.right > obj.left and self.left < obj.right:
                    return True
        return False

    def collides_with_bot(self, objects):
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                if self.bot > obj.top and self.right > obj.left and self.left < obj.right:
                    return True
        return False


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, ):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.top = self.rect.top
        self.bot = self.rect.bottom
        self.left = self.rect.left
        self.right = self.rect.right


class NPC(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bot = self.rect.bottom
        self.top = self.rect.top
        self.right = self.rect.right
        self.left = self.rect.left


class AnimatedObj(pygame.sprite.Sprite):
    def __init__(self, path, image, max_png, rate, x=0, y=0, straight=False):
        super().__init__()
        self.png = 1
        self.path = path
        self.image_base = image
        self.max_png = max_png
        self.rate = rate
        self.image = pygame.image.load(f'{self.path}{self.image_base}{self.png}.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.up = True
        self.straight = straight

    def update(self):
        self.counter += 1
        if self.counter == self.rate and self.png != self.max_png and self.up:
            self.png += 1
            self.counter = 0
        elif self.counter == self.rate and self.png == self.max_png and self.straight:
            self.png = 1
            self.counter = 0
        elif self.counter == self.rate and self.png == self.max_png:
            self.png -= 1
            self.counter = 0
            self.up = False
        elif self.counter == self.rate and self.png != 1:
            self.png -= 1
            self.counter = 0
        elif self.counter == self.rate and self.png == 1:
            self.png += 1
            self.counter = 0
            self.up = True
        self.image = pygame.image.load(f'{self.path}{self.image_base}{self.png}.png')


class BattleGroup(pygame.sprite.Sprite, Character):
    def __init__(self, name, imagesource, character, action, direction, x, y, max_hp, hp, max_mp, mp, strength, defense,
                 agility, level):
        super().__init__()
        self.name = name
        self.imagesource = imagesource
        self.character = character
        self.action = action
        self.direction = direction
        self.png = 1
        self.image = pygame.image.load(
            f'{self.imagesource}{self.character}{self.action}{self.direction}{str(self.png)}.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startx = x
        self.starty = y
        self.max_hp = max_hp
        self.hp = hp
        self.max_mp = max_mp
        self.mp = mp
        self.strength = strength
        self.defense = defense
        self.agility = agility
        self.speed = 0
        self.level = level
        self.exp = 0
        self.counter = 0
        self.move_counter = 0

    def level_up(self):
        self.level += 1
        self.exp -= 100
        self.max_hp += 10
        self.hp = self.max_hp
        self.max_mp += 5
        self.mp = self.max_mp
        self.strength += 2
        self.defense += 1
        battle_characters[self.name]['level'] = self.level
        battle_characters[self.name]['exp'] = self.exp
        battle_characters[self.name]['max hp'] = self.max_hp
        battle_characters[self.name]['hp'] = self.hp
        battle_characters[self.name]['max mp'] = self.max_mp
        battle_characters[self.name]['mp'] = self.mp
        battle_characters[self.name]['strength'] = self.strength
        battle_characters[self.name]['defense'] = self.defense

    def show_level_up(self):
        narrate_group = narrate(f"{self.name} has reached level {self.level}!")
        narrate_group.draw(screen)
        pygame.display.flip()
        time.sleep(1)

    def add_exp(self, exp):
        self.exp += exp
        if self.exp >= 100:
            self.level_up()
            self.show_level_up()

    def attack(self, enemy):
        damage = self.strength - enemy.defense
        if damage < 0:
            damage = 0
        enemy.hp -= damage
        return damage

    def move(self, x, y, enemy):
        enemyx, enemyy, enemyw, enemyh = enemy.rect
        clip_x = enemyx + enemyw / 4
        clip_y1 = enemyy
        clip_y2 = enemyy + enemyh
        difference_x = self.rect.x - x
        difference_y = self.rect.y - y
        self.rect.x -= difference_x / 12
        self.rect.y -= difference_y / 12
        if self.rect.collidepoint(enemy.rect.center) or self.rect.clipline(clip_x, clip_y1, clip_x, clip_y2):
            self.move_counter += 1
            if self.move_counter == 2:
                self.move_counter = 0
                self.rect.x = self.startx
                self.rect.y = self.starty
                self.png = 1
                enemy.killed()
                return True
            else:
                return False
        return False

    def attack_animate(self):
        self.counter += 1
        if self.counter == 2:
            if self.png != 6:
                self.png += 1
            self.counter = 0
        self.image = pygame.image.load(
            f'{self.imagesource}{self.character}{self.action}{self.direction}{str(self.png)}.png')

    def defend(self, character):
        self.hp -= (character.strength - self.defense)

    def turn(self):
        self.speed += self.agility
        if self.speed >= 100:
            self.speed = 0
            return True
        else:
            return False


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, image, x, y, health, mp, strength, defense):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = health
        self.max_mp = mp
        self.mp = self.max_mp
        self.strength = strength
        self.defense = defense
        self.exp = 100

    def killed(self):
        if self.hp <= 0:
            self.kill()

    def attack(self, character):
        character.health -= (self.strength - character.defense)

    def defend(self, character):
        self.hp -= (character.strength - self.defense)


class BattleMenu(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, hp, max_hp, x, y, h=14):
        super().__init__()
        self.width = 158 * hp / max_hp
        self.image = pygame.Surface((self.width, h))
        self.image.fill((0, 201, 13))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, current, max_hp):
        self.width = self.width = 158 * current / max_hp
