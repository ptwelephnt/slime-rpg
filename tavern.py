scenes = {
    'beach2': {
        'background': 'Images/Background/beach1.png',
        'player': {'image': 'images/Main Character/', 'action': 'walk', 'png': 1, 'direction': 'north', 'x': 300,
                   'y': 588},
        'exits': {'beach1': (0, 200, 0, 440), 'hometown': (640, 200, 640, 440)},
        'obstacle check': False,
        'NPC check': False,
        'animated check': True,
        'animal check': False,
        'return check': True,
        'battle check': False,
        'special check': True,
        'slime check': True,
        'slimes': [
            {'direction': 'away', 'x': 386, 'y': 81}
        ],
        'text': 'Well hello there.',
        'NPCs': [],
        'obstacles': [],
        'special': [
            {'image': 'images/environment/seashell.png', 'x': 157, 'y': 81}
        ],
        'battle background': 'Images/background/battlebg.png',
        'enemies': [
            {'image': 'Images/Enemies/Dragon.png', 'x': 45, 'y': 35, 'health': 100, 'mp': 100, 'damage': 10, 'armor': 0,
             'name': 'Dagron'},
            {'image': 'Images/Enemies/Dragon.png', 'x': 145, 'y': 135, 'health': 100, 'mp': 100, 'damage': 10,
             'armor': 0,
             'name': 'Dagron'}
        ],
        'battle menu': [
            {'image': 'Images/Battle/BattleMenu.png', 'x': 0, 'y': 445},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 460},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 515},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 570},
            {'image': 'Images/Battle/attackchoice.png', 'x': 225, 'y': 465},
            {'image': 'Images/Battle/magicchoice.png', 'x': 225, 'y': 465}
        ],
        'animated': [
            {'image': 'shortwater', 'path': 'Images/environment/animated/', 'x': 0, 'y': 0, 'max png': 8, 'rate': 20},
            {'image': 'fullwaves', 'path': 'Images/environment/animated/', 'x': 0, 'y': 10, 'max png': 10, 'rate': 20}
        ]
    },
    'beach1': {
        'background': 'Images/Background/beach1.png',
        'player': {'image': 'images/Main Character/', 'action': 'walk', 'png': 1, 'direction': 'north', 'x': 300,
                   'y': 588},
        'exits': {'road1': (200, 640, 440, 640), 'beach2': (640, 200, 640, 440)},
        'obstacle check': False,
        'NPC check': False,
        'animated check': True,
        'animal check': False,
        'return check': True,
        'battle check': False,
        'special check': False,
        'slime check': False,
        'obstacles': [],
        'battle background': 'Images/background/battlebg.png',
        'enemies': [
            {'image': 'Images/Enemies/Dragon.png', 'x': 45, 'y': 35, 'health': 100, 'mp': 100, 'damage': 10, 'armor': 0,
             'name': 'Dagron'},
            {'image': 'Images/Enemies/Dragon.png', 'x': 145, 'y': 135, 'health': 100, 'mp': 100, 'damage': 10,
             'armor': 0,
             'name': 'Dagron'}
        ],
        'battle menu': [
            {'image': 'Images/Battle/BattleMenu.png', 'x': 0, 'y': 445},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 460},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 515},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 570},
            {'image': 'Images/Battle/attackchoice.png', 'x': 225, 'y': 465},
            {'image': 'Images/Battle/magicchoice.png', 'x': 225, 'y': 465}
        ],
        'animated': [
            {'image': 'shortwater', 'path': 'Images/environment/animated/', 'x': 0, 'y': 0, 'max png': 8, 'rate': 20},
            {'image': 'fullwaves', 'path': 'Images/environment/animated/', 'x': 0, 'y': 10, 'max png': 10, 'rate': 20}
        ]
    },
    'road3': {
        'background': 'Images/Background/road3.png',
        'player': {'image': 'images/Main Character/', 'action': 'walk', 'png': 1, 'direction': 'north', 'x': 300,
                   'y': 588},
        'exits': {'road1': (200, 640, 440, 640), 'hometown': (640, 200, 640, 440)},
        'obstacle check': False,
        'NPC check': False,
        'animated check': True,
        'animal check': False,
        'return check': True,
        'battle check': False,
        'special check': False,
        'slime check': False,
        'obstacles': [],
        'battle background': 'Images/background/battlebg.png',
        'enemies': [
            {'image': 'Images/Enemies/Dragon.png', 'x': 45, 'y': 35, 'health': 100, 'mp': 100, 'damage': 10, 'armor': 0,
             'name': 'Dagron'},
            {'image': 'Images/Enemies/Dragon.png', 'x': 145, 'y': 135, 'health': 100, 'mp': 100, 'damage': 10,
             'armor': 0,
             'name': 'Dagron'}
        ],
        'battle menu': [
            {'image': 'Images/Battle/BattleMenu.png', 'x': 0, 'y': 445},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 460},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 515},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 570},
            {'image': 'Images/Battle/attackchoice.png', 'x': 225, 'y': 465},
            {'image': 'Images/Battle/magicchoice.png', 'x': 225, 'y': 465}
        ],
        'animated': [
            {'image': 'campfire', 'path': 'Images/Animated Objects/', 'x': 310, 'y': 520, 'max png': 5, 'rate': 20},
        ]
    },
    'road2': {
        'background': 'Images/Background/road2.png',
        'player': {'image': 'images/Main Character/', 'action': 'walk', 'png': 1, 'direction': 'north', 'x': 300,
                   'y': 588},
        'exits': {'road1': (200, 640, 440, 640), 'beach1': (200, 0, 440, 0), 'road3': (640, 200, 640, 440)},
        'obstacle check': False,
        'NPC check': False,
        'animated check': False,
        'animal check': False,
        'return check': True,
        'battle check': False,
        'special check': False,
        'slime check': False,
        'obstacles': [],
        'battle background': 'Images/background/battlebg.png',
        'enemies': [
            {'image': 'Images/Enemies/Dragon.png', 'x': 45, 'y': 35, 'health': 100, 'mp': 100, 'damage': 10, 'armor': 0,
             'name': 'Dagron'},
            {'image': 'Images/Enemies/Dragon.png', 'x': 145, 'y': 135, 'health': 100, 'mp': 100, 'damage': 10,
             'armor': 0,
             'name': 'Dagron'}
        ],
        'battle menu': [
            {'image': 'Images/Battle/BattleMenu.png', 'x': 0, 'y': 445},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 460},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 515},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 570},
            {'image': 'Images/Battle/attackchoice.png', 'x': 225, 'y': 465},
            {'image': 'Images/Battle/magicchoice.png', 'x': 225, 'y': 465}
        ]
    },
    'road1': {
        'background': 'Images/Background/road1.png',
        'player': {'image': 'images/Main Character/', 'action': 'walk', 'png': 1, 'direction': 'north', 'x': 300,
                   'y': 588},
        'exits': {'road2': (200, 0, 440, 0), 'hometown': (200, 640, 440, 640)},
        'obstacle check': False,
        'NPC check': False,
        'animated check': False,
        'animal check': False,
        'return check': True,
        'battle check': True,
        'special check': False,
        'slime check': False,
        'obstacles': [],
        'battle background': 'Images/background/battlebg.png',
        'enemies': [
            {'image': 'Images/Enemies/Dragon.png', 'x': 45, 'y': 35, 'health': 100, 'mp': 100, 'damage': 10, 'armor': 0,
             'name': 'Dagron'},
            {'image': 'Images/Enemies/Dragon.png', 'x': 145, 'y': 135, 'health': 100, 'mp': 100, 'damage': 10,
             'armor': 0,
             'name': 'Dagron'}
        ],
        'battle menu': [
            {'image': 'Images/Battle/BattleMenu.png', 'x': 0, 'y': 445},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 460},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 515},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 570},
            {'image': 'Images/Battle/attackchoice.png', 'x': 225, 'y': 465},
            {'image': 'Images/Battle/magicchoice.png', 'x': 225, 'y': 465}
        ]
    },
    'hometown': {
        'background': 'Images/Hometown.png',
        'player': {'image': 'images/Main Character/', 'action': 'walk', 'png': 1, 'direction': 'north', 'x': 308,
                   'y': 588},
        'exits': {'road1': (200, 0, 440, 0), 'tavern': (257, 640, 362, 640)},
        'obstacle check': True,
        'NPC check': False,
        'animated check': False,
        'animal check': True,
        'return check': True,
        'battle check': False,
        'special check': False,
        'slime check': False,
        'obstacles': [
            {'image': 'images/tavernOutside.png', 'x': 257, 'y': 591, 'boundaries': 'mid'},
            {'image': 'images/bankOutside.png', 'x': 0, 'y': 326, 'boundaries': 'mid'}
        ],
        'animals': [
            {'image': 'Images/NPCs/Animals/chicken/chicken', 'action': 'walk', 'direction': 'south', 'x': 480,
             'y': 320},
            {'image': 'Images/NPCs/Animals/Cow/Cow', 'action': 'walk', 'direction': 'east', 'x': 160, 'y': 320}
        ],
        'battle background': 'Images/background/battlebg.png',
        'enemies': [
            {'image': 'Images/Enemies/Dragon.png', 'x': 45, 'y': 35, 'health': 100, 'mp': 100, 'damage': 10, 'armor': 0,
             'name': 'Dagron'},
            {'image': 'Images/Enemies/Dragon.png', 'x': 145, 'y': 135, 'health': 100, 'mp': 100, 'damage': 10,
             'armor': 0,
             'name': 'Dagron'}
        ],
        'battle menu': [
            {'image': 'Images/Battle/BattleMenu.png', 'x': 0, 'y': 445},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 460},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 515},
            {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 570},
            {'image': 'Images/Battle/attackchoice.png', 'x': 225, 'y': 465},
            {'image': 'Images/Battle/magicchoice.png', 'x': 225, 'y': 465}
        ]
    },
    'tavern': {
        'background': 'Images/Tavern2.png',
        'player': {'image': 'images/Main Character/', 'action': 'walk', 'png': 1, 'direction': 'north', 'x': 308,
                   'y': 588},
        'exits': {'hometown': (312, 0, 328, 0)},
        'obstacle check': True,
        'NPC check': True,
        'animated check': True,
        'animal check': False,
        'battle check': False,
        'special check': False,
        'slime check': False,
        'NPCs': [
            {'image': 'images/npcs/shopkeeper.png', 'x': 500, 'y': 375},
            {'image': 'images/npcs/roguesitting.png', 'x': 162, 'y': 80},
            {'image': 'images/npcs/roguefemalesitting.png', 'x': 83, 'y': 146},
            {'image': 'images/npcs/roguefriendsitting.png', 'x': 241, 'y': 148},
            ],
        'obstacles': [
            {'image': 'images/chairFS.png', 'x': 157, 'y': 80, 'boundaries': 'mid'},
            {'image': 'images/chairFE.png', 'x': 71, 'y': 146, 'boundaries': 'left'},
            {'image': 'images/table.png', 'x': 128, 'y': 146, 'boundaries': 'sides'},
            {'image': 'images/chairFW.png', 'x': 241, 'y': 148, 'boundaries': 'right'},
            {'image': 'images/chairFN.png', 'x': 160, 'y': 226, 'boundaries': 'bottom'},
            {'image': 'images/chairFS.png', 'x': 157, 'y': 349, 'boundaries': 'mid'},
            {'image': 'images/table.png', 'x': 128, 'y': 405, 'boundaries': 'sides'},
            {'image': 'images/chairFE.png', 'x': 78, 'y': 412, 'boundaries': 'left'},
            {'image': 'images/chairFW.png', 'x': 238, 'y': 414, 'boundaries': 'right'},
            {'image': 'images/chairFN.png', 'x': 161, 'y': 487, 'boundaries': 'bottom'},
        ],
        'animated': [
            {'image': 'grandfatherclock', 'path': 'Images/Animated Objects/', 'x': 100, 'y': 0, 'max png': 5,
             'rate': 20},
        ]
    }}

