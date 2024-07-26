import pygame
from pygame import gfxdraw
import math
import random
import noise

# initialize pygame
pygame.init()

# get the size of the screen
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# create a fullscreen window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


class Rainbow:
    def __init__(self, i_color, red_flag=False, green_flag=False, blue_flag=False):
        self.red, self.green, self.blue = i_color
        self.red_flag = red_flag
        self.green_flag = green_flag
        self.blue_flag = blue_flag

    def change_color(self):
        if self.red_flag and self.red == 0:
            self.red_flag = False
            self.green_flag = True
        elif self.red_flag:
            self.red -= 1
            self.green += 1
        elif self.green_flag and self.green == 0:
            self.green_flag = False
            self.blue_flag = True
        elif self.green_flag:
            self.green -= 1
            self.blue += 1
        elif self.blue_flag and self.blue == 0:
            self.blue_flag = False
            self.red_flag = True
        elif self.blue_flag:
            self.blue -= 1
            self.red += 1
        return self.red, self.green, self.blue


class Starburst(pygame.sprite.Sprite):
    def __init__(self, surface, center, radius, color, is_growing=True):
        super().__init__()
        self.surface = surface
        self.center = center
        self.radius = radius
        self.color = color
        self.angle = 0
        self.is_growing = is_growing
        self.has_shrunk = False
        self.shape_change = False
        self.num_points = 1

    def draw(self):
        num_points = self.num_points
        angle_step = 360 / num_points
        start_angle = 0 + self.angle
        end_angle = angle_step + self.angle

        for i in range(num_points):
            # Calculate start and end points for line segment
            start_x = int(self.center[0] + self.radius * math.cos(math.radians(start_angle)))
            start_y = int(self.center[1] + self.radius * math.sin(math.radians(start_angle)))
            end_x = int(self.center[0] + self.radius * math.cos(math.radians(end_angle)))
            end_y = int(self.center[1] + self.radius * math.sin(math.radians(end_angle)))

            # Draw line segment
            gfxdraw.line(self.surface, start_x, start_y, end_x, end_y, self.color)

            # Move to next angle
            start_angle = end_angle
            end_angle += angle_step

    def rotate(self, color):
        self.color = color
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0

    def animate(self):
        if self.is_growing:
            self.radius += 1
            if self.radius >= screen_height / 2:
                self.is_growing = False
        else:
            self.radius -= 1
            if self.radius <= 1:
                self.is_growing = True
                self.has_shrunk = True

    def change_center(self):
        if self.has_shrunk:
            self.center = (random.randint(0, screen_width), random.randint(0, screen_height))
            self.has_shrunk = False
            self.shape_change = True

    def change_shape(self):
        if self.shape_change:
            if self.num_points < 12:
                self.num_points += 1
            else:
                self.num_points = 2
            self.shape_change = False


color1 = Rainbow((255, 0, 0), red_flag=True)

starburst = Starburst(screen, (320, 240), 100, (255, 0, 0))
starburst2 = Starburst(screen, (320, 240), 100, (255, 0, 0))

# run the game loop
running = True
while running:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    starburst.draw()
    starburst.rotate(color1.change_color())
    starburst.animate()
    starburst.change_center()
    starburst.change_shape()
    for each in range(0, 10):
        color1.change_color()
    starburst2.draw()
    starburst2.rotate(color1.change_color())
    starburst2.animate()
    starburst2.change_center()
    starburst2.change_shape()
    # starburst_group.draw(screen)
    pygame.draw.circle(screen, (0, 0, 0), (screen_width * 7 / 9, screen_height * 9 / 11), 5)

    # update the screen
    pygame.display.flip()

# quit pygame
pygame.quit()
