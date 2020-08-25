import sys
from random import randint, choice
from pygame.locals import *
import time
from Classes import *

pygame.init()

HEIGHT = 600
WIDTH = 575
GRIDSIZE = HEIGHT // 24
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TeTrIs_cUk_mAnK")

LVL_1, LVL_2, LVL_3, LVL_4, LVL_5, LVL_6, LVL_7, LVL_8, LVL_9 = 45, 20, 10, 7, 5, 4, 3, 2, 1

LEVELS = [LVL_1, LVL_2, LVL_3, LVL_4, LVL_5, LVL_6, LVL_7, LVL_8, LVL_9]

SCORE = 0

NAME=''
SCORES=0
# ---------------------------------------#

COLUMNS = 14
ROWS = 24
LEFT = 0
RIGHT = LEFT + COLUMNS
MIDDLE = LEFT + COLUMNS // 2
TOP = 1
FLOOR = TOP + ROWS

# -------------IMAGES and MUSIC--------------------#

pygame.mixer.set_num_channels(6)

# Channel 0: Background Music
# Channel 1: Block Rotation
# Channel 2: Force Hit
# Channel 3: Line Remove
# Channel 4: Slow Hit
# Channel 5: Tetris Remove


# ---- BACKGROUND IMAGES ---- #
tetris_img = pygame.image.load('images/Tetris.jpg')
grid_img = pygame.image.load('images/gridbg.png')

intro_screen = pygame.image.load('images/Intro.jpg')
outro_screen = pygame.image.load('images/Outro.jpg')
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


def draw_grid():
    """ Draw horisontal and vertical lines on the entire game window.
        Space between the lines is GRIDSIZE.
    """
    for i in range(15):
        pygame.draw.line(screen, BLACK, (i * GRIDSIZE, 0), (i * GRIDSIZE, HEIGHT), 1)

    for i in range(24):
        pygame.draw.line(screen, BLACK, (0, i * GRIDSIZE), (GRIDSIZE * 24, i * GRIDSIZE), 1)

