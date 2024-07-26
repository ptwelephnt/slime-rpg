from utils import character_spacing, alphabet_dictionary
import pygame
import sys
import time

pygame.init()
size = width, height = 640, 640

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

black = 0, 0, 0


class TextBox(pygame.sprite.Sprite):
    def __init__(self, character):
        self.png = 10
        self.image = pygame.image.load(f'images/Text Box/textbox{self.png}.png')
        self.rect = self.image.get_rect()
        self.character_x = character.rect.x
        self.character_y = character.rect.y
        self.rect.center = self.character_x, self.character_y
        self.cx = self.character_x
        self.cy = self.character_y
        self.count = 0
        self.text_check = False
        self.text_group = pygame.sprite.Group()
        self.character_size = 0
        self.text_index = 0
        self.stored_spacing = 0
        self.string_width = 0
        self.line_down = 20

    def grow(self):
        welcome_group = pygame.sprite.Group()
        self.count += 1
        if self.character_y >= 290:
            self.dest_y = 150
        else:
            self.dest_y = 490
        if self.count == 2 and self.cy != self.dest_y and self.png != 1:
            self.png -= 1
            self.cy += (self.dest_y - self.character_y) / 9
            self.cx += (320 - self.character_x) / 9
            self.count = 0
            self.image = pygame.image.load(f'images/Text Box/textbox{self.png}.png')
        elif self.png == 1:
            self.text_check = True

        welcome_box = pygame.sprite.Sprite()
        welcome_box.image = self.image
        welcome_box.rect = self.image.get_rect()
        welcome_box.rect.center = self.cx, self.cy
        welcome_group.add(welcome_box)
        return welcome_group, self.text_check

    def line_break(self, string):
        character = string[self.text_index]
        self.string_width += alphabet_dictionary[character][0]
        if self.string_width >= 560:
            self.stored_spacing = 0
            self.string_width = 0
            self.line_down += 20

    def speak(self, surface, text_input, draw_only=False):
        length = len(text_input)
        if draw_only:
            return self.text_group.draw(surface)
        elif self.text_index == length:
            return self.text_group.draw(screen), False, True
        elif self.text_index != length and text_input[self.text_index] != '\n':
            self.line_break(text_input)
            text_font = pygame.font.Font('freesansbold.ttf', 15)
            text_surface = text_font.render(text_input[self.text_index], True, [255, 255, 255])
            letter = pygame.sprite.Sprite()
            letter.image = text_surface
            letter.rect = text_surface.get_rect()
            letter.rect.x = 40
            letter.rect.y = self.line_down + (self.dest_y - 150)
            letter.rect.x += self.stored_spacing
            self.text_group.add(letter)
            self.stored_spacing += character_spacing(text_input[self.text_index])
            print(text_input[self.text_index], letter.rect.x, letter.rect.y)
        self.text_index += 1
        return self.text_group.draw(screen), True, False