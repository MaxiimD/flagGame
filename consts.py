from pygame import constants as pygame_const

NUM_OF_BUSHES = 20
BUSH_IMG = "grass.png"
BUSH_HEIGHT = 40
BUSH_WIDTH = 40

WELCOME_MSG = "wcg"

GAME_GRID_ROW = 25
GAME_GRID_COL = 50

SOLDIER_HEIGHT = 4
SOLDIER_WIDTH = 2
SOLDIER_START_LOCATION = [0, 0]
SOLDIER_IMG = "soldier.png"
SOLDIER_IMG_XRAY = "soldier_nigth.png"
SOLDIER_STEP = 1

# This sets the WIDTH and HEIGHT of each grid location (in pixels)
SQUARE_WIDTH = 20
SQUARE_HEIGHT = 20
# This sets the margin between each cell(in pixels)
SQUARE_BORDER = 1
SQUARE_COLOR = (0, 100, 0)
# set the window dimensions based on the squares
WINDOW_HEIGHT = SQUARE_HEIGHT * GAME_GRID_ROW
WINDOW_WIDTH = SQUARE_WIDTH * GAME_GRID_COL

BACKGROUND_COLOR = (34, 139, 34)
BACKGROUND_XRAY = (0, 0, 0)

FLAG_WIDTH = 4
FLAG_HEIGHT = 3
FLAG_IMG = "flag.png"

NUM_OF_MINES = 20
MINE_WIDTH = 3
MINE_HEIGHT = 1
MINE_IMG = "mine.png"

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

MINE = 1
FLAG = 2
SOLIDER = 3
GUARD = 4
EMPTY = 0
TELEPORT = 5

# saves the bush x,y cords
bush_locations = []
# saves each mine's location in the grid
mine_locations = []

FONT_NAME = "Calibri"
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = (89, 89, 89)
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

# Dict containing num_key_const:timestamp_of_press
NUMBER_KEYS_TIME_DICT = {pygame_const.K_1: None, pygame_const.K_2: None, pygame_const.K_3: None, pygame_const.K_4: None,
                         pygame_const.K_5: None, pygame_const.K_6: None,
                         pygame_const.K_7: None, pygame_const.K_8: None, pygame_const.K_9: None}

MOVEMENT_KEYS = (pygame_const.K_UP, pygame_const.K_DOWN, pygame_const.K_LEFT, pygame_const.K_RIGHT,)

GRID_VIEW_TIME = 1

SAVE_TIME = 1

WIN_LOSE_MSG_TIME = 3

FPS = 60

GUARD_HEIGHT = 4
GUARD_WIDTH = 2
GUARD_STARTING_LOCATION = [0, int((GAME_GRID_ROW-1)/2)]
GUARD_MOVE_INTERVAL = 100  # in ms

RIGHT = 'R'
LEFT = 'L'

DB_COL = ['Mines', 'Bushes', 'Soldier', 'Guard']
