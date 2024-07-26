import random
import pygame
import math
from sceneloader import change_battle_menu
import time

pygame.init()

size = width, height = 640, 640
screen = pygame.display.set_mode(size)


def narrate(text):
    text_font = pygame.font.Font('freesansbold.ttf', 15)
    text_surface = text_font.render(text, True, [10, 201, 0])
    text_surfacerect = text_surface.get_rect()
    text_surfacerect.x = 10
    text_surfacerect.y = 20
    screen.blit(text_surface, text_surfacerect)
    pygame.display.flip()
    time.sleep(3)


class Selector:
    def __init__(self, x, y):
        self.image = pygame.image.load('Images/Battle/selector.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.orig_x = x
        self.orig_y = y
        self.measure = 0
        self.up = True
        self.angle = 0
        self.position = 0
        self.menu = 1

    def cursor_move(self, battle_group, menu_group, k_sprite, a_sprite, enemy_group, character):
        change = 0
        num_choices = 0
        if self.menu == 1:
            change = 40
            num_choices = 3
        elif self.menu == 2:
            change = 32
            num_choices = 4
        elif self.menu == 'attacking':
            num_choices = len(pygame.sprite.Group.sprites(enemy_group))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if type(self.menu) == int and event.key == pygame.K_UP:
                    if self.position != 0:
                        self.position -= 1
                        self.y -= change
                        return (self.x, self.y), False, False
                    else:
                        self.position = (num_choices - 1)
                        self.y += change * (num_choices - 1)
                        return (self.x, self.y), False, False
                elif event.key == pygame.K_DOWN:
                    if self.position != num_choices - 1:
                        self.position += 1
                        self.y += change
                        return (self.x, self.y), False, False
                    else:
                        self.position = 0
                        self.y -= change * (num_choices - 1)
                        return (self.x, self.y), False, False
                elif event.key == pygame.K_RIGHT and self.menu == 'attacking':
                    if self.position != num_choices - 1:
                        self.position += 1
                        return self.enemy_pos(enemy_group, 2), False, False
                    elif self.position == num_choices - 1:
                        self.position = 0
                        return self.enemy_pos(enemy_group, 2), False, False
                elif event.key == pygame.K_RETURN:
                    if self.position == 0 and self.menu != 'attacking':
                        # move selector to enemy1 position
                        self.menu = 'attacking'
                        self.image = pygame.transform.rotate(self.image, 270)
                        return self.enemy_pos(enemy_group, 2), False, False
                    elif self.menu == 'attacking':
                        enemies = pygame.sprite.Group.sprites(enemy_group)
                        enemy = enemies[self.position]
                        x, y = self.enemy_pos(enemy_group, enemy.rect.x)
                        character.move(x, y, enemy)
                        self.x, self.y = self.reset()
                        return (self.x, self.y), False, (x, y, enemy)
                    elif self.position == 1:
                        self.position = 0
                        self.y = 485
                        self.menu = 2
                        return (self.x, self.y), change_battle_menu(menu_group, k_sprite, a_sprite), False
                    elif self.position == 2:
                        # open item menu selector moves to item1 position
                        pass
                    elif self.position == 3:
                        self.position = 0
                        self.y = 492
                        self.menu = 1
                        return (self.x, self.y), change_battle_menu(menu_group, a_sprite, k_sprite), False
                    elif event.key == pygame.K_SPACE:
                        pass
                else:
                    return (self.x, self.y), False, False
            else:
                return (self.x, self.y), False, False
        return (self.x, self.y), False, False

    def enemy_pos(self, enemies, n):
        enemy_list = pygame.sprite.Group.sprites(enemies)
        enemy = enemy_list[self.position]
        self.x = enemy.rect.x + enemy.rect.width / n
        self.y = enemy.rect.y
        return self.x, self.y

    def floating(self, pos):
        self.rect.x = pos[0] + 2 * math.cos(self.angle)
        self.rect.y = pos[1] + .5 * math.sin(self.angle)
        self.angle += .1

    def reset(self):
        self.image = pygame.transform.rotate(self.image, -270)
        self.menu = 1
        self.position = 0
        return self.orig_x, self.orig_y

    def show(self):
        screen.blit(self.image, self.rect)


# Class for the player
class Player:
    def __init__(self, name, max_hp, max_mp, strength, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_mp = max_mp
        self.mp = max_mp
        self.strength = strength
        self.defense = defense
        self.level = 1
        self.exp = 0

    def attack(self, enemy):
        damage = self.strength - enemy.defense
        if damage < 0:
            damage = 0
        enemy.hp -= damage
        narrate(f"{self.name} attacked {enemy.name} and dealt {damage} damage!")
        pygame.display.flip()

        if enemy.hp <= 0:
            narrate(f"{enemy.name} has been defeated!")
            self.exp += enemy.exp
            if self.exp >= 100:
                self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= 100
        self.max_hp += 10
        self.hp = self.max_hp
        self.max_mp += 5
        self.mp = self.max_mp
        self.strength += 2
        self.defense += 1
        narrate(f"{self.name} has reached level {self.level}!")

    def health_bar(self, x, y):
        width = 158 * self.hp / self.max_hp
        bar = pygame.Surface((width, 14))
        bar.fill()
        bar.rect = bar.get_rect()
        bar.rect.x = x
        bar.rect.y = y
#         27, 31


# Class for enemies
class Enemy:
    def __init__(self, name, max_hp, strength, defense, exp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.defense = defense
        self.exp = exp

    def attack(self, player):
        damage = self.strength - player.defense
        if damage < 0:
            damage = 0
        player.hp -= damage
        narrate(f"{self.name} attacked {player.name} and dealt {damage} damage!")
        if player.hp <= 0:
            narrate(f"{player.name} has been defeated!")


# Class for NPCs
class NPC:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def talk(self):
        narrate(f"{self.name}: {self.message}")


# Class for items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, target):
        pass


# Subclass for healing items
class HealingItem(Item):
    def __init__(self, name, description, amount):
        super().__init__(name, description)
        self.amount = amount

    def use(self, target):
        if isinstance(target, Player):
            target.hp += self.amount
            if target.hp > target.max_hp:
                target.hp = target.max_hp
            narrate(f"{target.name} used {self.name} and restored {self.amount} HP!")
        else:
            narrate("Invalid target.")


# Subclass for damaging items
class DamagingItem(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def use(self, target):
        if isinstance(target, Enemy):
            target.hp -= self.damage
            narrate(f"{target.name} was damaged by {self.name} and lost {self.damage} HP!")
            if target.hp <= 0:
                narrate(f"{target.name} has been defeated!")
        else:
            narrate("Invalid target.")


class Battle:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def start(self):
        narrate("A battle has started!")
        while True:
            # Player turn
            narrate("Player's turn.")
            command = input("Enter 'a' to attack or 'm' to use magic: ")
            if command == "a":
                enemy = random.choice(self.enemies)
                self.player.attack(enemy)
                if self.check_win():
                    return
            elif command == "m":
                pass
            else:
                narrate("Invalid command.")
                continue

            # Enemies turn
            narrate("Enemies' turn.")
            for enemy in self.enemies:
                enemy.attack(self.player)
                if self.check_lose():
                    return

    def check_win(self):
        for enemy in self.enemies:
            if enemy.hp > 0:
                return False
        narrate("You have won the battle!")
        return True

    def check_lose(self):
        if self.player.hp <= 0:
            narrate("You have been defeated!")
            return True
        return False
