current_scene = []


def boundary_top(char):
    if char.top >= 1:
        return True


def boundary_bottom(char):
    if char.bot <= 639:
        return True


def boundary_right(char):
    if char.right <= 639:
        return True


def boundary_left(char):
    if char.left >= 1:
        return True


alphabet_dictionary = {
    'a': (8, 15),
    'b': (9, 15),
    'c': (8, 15),
    'd': (9, 15),
    'e': (8, 15),
    'f': (5, 15),
    'g': (9, 16),
    'h': (9, 15),
    'i': (4, 15),
    'j': (4, 15),
    'k': (9, 15),
    'l': (4, 15),
    'm': (13, 15),
    'n': (9, 15),
    'o': (9, 15),
    'p': (9, 15),
    'q': (9, 15),
    'r': (6, 15),
    's': (8, 15),
    't': (5, 15),
    'u': (9, 15),
    'v': (9, 15),
    'w': (12, 15),
    'x': (9, 15),
    'y': (9, 15),
    'z': (8, 15),
    ' ': (4, 15),
    'A': (11, 15),
    'B': (11, 15),
    'C': (11, 15),
    'D': (11, 15),
    'E': (10, 15),
    'F': (9, 15),
    'G': (12, 15),
    'H': (11, 15),
    'I': (4, 15),
    'J': (8, 15),
    'K': (11, 15),
    'L': (9, 15),
    'M': (13, 15),
    'N': (11, 15),
    'O': (12, 15),
    'P': (10, 15),
    'Q': (12, 15),
    'R': (11, 15),
    'S': (10, 15),
    'T': (9, 15),
    'U': (11, 15),
    'V': (10, 15),
    'W': (14, 15),
    'X': (10, 15),
    'Y': (10, 15),
    'Z': (9, 15),
    '1': (8, 15),
    '2': (8, 15),
    '3': (8, 15),
    '4': (8, 15),
    '5': (8, 15),
    '6': (8, 15),
    '7': (8, 15),
    '8': (8, 15),
    '9': (8, 15),
    '0': (8, 15),
    '!': (5, 15),
    '@': (15, 15),
    '#': (9, 15),
    '$': (8, 15),
    '%': (13, 15),
    '^': (9, 15),
    '&': (11, 15),
    '*': (6, 15),
    '(': (5, 15),
    ')': (5, 15),
    '_': (10, 15),
    '+': (9, 15),
    '-': (5, 15),
    '=': (9, 15),
    '.': (4, 15),
    '\'': (4, 15),
    '\n': (0, 15),
    ',': (4, 15),
    '?': (9, 15),
}


def character_spacing(character):
    spacing = alphabet_dictionary[character][0]
    return spacing


def line_break(self, string):
    self.string_width = 0
    self.string_width += alphabet_dictionary[self.text_index][0]
    if self.string_width >= 280:
        self.rect.y += 20
        self.stored_spacing = 0
        return True


def check_collisions(main_character, *non_player_groups):
    main_character.prev_x = main_character.rect.x
    main_character.prev_y = main_character.rect.y
    # Check for collisions with non-player characters
    for group in non_player_groups:
        for sprite in group:
            if main_character.rect.colliderect(sprite.rect):
                # Move the main character back to its previous position
                main_character.rect.x = main_character.prev_x
                main_character.rect.y = main_character.prev_y
                return False
    return True


def special_collision(player, group):
    counter = 0
    for each in group.sprites():
        while each.top <= player.rect.center[1] <= each.bot and each.left <= player.rect.center[0] <= each.right:
            print(player.rect.center)
            counter += 1
            if counter == 20:
                return True
    return False


def clear_group(*group):
    for sprite_group in group:
        for each in sprite_group.sprites():
            each.kill()
