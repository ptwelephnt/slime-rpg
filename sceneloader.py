import pdb
import pygame
import time
from classes import Character, Background, Obstacle, NPC, AnimatedObj, Enemy, BattleGroup, BattleMenu, HealthBar
from animals import Animal
from tavern import battle_characters, battle_menu, scenes
from slime import Slime


def fade_out(screen, background):
    x = 255
    while x > 3:
        screen.fill((0, 0, 0))
        background.image.set_alpha(x)
        background.show()
        x -= 4
        pygame.display.flip()
        time.sleep(.001)


def fade_in(screen, background):
    x = 0
    while x < 255:
        screen.fill((0, 0, 0))
        background.image.set_alpha(x)
        background.show()
        x += 4
        pygame.display.flip()
        time.sleep(.001)


def load_scene(scene):
    return Background(scene['background'])


def load_player(scene):
    image = scene['player']['image']
    action = scene['player']['action']
    png = scene['player']['png']
    direction = scene['player']['direction']
    x = scene['player']['x']
    y = scene['player']['y']
    return Character(image, action, png, direction,
                     x, y)


def load_obs(scene):
    obst_group = pygame.sprite.Group()
    line_list = []
    if scene['obstacles']:
        for each in scene['obstacles']:
            obstacle = Obstacle(each['image'], each['x'], each['y'])
            line = {each['boundaries']: {each['x'], each['y'], obstacle.rect.w, obstacle.rect.h}}
            line_list.append(line)
            obst_group.add(obstacle)
        return obst_group, line_list


def load_special(scene):
    special_group = pygame.sprite.Group()
    for each in scene['special']:
        special = Obstacle(each['image'], each['x'], each['y'])
        special_group.add(special)
    return special_group


def load_npcs(scene):
    npc_group = pygame.sprite.Group()
    for each in scene['NPCs']:
        npc = NPC(each['image'], each['x'], each['y'])
        npc_group.add(npc)
    return npc_group


def load_animated(scene):
    animated_group = pygame.sprite.Group()
    for each in scene['animated']:
        animated = AnimatedObj(each['path'], each['image'], each['max png'], each['rate'], each['x'], each['y'])
        animated_group.add(animated)
    return animated_group


def load_animals(scene):
    animal_group = pygame.sprite.Group()
    for each in scene['animals']:
        animal = Animal(each['image'], each['action'], each['direction'], each['x'], each['y'])
        animal_group.add(animal)
    return animal_group


def load_slime(scene):
    slime_group = pygame.sprite.Group()
    for each in scene['slimes']:
        slime = Slime(each['direction'], each['x'], each['y'])
        slime_group.add(slime)
    return slime_group


def exits(scene, player):
    for key, exit_data in scene['exits'].items():
        if player.rect.clipline(exit_data):
            return key, True
    return None, False


def load_battle_bg(scene):
    return Background(scene['battle background'])


def load_enemies(scene):
    enemy_group = pygame.sprite.Group()
    for each in scene['enemies']:
        enemy = Enemy(each['name'], each['image'], each['x'], each['y'], each['health'], each['mp'], each['damage'],
                      each['armor'])
        enemy_group.add(enemy)
    return enemy_group


def load_battle_group():
    battle_group = pygame.sprite.Group()
    for key, character_data in battle_characters.items():
        each = character_data
        character = BattleGroup(key, each['imagesource'], each['character'], each['action'], each['direction'], each['x'], each['y'], each['max hp'], each['hp'],
                                each['max mp'], each['mp'], each['strength'], each['defense'], each['agility'], each['level'])
        battle_group.add(character)
    return battle_group


def load_battle_menu():
    menu_group = pygame.sprite.Group()
    health_group = pygame.sprite.Group()
    hp_bar_position = 491
    for each in battle_menu:
        menu = BattleMenu(each['image'], each['x'], each['y'])
        menu_group.add(menu)
    for key, character_data in battle_characters.items():
        each = character_data
        bar = HealthBar(each['hp'], each['max hp'], 37, hp_bar_position)
        health_group.add(bar)
        hp_bar_position += 55
    return menu_group, health_group


def change_battle_menu(group, k_sprite, a_sprite):
    menu_group = group
    menu_to_remove = k_sprite
    menu_to_add = a_sprite
    menu_to_remove.kill()
    menu_group.add(menu_to_add)
    return menu_group
