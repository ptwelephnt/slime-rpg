hometown = {
    'background': 'Images/Hometown.png',
    'player': {'image': 'images/Main Character/', 'png': 1, 'direction': 'walknorth', 'x': 308, 'y': 588},
    'exit1': (0, 0, 30, 0),
    'exit2': (0, 0, 30, 0),
    'return': (257, 640, 362, 640),
    'obstacle check': True,
    'NPC check': False,
    'animated check': False,
    'animal check': True,
    'return check': True,
    'obstacles': [
        {'image': 'images/tavernOutside.png', 'x': 257, 'y': 591, 'boundaries': 'mid'},
        {'image': 'images/bankOutside.png', 'x': 0, 'y': 326, 'boundaries': 'mid'}
    ],
    'animals': [
        {'image': 'Images/NPCs/Animals/chicken/chicken', 'action': 'walk', 'direction': 'south', 'x': 480, 'y': 320},
        {'image': 'Images/NPCs/Animals/Cow/Cow', 'action': 'walk', 'direction': 'east', 'x': 160, 'y': 320}
    ]
}
png = 1
tavern_scene = {
    'background': 'Images/Tavern2.png',
    'player': {'image': f'images/Main Character/', 'png': 1, 'direction': 'walknorth', 'x': 308, 'y': 50},
    'exit1': (312, 0, 328, 0),
    'exit2': (0, 0, 30, 0),
    'next scene1': hometown,
    'obstacle check': True,
    'NPC check': True,
    'animated check': True,
    'animal check': False,
    'return check': False,
    'NPCs': [{'image': 'images/npcs/shopkeeper.png', 'x': 500, 'y': 375},
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
        {'image': 'grandfatherclock', 'x': 100, 'y': 0},
        ]
}

opening_scene = {'background': 'images/azoDyot.png'}
