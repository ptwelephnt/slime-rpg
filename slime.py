from textbox import TextBox
import pygame

size = width, height = 640, 640
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Slime(pygame.sprite.Sprite):
    def __init__(self, direction='away', x=0, y=0, png=0):
        super().__init__()
        self.png = png
        self.direction = direction
        self.imagesource = f'images/slimes/slime{self.direction}water.png'
        self.image = pygame.image.load(self.imagesource)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = x, y
        self.move = 0
        self.bot = self.rect.bottom
        self.top = self.rect.top
        self.right = self.rect.right
        self.left = self.rect.left
        self.end = False
        self.start = True
        self.step = False
        self.pause = False
        self.up = True
        self.counter = 0

    def show(self):
        screen.blit(self.image, self.rect)

    def update(self, player, bg, groups, text):
        self.start_position = self.rect.x
        box_check = False
        text_check = False
        player_speak = TextBox(player)
        # while not self.end:
        while True:
            bg.show()
            groups.draw(screen)
            player.show()
            self.counter += 1
            if self.start and self.counter == 5:
                self.direction = 'west'
                self.start = False
                self.step = True
                self.counter = 0
            elif self.step and self.counter == 5:
                if not self.pause:
                    player.change_direction('north')
                    self.direction = 'west'
                    self.rect.x -= 3
                difference = self.start_position - self.rect.x
                if difference >= 50:
                    player.change_direction('east')
                    self.direction = 'away'
                    self.start_position = self.rect.x
                    self.pause = True
                    start_time = pygame.time.get_ticks()
                elif self.rect.x <= 200:
                    self.step = False
                    player.change_direction('east')
                    box_check = True
                if self.pause:
                    current_time = pygame.time.get_ticks()
                    elapsed_time = (current_time - start_time) / 1000
                if self.pause and elapsed_time >= 1:
                    self.pause = False
                self.counter = 0
            elif box_check:
                player.change_direction('east', action='crouch')
                welcome_group, text_check = player_speak.grow()
                welcome_group.draw(screen)
                if text_check:
                    text_group, text_check, self.end = player_speak.speak(screen, text)

            self.image = pygame.image.load(f'images/slimes/slime{self.direction}water.png')
            self.show()

            pygame.display.flip()
