import pygame, os
from pygame.locals import *
import sys
from random import randint, choice
import random
import time
from Classes import *
pygame.init()
HEIGHT = 600
WIDTH = 575
GRIDSIZE = HEIGHT // 24
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris - David Gurevich")

LVL_1, LVL_2, LVL_3, LVL_4, LVL_5, LVL_6, LVL_7, LVL_8, LVL_9 = 45, 20, 10, 7, 5, 4, 3, 2, 1

LEVELS = [LVL_1, LVL_2, LVL_3, LVL_4, LVL_5, LVL_6, LVL_7, LVL_8, LVL_9]

SCORE = 0

# ---------------------------------------#

COLUMNS = 14
ROWS = 24
LEFT = 0
RIGHT = LEFT + COLUMNS
MIDDLE = LEFT + COLUMNS // 2
TOP = 1
FLOOR = TOP + ROWS


#
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 20, 47)
LAM = (110, 255, 197)
YELLOW = (255, 255, 99)
GREEN=(71,240,59)
VIOLET=(226,34,220)
list_color = (WHITE, RED, PINK, LAM, YELLOW,GREEN,VIOLET)
# -------------IMAGES and MUSIC--------------------#

pygame.mixer.set_num_channels(6)
BLUE=(0,255,0)

# Channel 0: Background Music
# Channel 1: Block Rotation
# Channel 2: Force Hit
# Channel 3: Line Remove
# Channel 4: Slow Hit
# Channel 5: Tetris Remove


# ---- BACKGROUND IMAGES ---- #
tetris_img = pygame.image.load('images/Tetris.jpg')
grid_img = pygame.image.load('images/gridBG.png')

intro_screen = pygame.image.load('images/Intro.jpg')
outro_screen = pygame.image.load('images/Outro.jpg')
RICARDO=pygame.image.load('images/ricardo.png')
boxmess=pygame.image.load('images/box.png')
# --------------------------- #

# ---- SOUND EFFECTS ---- #
block_rotate = pygame.mixer.Sound('Sounds/block-rotate.ogg')
force_hit = pygame.mixer.Sound('Sounds/force-hit.ogg')
line_remove = pygame.mixer.Sound('Sounds/line-remove.ogg')
slow_hit = pygame.mixer.Sound('Sounds/slow-hit.ogg')
tetris_remove = pygame.mixer.Sound('Sounds/tetris-remove.ogg')
# ----------------------- #

# ---- BACKGROUND MUSIC ---- #
kalinka = pygame.mixer.Sound('Music/kalinka.ogg')
katyusha = pygame.mixer.Sound('Music/katyusha.ogg')
korobushka = pygame.mixer.Sound('Music/korobushka.ogg')
smuglianka = pygame.mixer.Sound('Music/smuglianka.ogg')

bg_music = choice([kalinka, katyusha, korobushka, smuglianka])
# -------------------------- #

# ---- BLOCK PREVIEWS ---- #
cube_block = pygame.image.load('Previews/cube-block.png').convert_alpha()
i_block = pygame.image.load('Previews/i-block.png').convert_alpha()
j_block = pygame.image.load('Previews/j-block.png').convert_alpha()
L_block = pygame.image.load('Previews/L-block.png').convert_alpha()
r_s_block = pygame.image.load('Previews/r-s-block.png').convert_alpha()
s_block = pygame.image.load('Previews/s-block.png').convert_alpha()
t_block = pygame.image.load('Previews/t-block.png').convert_alpha()

block_img_lst = [r_s_block, s_block, L_block, j_block, i_block, t_block, cube_block]  # MUST MATCH LIST IN CLASSES.PY
# ------------------------ #

# ---- FAVICON ---- #
favicon = pygame.image.load('images/favicon.png').convert_alpha()
pygame.display.set_icon(favicon)
# ----------------- #

# ---- FONTS ---- #
pygame.font.init()
my_font = pygame.font.SysFont('Arial Black', 21)


# --------------- #

# ------------- FUNCTIONS -------------------- #

def createText(text,x,y,color,size):
    font = pygame.font.Font(None, size)
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface,(x,y))
def draw_grid():
    """ Draw horisontal and vertical lines on the entire game window.
        Space between the lines is GRIDSIZE.
    """
    for i in range(15):
        pygame.draw.line(screen, BLACK, (i * GRIDSIZE, 0), (i * GRIDSIZE, HEIGHT), 1)

    for i in range(24):
        pygame.draw.line(screen, BLACK, (0, i * GRIDSIZE), (GRIDSIZE * 24, i * GRIDSIZE), 1)


