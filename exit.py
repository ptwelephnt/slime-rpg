def exit_scene(next_scene, screen, background, pygame, time, classy):
    # "line" = (x1, y1, x2, y2)
        x = 255
        while x > 3:
            screen.fill((0, 0, 0))
            background.image.set_alpha(x)
            background.show()
            x -= 4
            pygame.display.flip()
            time.sleep(.001)
        current_scene = next_scene
        while x < 255:
            background = classy(current_scene['background'])
            x = 255
            screen.fill((0, 0, 0))
            background.image.set_alpha(x)
            background.show()
            pygame.display.flip()
            time.sleep(.001)
