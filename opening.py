import pdb
from utils import character_spacing, alphabet_dictionary
import pygame
import sys
import time


pygame.init()
size = width, height = 640, 640

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

black = 0, 0, 0


class CharacterIntro(pygame.sprite.Sprite):
    def __init__(self, image, action, x=0, y=0):
        super().__init__()
        self.png = 1
        self.imagesource = image
        self.action = action
        self.image = pygame.image.load(f'{self.imagesource}{self.action}{str(self.png)}.png')
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.count = 0
        self.enter = True
        self.reset = True
        self.fall = False
        self.stand = False
        self.back = False
        self.welcome = False
        self.text_box = False

    def animate_character(self):
        character_group = pygame.sprite.Group()
        self.count += 1
        if self.rect.y < 320 and self.enter:
            if self.count == 1:
                self.rect.y += 3
                self.png += 1
                self.count = 0
            self.image = pygame.image.load(f'{self.imagesource}{self.action}{str(self.png)}.png')
            if self.png == 9:
                self.png = 1
        elif self.reset:
            self.enter = False
            self.reset = False
            self.png = 1
            self.fall = True

        if self.fall and self.count == 5 and self.png != 6:
            self.action = 'fall'
            self.rect.y += 12
            self.png += 1
            self.count = 0
            if self.png == 6:
                self.fall = False
                self.stand = True
            self.image = pygame.image.load(f'{self.imagesource}{self.action}{str(self.png)}.png')
        elif self.count == 20 and self.stand:
            self.png -= 1
            self.count = 0
            self.image = pygame.image.load(f'{self.imagesource}{self.action}{str(self.png)}.png')
            if self.png == 1:
                time.sleep(.5)
                self.stand = False
                self.back = True
        elif self.count == 2 and self.back:
            self.action = 'walknorth'
            self.rect.y -= 3
            self.png += 1
            self.count = 0
            self.image = pygame.image.load(f'{self.imagesource}{self.action}{str(self.png)}.png')
            if self.png == 9:
                self.png = 1
            if self.rect.y <= 320:
                self.back = False
                self.welcome = True
                self.png = 1

        if self.count == 2 and self.welcome:
            self.action = 'walksouth'
            self.count = 0
            self.image = pygame.image.load(f'{self.imagesource}{self.action}{str(self.png)}.png')
            self.welcome = False
            self.text_box = True

        character = pygame.sprite.Sprite()
        character.image = self.image
        character.rect = self.image.get_rect()
        character.rect.x = self.rect.x
        character.rect.y = self.rect.y
        character_group.add(character)
        return character_group, self.text_box


class WelcomeBox(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        self.png = 10
        self.image = pygame.image.load(f'images/Text Box/textbox{self.png}.png')
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.cx = x
        self.cy = y
        self.count = 0
        self.text_check = False
        self.text_group = pygame.sprite.Group()
        self.character_x = 0
        self.character_size = 0
        self.text_index = 0
        self.stored_spacing = 0
        self.string_width = 0
        self.line_down = 20


    def grow(self):
        welcome_group = pygame.sprite.Group()
        self.count += 1
        # if self.count == 5 and self.png != 1:
        #     self.png -= 1
        if self.count == 2 and self.cy != 150 and self.png != 1:
            self.png -= 1
            self.cy -= 17
            self.count = 0
            self.image = pygame.image.load(f'images/Text Box/textbox{self.png}.png')
        if self.cy == 150:
            self.text_check = True

        welcome_box = pygame.sprite.Sprite()
        welcome_box.image = self.image
        welcome_box.rect = self.image.get_rect()
        welcome_box.rect.center = 320, self.cy
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
            letter.rect.y = self.line_down
            letter.rect.x += self.stored_spacing
            self.text_group.add(letter)
            self.stored_spacing += character_spacing(text_input[self.text_index])
            print(text_input[self.text_index], letter.rect.x, letter.rect.y)
        self.text_index += 1
        return self.text_group.draw(screen), True, False

def load_background():
    image = pygame.image.load('images/azoDyot.png')
    imagerect = image.get_rect()
    imagerect.x = 0
    imagerect.y = 0
    return image, imagerect

def show(self):
    screen.blit(self.image, self.rect)

if __name__ == '__main__':

    character = CharacterIntro('images/main character/', 'walksouth', 320, 0)
    welcome = WelcomeBox(320, 303)
    text_group = pygame.sprite.Group()
    bg_check = False
    opacity = 0
    text = '''
    Whoops! I tripped there. He he.. Anyway... Welcome and Hello!! How are you doing today? I have a wonderful story
    I'd like to tell you.
    '''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)

        character_group, box_check = character.animate_character()
        if box_check:
            welcome_group, text_check = welcome.grow()
            welcome_group.draw(screen)
            if text_check:
                text_group, text_check, bg_check = welcome.speak(screen, text)
        if bg_check:
            background, backgroundrect = load_background()
            if opacity < 255:
                opacity += 5
            background.set_alpha(opacity)
            screen.blit(background, backgroundrect)

        character_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)
