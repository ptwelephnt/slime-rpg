import sys
import threading

import pygame
from sceneloader import fade_in, fade_out, load_scene, load_player, load_obs, load_npcs, load_animated, load_animals, \
    exits, load_special, load_slime
from tavern import scenes
from random import randint
from battle import battle
from utils import special_collision, clear_group

pygame.init()
size = width, height = 640, 640
screen = pygame.display.set_mode(size)
x = 255
pygame.key.set_repeat(10, 10)
clock = pygame.time.Clock()


def play(scene):
    background = load_scene(scene)
    player = load_player(scene)
    obst_group, line_list = load_obs(scene)
    npc_group = load_npcs(scene)
    animated_group = load_animated(scene)
    animal_group = pygame.sprite.Group()
    special_group = pygame.sprite.Group()
    slime_group = pygame.sprite.Group()
    all_groups = pygame.sprite.Group()
    all_groups.add(obst_group, animated_group, animal_group, special_group, npc_group, slime_group)
    special_check = False
    thread_check = False
    wait = False
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        background.show()
        moving = player.movement()
        player.show()
        if not wait:
            animated_group.update()
            animal_group.update()
            all_groups.draw(screen)

        if scene['battle check'] and moving and randint(0, 199) == 10:
            fade_out(screen, background)
            battle(scene)
            fade_in(screen, background)

        next_scene, scene_check = exits(scene, player)

        if scene_check:
            scene = scenes[next_scene]
            fade_out(screen, background)
            background = load_scene(scene)
            player = load_player(scene)
            clear_group(animated_group, obst_group, animal_group, npc_group, special_group, slime_group)
            special_check = scene['special check']
            if scene['animal check']:
                animal_group = load_animals(scene)
                all_groups.add(animal_group)
            if scene['obstacle check']:
                obst_group, line_list = load_obs(scene)
                all_groups.add(obst_group)
            if scene['animated check']:
                animated_group = load_animated(scene)
                all_groups.add(animated_group)
            if scene['NPC check']:
                npc_group = load_npcs(scene)
                all_groups.add(npc_group)
            if scene['special check']:
                special_group = load_special(scene)
                all_groups.add(special_group)
            if scene['slime check']:
                slime_group = load_slime(scene)
                all_groups.add(slime_group)
            fade_in(screen, background)
            wait = False

        if special_check:
            special_flag = special_collision(player, special_group)
            if special_flag:
                slime_thread = threading.Thread(target=slime_group.update, args=(player, background, all_groups, scene['text']))
                slime_thread.start()
                special_check = False
                thread_check = True

        if thread_check:
            slime_thread.join()

        pygame.display.flip()
        clock.tick(60)