def Rankings():
    with open("HighScores.txt", "r") as f:
        my = [line.strip() for line in f]
    pygame.init()
    screen = pygame.display.set_mode((600, 575), 0, 32)
    pygame.display.set_caption('Drawing')

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('#', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 25)
    screen.blit(textSurfaceObj, textRectObj)

    pygame.draw.rect(screen, BLACK, (10, 10, 550, 330), 1)
    pygame.draw.line(screen, BLACK, (10, 40), (560, 40))
    pygame.draw.line(screen, BLACK, (35, 10), (35, 340))
    pygame.draw.line(screen, BLACK, (290, 10), (290, 340))
    pygame.draw.line(screen, BLACK, (10, 70), (560, 70))
    pygame.draw.line(screen, BLACK, (10, 100), (560, 100))
    pygame.draw.line(screen, BLACK, (10, 130), (560, 130))
    pygame.draw.line(screen, BLACK, (10, 160), (560, 160))
    pygame.draw.line(screen, BLACK, (10, 190), (560, 190))
    pygame.draw.line(screen, BLACK, (10, 220), (560, 220))
    pygame.draw.line(screen, BLACK, (10, 250), (560, 250))
    pygame.draw.line(screen, BLACK, (10, 280), (560, 280))
    pygame.draw.line(screen, BLACK, (10, 310), (560, 310))

    textSurfaceObj = fontObj.render('1', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 55)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('2', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 85)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('3', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 115)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('4', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 145)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('5', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 175)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('6', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 205)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('7', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 235)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('8', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 265)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('9', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 295)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('10', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 325)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('Name', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (160, 25)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('Score', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (420, 25)
    screen.blit(textSurfaceObj, textRectObj)

    xi = 160
    yi = 55
    for i in range(0, len(my),2):
        textSurfaceObj = fontObj.render(my[i], True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (xi, yi)
        screen.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render(my(i+1), True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (xi + 260, yi)
        screen.blit(textSurfaceObj, textRectObj)
        yi += 30
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

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


# -------------------------------------------- #

# ------------- MAIN PROGRAM -------------------- #

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
rankings = False
level = 0

PREV_TETRIS = False

pygame.mixer.Channel(0).play(bg_music, -1)

# ---- INTRO SCREEN ---- #
while not inPlay and not hasPlayed:
    screen.blit(intro_screen, (0, 0))
    pygame.display.flip()

    screen.blit(intro_screen, (0, 0))
    pygame.display.flip()
    clgt = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                with open("HighScores.txt", "r") as f:
                    my = [line.strip() for line in f]
                a=[]
                tmp=[]
                for i in range (0,len(my),2):
                    #c=str(my[i+1])
                    b=[my[i],int(my[i+1])]
                    tmp.append(b)
                tmp.sort(key=lambda x: x[-1],reverse=True)
                print(tmp)
                for i in range (0,len(tmp),1):
                    c=str(tmp[i][1])
                    b=[tmp[i][0],c]
                    a.append(b)

                print(a)
                #print("dskghsdg")
                pygame.init()
                screen.fill(WHITE)
                pygame.display.set_caption('Drawing')

                BLACK = (0, 0, 0)
                WHITE = (255, 255, 255)
                RED = (255, 0, 0)
                GREEN = (0, 255, 0)
                BLUE = (0, 0, 255)



                fontObj = pygame.font.Font('freesansbold.ttf', 20)
                textSurfaceObj = fontObj.render('#', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 25)
                screen.blit(textSurfaceObj, textRectObj)
                #screen.fill(WHITE)
                pygame.draw.rect(screen, BLACK, (10, 10, 550, 330), 1)
                pygame.draw.line(screen, BLACK, (10, 40), (560, 40))
                pygame.draw.line(screen, BLACK, (35, 10), (35, 340))
                pygame.draw.line(screen, BLACK, (290, 10), (290, 340))
                pygame.draw.line(screen, BLACK, (10, 70), (560, 70))
                pygame.draw.line(screen, BLACK, (10, 100), (560, 100))
                pygame.draw.line(screen, BLACK, (10, 130), (560, 130))
                pygame.draw.line(screen, BLACK, (10, 160), (560, 160))
                pygame.draw.line(screen, BLACK, (10, 190), (560, 190))
                pygame.draw.line(screen, BLACK, (10, 220), (560, 220))
                pygame.draw.line(screen, BLACK, (10, 250), (560, 250))
                pygame.draw.line(screen, BLACK, (10, 280), (560, 280))
                pygame.draw.line(screen, BLACK, (10, 310), (560, 310))

                textSurfaceObj = fontObj.render('1', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 55)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('2', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 85)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('3', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 115)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('4', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 145)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('5', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 175)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('6', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 205)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('7', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 235)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('8', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 265)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('9', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 295)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('10', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (22, 325)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('Name', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (160, 25)
                screen.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = fontObj.render('Score', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (420, 25)
                screen.blit(textSurfaceObj, textRectObj)

                xi = 160
                yi = 55
                for i in range(0, 10, 1):
                    textSurfaceObj = fontObj.render(a[i][0], True, BLACK, WHITE)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (xi, yi)
                    screen.blit(textSurfaceObj, textRectObj)
                    textSurfaceObj = fontObj.render(a[i][1], True, BLACK, WHITE)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (xi + 260, yi)
                    screen.blit(textSurfaceObj, textRectObj)
                    yi += 30
                    print("sad")
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                            #pygame.quit()
                                clgt = 1
                                break
                    if(clgt == 1):
                        break
                        #pygame.display.update()
            if event.key == pygame.K_SPACE:
                    font = pygame.font.Font(None, 32)
                    clock = pygame.time.Clock()
                    input_box = pygame.Rect(100, 100, 140, 32)
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
                                        NAME=text
                                        done = True
                                    elif event.key == pygame.K_BACKSPACE:
                                        text = text[:-1]
                                    else:
                                        text += event.unicode

                        screen.fill((30, 30, 30))
                        # Render the current text.
                        txt_surface = font.render(text, True, color)
                        # Resize the box if the text is too long.
                        width = max(200, txt_surface.get_width() + 10)
                        input_box.w = width
                        # Blit the text.
                        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                        # Blit the input_box rect.
                        pygame.draw.rect(screen, color, input_box, 2)

                        pygame.display.flip()
                        clock.tick(30)
                    #pygame.quit()
                    if(clgt == 0):
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                shape.rotateClkwise()
                shape._rotate()
                if shape.collides(leftWall) or shape.collides(rightWall) or shape.collides(floor) or shape.collides(
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

    if 1000 >= SCORE >= 500:
        level = 1
    elif 1500 >= SCORE > 1000:
        level = 2
    elif 2000 >= SCORE > 1500:
        level = 3
    elif 2250 >= SCORE > 2000:
        level = 4
    elif 2500 >= SCORE > 2250:
        level = 5
    elif 2750 >= SCORE > 2500:
        level = 6
    elif 3000 >= SCORE > 2750:
        level = 7
    elif 3250 >= SCORE > 3000:
        level = 8
    elif SCORE >= 3250:
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
            with open("HighScores.txt", "a+") as fo:
                fo.write(NAME + "\n" +str(SCORE)+"\n")
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                with open("HighScores.txt", "a+") as fo:
                    fo.write(NAME + "\n" +str(SCORE)+"\n")
                pygame.quit()
                sys.exit(0)

        if pygame.time.get_ticks() - start_timer >= 2000:
            with open("HighScores.txt", "a+") as fo:
                fo.write(NAME + "\n" +str(SCORE)+"\n")
            pygame.quit()
            sys.exit(0)

# ----------------------------------------------- #

sys.exit("Exited Final")
