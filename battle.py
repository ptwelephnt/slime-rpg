import pdb
import pygame
import sys
import time
from sceneloader import load_battle_bg, load_enemies, load_battle_group, load_battle_menu, fade_in, fade_out
from AIBattleClasses import Selector

pygame.init()
size = width, height = 640, 640
screen = pygame.display.set_mode(size)
pygame.key.set_repeat(10, 10)
clock = pygame.time.Clock()


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


def choose_turn(group):
    while True:
        for sprite in group.sprites():
            if sprite.turn():
                return sprite


def battle(scene):
    pygame.key.set_repeat(200, 10)
    background = load_battle_bg(scene)
    enemy_group = load_enemies(scene)
    exp = 0
    for each in enemy_group:
        exp += each.exp
    battle_group = load_battle_group()
    menu_group, health_group = load_battle_menu()
    attack_choice = menu_group.sprites()[4]
    magic_choice = menu_group.sprites()[5]
    magic_choice.kill()
    number_of_enemies = len(enemy_group.sprites())
    done_attacking = True
    enemy_damaged = False
    narrate_check = False
    battle_end = False
    level_up_narrate = False
    dead = False
    start = True
    counter = 0
    selector = Selector(275, 488)
    running = True
    character = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        if start:
            fade_in(screen, background)
            start = False
        background.show()
        enemy_group.draw(screen)
        battle_group.draw(screen)
        menu_group.draw(screen)
        health_group.draw(screen)
        selector.show()
        selector_pos, menu_group_update, attacking = selector.cursor_move(battle_group, menu_group, attack_choice, magic_choice, enemy_group, character)
        selector.floating(selector_pos)
        if not character:
            character = choose_turn(battle_group)
        if menu_group_update:
            menu_group = menu_group_update
        if attacking:
            x, y, enemy = attacking
            done_attacking = False
        if battle_end:
            counter += 1
            if add_experience:
                for each in battle_group:
                    each.add_exp(exp)
                exp = 0
                add_experience = False
            if counter == 40:
                fade_out(screen, background)
                running = False
        if dead:
            counter += 1
            narrate_group = narrate(f"{enemy.name} has been defeated!")
            narrate_group.draw(screen)
            if counter == 40:
                dead = False
                counter = 0
                if len(enemy_group.sprites()) == 0:
                    battle_end = True
                    add_experience = True
                else:
                    character = choose_turn(battle_group)
        if not done_attacking:
            done_attacking = character.move(x, y, enemy)
            character.attack_animate()
            enemy_damaged = True
        if enemy_damaged:
            damage = character.attack(enemy)
            enemy_damaged = False
            narrate_check = True
        if narrate_check:
            counter += 1
            narrate_group = narrate(f"{character.name} attacked {enemy.name} and dealt {damage} damage!")
            narrate_group.draw(screen)
            if counter == 40:
                narrate_check = False
                counter = 0
                if number_of_enemies > len(enemy_group.sprites()):
                    number_of_enemies = len(enemy_group.sprites())
                    dead = True

        clock.tick(60)
        pygame.display.flip()
