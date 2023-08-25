from pygame import constants as pygameConst

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
SQUARE_MARGIN = 1
SQUARE_COLOR = (0, 100, 0)
# set the window dimensions based on the squares
WINDOW_HEIGHT = SQUARE_HEIGHT * GAME_GRID_ROW + GAME_GRID_ROW * SQUARE_MARGIN + SQUARE_MARGIN
WINDOW_WIDTH = SQUARE_WIDTH * GAME_GRID_COL + GAME_GRID_COL * SQUARE_MARGIN + SQUARE_MARGIN

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
EMPTY = 0

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

NUMBER_KEYS = (
    pygameConst.K_1, pygameConst.K_2, pygameConst.K_3, pygameConst.K_4, pygameConst.K_5, pygameConst.K_6,
    pygameConst.K_7, pygameConst.K_8, pygameConst.K_9)
MOVEMENT_KEYS = (pygameConst.K_UP, pygameConst.K_DOWN, pygameConst.K_LEFT, pygameConst.K_RIGHT,)

GRID_VIEW_TIME = 1
