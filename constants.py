import json

with open('config.json', 'r') as file:
    config = json.load(file)

SCREEN_WIDTH = config['screen_width']
SCREEN_HEIGHT = config['screen_height']

WHITE = tuple(config['colors']['white'])
BLACK = tuple(config['colors']['black'])
RED = tuple(config['colors']['red'])

PLAYER_WIDTH = config['player']['width']
PLAYER_HEIGHT = config['player']['height']
PLAYER_SPEED = config['player']['speed']

OBSTACLE_WIDTH = config['obstacle']['width']
OBSTACLE_HEIGHT = config['obstacle']['height']
OBSTACLE_SPEED = config['obstacle']['speed']
OBSTACLE_FREQUENCY = config['obstacle']['frequency']

FONT_SIZE = config['font_size']