battle_characters = {
    'Aubrey': {'imagesource': 'Images/Main Character/', 'character': '', 'action': 'Attack', 'direction': 'West',
               'x': 400, 'y': 300, 'max hp': 100, 'max mp': 100,
               'hp': 100, 'mp': 100,
               'strength': 100, 'defense': 5, 'agility': 95, 'exp': 0, 'level': 1},
    'Holy Cow': {'imagesource': 'Images/NPCs/Animals/Cow/', 'character': 'Cow', 'action': 'Walk', 'direction': 'West',
                 'x': 450, 'y': 250, 'max hp': 100, 'max mp': 100,
                 'hp': 100, 'mp': 100,
                 'strength': 100, 'defense': 5, 'agility': 45, 'exp': 0, 'level': 1},
    'Big Cock': {'imagesource': 'Images/NPCs/Animals/Chicken/', 'character': 'Chicken', 'action': 'Walk',
                 'direction': 'West', 'x': 350, 'y': 350, 'max hp': 100, 'max mp': 100,
                 'hp': 100, 'mp': 100,
                 'strength': 100, 'defense': 5, 'agility': 75, 'exp': 0, 'level': 1}
}

battle_menu = [
    {'image': 'Images/Battle/BattleMenu.png', 'x': 0, 'y': 445},
    {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 460},
    {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 515},
    {'image': 'Images/Battle/HealthBar.png', 'x': 10, 'y': 570},
    {'image': 'Images/Battle/attackchoice.png', 'x': 225, 'y': 465},
    {'image': 'Images/Battle/magicchoice.png', 'x': 225, 'y': 465}
]
