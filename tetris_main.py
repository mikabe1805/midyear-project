# hi
import pygame
import random
 
# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pygame.font.init()
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 
 
# SHAPE FORMATS
 
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 
# 7
shapes = [S, Z, I, O, J, L, T]
# all the colors, make it nicer >:(
# 7 colors previously
# now 
shape_colors = [(84, 22, 180), (112, 39, 195), (185, 76, 225), (150, 0, 205), (164, 66, 220), (181, 100, 227), (228, 0, 224), (236, 71, 233), (244, 147, 242), (0, 181, 236), (204, 255, 0), (255, 106, 0), (67, 59, 103), (96, 88, 133), (148, 141, 179)]
# index 0 - 6 represent shape
 
 
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        # self.color = shape_colors[random.randint(0, len(shape_colors)-1)]
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0
 
def create_grid(locked_pos={}):
    # 10 squares in each row, 20 rows
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)] 

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid


 
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))


    for i, pos in enumerate(positions):
        # for offsetting to center the piece
        positions[i] = (pos[0] - 2, pos[1]-4)

    return positions
 
def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid [i][j] == (0, 0, 0)] for i in range (20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False
 
def get_shape():
    return Piece(5, 0, random.choice(shapes))
 
 
def draw_text_middle(text, size, color, surface):
    pass
   
def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range (len(grid)):
        # color of grid lines (I can't think of any nicer color guys pls help me ;-;)
        pygame.draw.line(surface, (128, 128, 128), (sx, sy+i*block_size), (sx+play_width, sy+i*block_size))
        for j in range(len(grid[i])):
            # come back to check if works once code is finished
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy), (sx+j*block_size, sy+play_height))
            # pygame.draw.line(surface, (128, 128, 128), (sx, j*block_size, sy), (sx+j*block_size, sy+play_height))
         

def clear_rows(grid, locked):
    # TODO: find a way to shift fallen pieces all the way down
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0,0,0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key = lambda x: x[1])[::-1]:
            x,y = key
            if y < ind:
                newkey = (x,y + inc)
                locked[newkey] = locked.pop(key)
 
def draw_next_shape(shape, surface):
    # maybe problematic font
    font = pygame.font.Font('goodbyeDespair.ttf', 30)
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            # draw blocks according to where they show up
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*block_size, block_size, block_size), 0)
 
    surface.blit(label, (sx + 10, sy - 30))

def draw_window(surface, grid):
    surface.fill((0, 0, 0))

    pygame.font.init()
    # font = os.path.abspath("C:/Users/mikus/Downloads/goodbyeDespair.ttf")
    # font = pygame.font.Font('C:/Users/mikus/Downloads/goodbyeDespair.ttf', 60)
    font = pygame.font.Font('goodbyeDespair.ttf', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)
    
    # color represents outside of play area (the grid)
    pygame.draw.rect (surface, (255, 106, 0), (top_left_x, top_left_y, play_width, play_height), 4)

    draw_grid(surface, grid)
    # pygame.display.update()

 
def main(win):
    
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.25

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # move the pieces
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                # our piece is no longer moving
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            # not sure
            clear_rows(grid, locked_positions)

        draw_window(win, grid)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False
    pygame.display.quit()

 
def main_menu(win):
    main(win)
 
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)  # start game