def redraw_screen():
    score_text = my_font.render(str(SCORE), True, WHITE)
    timer_text = my_font.render(str(round(pygame.time.get_ticks() / 1000, 2)), True, WHITE)
    level_text = my_font.render(str(level + 1), True, WHITE)

    screen.blit(grid_img, (0, 0))
    draw_grid()
    screen.blit(tetris_img, (GRIDSIZE * 14, 0))
    shape.draw(screen, GRIDSIZE)
    shadow.draw(screen, GRIDSIZE, True)
    obstacles.draw(screen, GRIDSIZE)

    # BLIT FONTS
    screen.blit(score_text, ((GRIDSIZE * 14) + 90, 460))
    screen.blit(timer_text, ((GRIDSIZE * 14) + 85, 538))
    screen.blit(level_text, ((GRIDSIZE * 14) + 100, 380))

    # BLIT NEXT SHAPE
    screen.blit(block_img_lst[nextShapeNo - 1], ((GRIDSIZE * 14) + 72, 240))

    pygame.display.flip()


def drop(my_shape):
    flow = False
    while not flow:
        my_shape.move_down()
        if my_shape.collides(floor) or my_shape.collides(obstacles):
            my_shape.move_up()
            flow = True

    if not my_shape.shadow:
        pygame.mixer.Channel(2).play(force_hit)

# Game Initialization

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=600
screen_height=575

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
white=yellow
# Game Fonts
font = "astron-boy.ttf"


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
menu=True
selected="start"

