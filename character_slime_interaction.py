import sys

import pygame as py
from sceneloader import load_player, load_animated, load_scene
from tavern import scenes

py.init()

size = width, height = 640, 640
screen = py.display.set_mode(size)
clock = py.time.Clock()
py.key.set_repeat(10, 10)

slime_images = [
    'Images/Slimes/slimeawaywater.png',
    'Images/Slimes/slimefacewater.png',
    'Images/Slimes/slimewestwater.png',
]


class Slime(py.sprite.Sprite):
    def __init__(self, start_x=0, start_y=0):
        super().__init__()
        self.loaded_imgs = []
        self.load_images(slime_images)
        self.img_away = self.loaded_imgs[0]
        self.img_face = self.loaded_imgs[1]
        self.img_west = self.loaded_imgs[2]
        self.image = self.img_away
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def load_images(self, path_list):
        for each in path_list:
            image = py.image.load(each)
            self.loaded_imgs.append(image)

    def change_image(self, new_image):
        self.image = new_image

    def show(self):
        screen.blit(self.image, self.rect)

    def move(self, x_y, distance, seconds):
        frame_rate = 60
        steps = frame_rate * seconds
        px_per_frame = distance / steps
        print(px_per_frame)

        counter = 1
        while counter <= steps:
            if x_y == 'x':
                self.rect.x += px_per_frame
            elif x_y == 'y':
                self.rect.y += px_per_frame
            py.time.wait(200)
            counter += 1


player = load_player(scenes['beach2'])
animated = load_animated(scenes['beach2'])
background = load_scene(scenes['beach2'])
slime = Slime(320, 320)

if __name__ == '__main__':
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        background.show()
        moving = player.movement()
        player.show()
        animated.draw(screen)
        animated.update()
        slime.show()

        clock.tick(60)
        py.display.flip()