while menu:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and selected == 'high score':
                selected="start"
            elif event.key==pygame.K_DOWN and selected == 'high score':
                selected='quit'
            elif event.key==pygame.K_UP and selected == 'quit':
                selected="high score"
            elif event.key == pygame.K_DOWN and selected == 'start':
                selected ='high score'
            elif event.key == pygame.K_UP and selected == 'start':
                selected = 'quit'
            elif event.key == pygame.K_DOWN and selected == 'quit':
                selected = 'start'
            if event.key==pygame.K_RETURN:
                if selected=="start":
                    counter = 0

                    shapeNo = randint(1, 7)
                    nextShapeNo = randint(1, 7)

                    shape = Shape(MIDDLE, TOP, shapeNo)
                    floor = Floor(LEFT, ROWS, COLUMNS)
                    leftWall = Wall(LEFT - 1, 0, ROWS)
                    rightWall = Wall(RIGHT, 0, ROWS)
                    obstacles = Obstacles(LEFT, FLOOR)
                    inPlay = False
                    hasPlayed = False
                    level = 0

                    PREV_TETRIS = False

                    pygame.mixer.Channel(0).play(bg_music, -1)

                    # ---- INTRO SCREEN ---- #
                    while not inPlay and not hasPlayed:
                        screen.blit(intro_screen, (0, 0))
                        pygame.display.flip()

                        screen.blit(intro_screen, (0, 0))
                        pygame.display.flip()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    font = pygame.font.Font(None, 32)
                                    clock = pygame.time.Clock()
                                    input_box = pygame.Rect(70, 300, 200, 35)
                                    color_inactive = pygame.Color('lightskyblue3')
                                    color_active = pygame.Color('dodgerblue2')
                                    color = color_inactive
                                    active = False
                                    text = ''
                                    done = False

                                    while not done:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                done = True
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                # If the user clicked on the input_box rect.
                                                if input_box.collidepoint(event.pos):
                                                    # Toggle the active variable.
                                                    active = not active
                                                else:
                                                    active = False
                                                # Change the current color of the input box.
                                                color = color_active if active else color_inactive
                                            if event.type == pygame.KEYDOWN:
                                                if active:
                                                    if event.key == pygame.K_RETURN:
                                                        # print(text)
                                                        NAME = text
                                                        done = True
                                                    elif event.key == pygame.K_BACKSPACE:
                                                        text = text[:-1]
                                                    else:
                                                        text += event.unicode
                                        screen.blit(grid_img, (0, 0))
                                        screen.blit(RICARDO, (0, -50))
                                        screen.blit(boxmess, (50, 100))
                                        what_Name = "What 's "
                                        name = "your name??"
                                        createText(what_Name, 120, 140, WHITE, 45)
                                        createText(name, 80, 190, WHITE, 45)
                                        pygame.display.flip()
                                        # Render the current text.
                                        txt_surface = font.render(text, True, WHITE)
                                        # Resize the box if the text is too long.
                                        width = max(200, txt_surface.get_width() + 10)
                                        input_box.w = width
                                        # Blit the text.
                                        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                                        # Blit the input_box rect.
                                        pygame.draw.rect(screen, color, input_box, 5)

                                        pygame.display.flip()
                                        clock.tick(30)
                                    # pygame.quit()

                                    inPlay = True
                                    hasPlayed = True

                    # ---------------------- #
                    while inPlay:

                        shadow = Shape(shape.col, shape.row, shape.clr, shape._rot, True)
                        drop(shadow)

                        if counter % LEVELS[level] == 0:
                            shape.move_down()
                            if shape.collides(floor) or shape.collides(obstacles):
                                shape.move_up()
                                obstacles.append(shape)
                                pygame.mixer.Channel(5).play(slow_hit)
                                fullRows = obstacles.findFullRows(TOP, FLOOR, COLUMNS)

                                # --------- CHECK --------- #
                                if 4 > len(fullRows) > 0:
                                    SCORE += 100 * len(fullRows)
                                    pygame.mixer.Channel(3).play(line_remove)
                                elif len(fullRows) >= 4:
                                    SCORE += 800 + (100 * (len(fullRows) - 4))
                                    pygame.mixer.Channel(4).play(tetris_remove)
                                    PREV_TETRIS = True
                                elif len(fullRows) >= 4 and PREV_TETRIS:
                                    SCORE += 1200 + (100 * (len(fullRows) - 4))
                                    PREV_TETRIS = True
                                    pygame.mixer.Channel(4).play(tetris_remove)
                                # ------------------------ #

                                obstacles.removeFullRows(fullRows)
                                shapeNo = nextShapeNo
                                nextShapeNo = randint(1, 7)
                                if not shape.row <= 1:
                                    shape = Shape(MIDDLE, TOP, shapeNo)
                                else:
                                    inPlay = False

                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                inPlay = False
                            if event.type == pygame.MOUSEBUTTONUP:
                                start = event.pos
                                if (start[0] >= 400 and start[0] <= 532 and start[1] >= 15 and start[1] <= 170):
                                    text = "Press SPACE to continue!!!"

                                    rect = pygame.Rect(40, 240, 295, 45)
                                    pygame.draw.rect(screen, BLACK, rect)

                                    while True:
                                        R = randint(0, 255)
                                        G = randint(0, 255)
                                        B = randint(0, 255)
                                        createText(text, 50, 250, (R, G, B), 30)
                                        pygame.display.update()
                                        k = 0.1
                                        qu = 1
                                        time.sleep(k)
                                        for event1 in pygame.event.get():
                                            if event1.type == pygame.KEYDOWN:
                                                if event1.key == pygame.K_SPACE:
                                                    qu = 0
                                                    print(k)
                                                    break
                                            if event1.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit(0)
                                        if qu == 0:
                                            break
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                    shape.rotateClkwise()
                                    shape._rotate()
                                    if shape.collides(leftWall) or shape.collides(rightWall) or shape.collides(
                                            floor) or shape.collides(
                                            obstacles):
                                        shape.rotateCntclkwise()
                                        shape._rotate()
                                    else:
                                        pygame.mixer.Channel(1).play(block_rotate)

                                if event.key == pygame.K_LEFT:
                                    shape.move_left()
                                    if shape.collides(leftWall):
                                        shape.move_right()
                                    elif shape.collides(obstacles):
                                        shape.move_right()

                                if event.key == pygame.K_RIGHT:
                                    shape.move_right()
                                    if shape.collides(rightWall):
                                        shape.move_left()
                                    elif shape.collides(obstacles):
                                        shape.move_left()

                                if event.key == pygame.K_DOWN:
                                    shape.move_down()
                                    if shape.collides(floor) or shape.collides(obstacles):
                                        shape.move_up()
                                        obstacles.append(shape)
                                        fullRows = obstacles.findFullRows(TOP, FLOOR, COLUMNS)
                                        # --------- CHECK --------- #
                                        if 4 > len(fullRows) > 0:
                                            SCORE += 100 * len(fullRows)
                                            pygame.mixer.Channel(3).play(line_remove)
                                        elif len(fullRows) >= 4:
                                            SCORE += 800 + (100 * (len(fullRows) - 4))
                                            pygame.mixer.Channel(4).play(tetris_remove)
                                            PREV_TETRIS = True
                                        elif len(fullRows) >= 4 and PREV_TETRIS:
                                            SCORE += 1200 + (100 * (len(fullRows) - 4))
                                            PREV_TETRIS = True
                                            pygame.mixer.Channel(4).play(tetris_remove)
                                        # ------------------------- #

                                        obstacles.removeFullRows(fullRows)
                                        shapeNo = nextShapeNo
                                        nextShapeNo = randint(1, 7)
                                        shape = Shape(MIDDLE, TOP, shapeNo)
                                        shape = Shape(MIDDLE, TOP, shapeNo)

                                if event.key == pygame.K_SPACE:
                                    drop(shape)
                                    obstacles.append(shape)
                                    shapeNo = nextShapeNo
                                    nextShapeNo = randint(1, 7)
                                    shape = Shape(MIDDLE, TOP, shapeNo)
                                    fullRows = obstacles.findFullRows(TOP, FLOOR, COLUMNS)
                                    # --------- CHECK --------- #
                                    if 4 > len(fullRows) > 0:
                                        SCORE += 100 * len(fullRows)
                                        pygame.mixer.Channel(3).play(line_remove)
                                    elif len(fullRows) >= 4:
                                        SCORE += 800 + (100 * (len(fullRows) - 4))
                                        pygame.mixer.Channel(4).play(tetris_remove)
                                        PREV_TETRIS = True
                                    elif len(fullRows) >= 4 and PREV_TETRIS:
                                        SCORE += 1200 + (100 * (len(fullRows) - 4))
                                        PREV_TETRIS = True
                                        pygame.mixer.Channel(4).play(tetris_remove)
                                    # ------------------------- #
                                    obstacles.removeFullRows(fullRows)

                        if 2000 >= SCORE >= 500:
                            level = 1
                        elif 4500 >= SCORE > 2000:
                            level = 2
                        elif 7000 >= SCORE > 4500:
                            level = 3
                        elif 10000 >= SCORE > 7000:
                            level = 4
                        elif 12500 >= SCORE > 10000:
                            level = 5
                        elif 17750 >= SCORE > 12500:
                            level = 6
                        elif 30000 >= SCORE > 17750:
                            level = 7
                        elif 32500 >= SCORE > 30000:
                            level = 8
                        elif SCORE >= 32500:
                            level = 9

                        PREV_TETRIS = False
                        counter += 1
                        redraw_screen()

                    while not inPlay and hasPlayed:
                        start_timer = pygame.time.get_ticks()
                        screen.blit(outro_screen, (0, 0))
                        pygame.display.flip()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    pygame.quit()
                                    sys.exit(0)

                            if pygame.time.get_ticks() - start_timer >= 200000000:
                                pygame.quit()
                                sys.exit(0)

                if selected=='high score':

                if selected=="quit":
                    pygame.quit()
                    quit()


    # Main Menu UI
    back=pygame.image.load('images/background.jpg')
    screen.blit(back,(0,0))

    title=text_format("Tetris", font, 90, yellow)
    if selected=="start":
        text_start=text_format("NEW GAME", font, 75, white)
    else:
        text_start = text_format("NEW GAME", font, 75, black)
    if selected=="high score":
        text_highscore = text_format("HIGH SCORE", font, 75, white)
    else:
        text_highscore = text_format("HIGH SCORE", font, 75, black)
    if selected=="quit":
        text_quit=text_format("QUIT", font, 75, white)
    else:
        text_quit = text_format("QUIT", font, 75, black)

    title_rect=title.get_rect()
    start_rect=text_start.get_rect()
    highscore_rect = text_highscore.get_rect()
    quit_rect=text_quit.get_rect()

    # Main Menu Text

    screen.blit(text_start, (screen_width//2 - (start_rect[2]//2), 360))
    screen.blit(text_highscore, (screen_width//2 - (highscore_rect[2]//2), 420))
    screen.blit(text_quit, (screen_width//2 - (quit_rect[2]//2), 480))
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.set_caption("Tetris")

#Initialize the Game
pygame.quit()
quit()