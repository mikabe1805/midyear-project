# I hate github
# I still hate github
# image of mikan will not show up until player starts losing
import pygame
import random
import simpleaudio as sa
from tkinter import *
import cv2
import numpy as np
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer

class Tetris(Frame):
   """ I'm trying ;-; """
   def __init__(self, master, character, limit, x, y, x2, callback_on_selected):
        super().__init__(master)
        self.callback = callback_on_selected
        self.character = character
        self.limit = limit
        self.x = x
        self.y = y
        self.x2 = x2
        self.grid()
        # self.play_tetris()

   def play_tetris(self):
 
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

        # last left off
        # gggg
        def check_losing1(positions):
            # problem: only works once
            # update: I'm an idiot.
            for pos in positions:
                x, y = pos
                if y < 12:
                    return True

            return False

        def check_losing2(positions):
            # problem: only works once
            # update: I'm an idiot.
            for pos in positions:
                x, y = pos
                if y < 8:
                    return True

            return False

        def check_losing3(positions):
            # problem: only works once
            # update: I'm an idiot.
            for pos in positions:
                x, y = pos
                if y < 3:
                    return True

            return False

        
        def get_shape():
            return Piece(5, 0, random.choice(shapes))

        def draw_text_middle(text, size, color, surface):
            font = pygame.font.Font('goodbyeDespair.ttf', size, bold=True)
            label = font.render(text, 1, color)
            surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + (play_height/16)*7 - label.get_height()/2))

        def draw_text_middle2(text, text2, size, color, surface):
            font = pygame.font.Font('goodbyeDespair.ttf', size, bold=True)
            label = font.render(text, 1, color)
            surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + (play_height/16)*3 - label.get_height()/2))

            font = pygame.font.Font('goodbyeDespair.ttf', size, bold=True)
            label = font.render(text2, 1, color)
            surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + (play_height/8)*5 - label.get_height()/2))
        
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
            # copy this code and make it into a function named "check" to see if the player is losing
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

            return inc
        
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

        def update_score(nscore):
            score = max_score()

            with open('tetris_scores.txt', 'w') as f:
                if int(score) > nscore:
                    f.write(str(score))
                else:
                    f.write(str(nscore))

        def max_score():
            # with open('tetris_scores.txt', 'r') as f:
            #     lines = f.readline()
            #     score = lines[0].strip()
            f = open('tetris_scores.txt')
            for line in f:
                score = line.strip()

            return score

        self.s = 1
        # 88 is one beat
        # 3 short beats one long beat??
        self.idk = 188
        self.load = 2
        def draw_window(surface, grid, score=0, high_score=0):
            surface.fill((0, 0, 0))
            pygame.font.init()
            # font = os.path.abspath("C:/Users/mikus/Downloads/goodbyeDespair.ttf")
            # font = pygame.font.Font('C:/Users/mikus/Downloads/goodbyeDespair.ttf', 60)
            font = pygame.font.Font('goodbyeDespair.ttf', 60)
            label = font.render('Tetris', 1, (255, 255, 255))

            surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))
            
            # current score
            font = pygame.font.Font('goodbyeDespair.ttf', 30)
            label = font.render('Score: ' + str(score), 1, (255, 255, 255))

            sx = top_left_x + play_width + 50
            sy = top_left_y + play_height/2 - 100

            surface.blit(label, (sx + 20, sy + 250))

            # high score
            label = font.render('HS: ' + high_score, 1, (255, 255, 255))

            sx = top_left_x - 250
            sy = top_left_y - 79

            surface.blit(label, (sx + 20, sy + 250))
            
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)
            
            # gggg
            if not check_losing1(self.locked_positions):
                # changes sprite with the beat
                if self.counter == self.idk:
                    # make it so sprites won't repeat, breaking the beat
                    self.load = random.choice([i for i in range(1,self.limit) if i not in [self.load]])
                    self.counter = 0
                spr = pygame.image.load('sprites/'+self.character+'/happy'+str(self.load)+'.png')
                spr.set_alpha(100)
                regularMusic()
                if self.play == 1:
                    self.play_obj.stop()
                    self.play = 0
                # spr.set_alpha(self.s/50)
                # if self.s < 5000:
                #     self.s += 1

                surface.blit(spr, (self.x,self.y))
                self.counter += 1


            if check_losing1(self.locked_positions):
                # spr.destroy()
                spr = pygame.image.load('sprites/'+self.character+'/scary.png')
                spr.set_alpha(100)
                self.play2 = 0
                self.play_obj2.stop()
                PTA()
                # spr.set_alpha(self.s/50)
                # if self.s < 5000:
                #     self.s += 1

                surface.blit(spr, (self.x, self.y))
                

            # if check_losing2(self.locked_positions):
            #     transparent = (0, 0, 0, 0)
            #     spr.fill(transparent)
            # not what I tried tp do, but interesting effect ^^^

            # color represents outside of play area (the grid)
            pygame.draw.rect (surface, (255, 106, 0), (top_left_x, top_left_y, play_width, play_height), 4)

            draw_grid(surface, grid)
            # pygame.display.update()


            if check_losing2(self.locked_positions):
                spr = pygame.image.load('sprites/'+self.character+'/scary.png')
                spr.set_alpha(100)
                surface.blit(spr, (self.x, self.y))

            # if check_losing3(self.locked_positions):
            #     spr = pygame.image.load('sprites/mikan/mikan_sad.png')
            #     spr_big = pygame.transform.rotozoom(spr, 0, 3.5)
            #     # surface.blit(spr_big, (80,240))
            #     surface.blit(spr_big, (-90,120))

        self.play2 = 0
        self.play = 0

        def regularMusic():
            if self.play2 == 0:
                filename = 'voice_lines/'+self.character+'/happy.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                self.play_obj2 = wave_obj.play()
            if self.play_obj2.is_playing():
                self.play2 = 1
            else:
                self.play2 = 0
            if self.play == 1:
                self.play_obj2.stop()


        def PTA():
            if self.play == 0:
                # change to self.character later
                filename = 'voice_lines/'+self.character+'/angry.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                self.play_obj = wave_obj.play()
            if self.play_obj.is_playing():
                self.play = 1
            else:
                self.play = 0

        def PlayVideo(video_path):
            video=cv2.VideoCapture(video_path)
            player = MediaPlayer(video_path)
            while True:
                grabbed, frame=video.read()
                audio_frame, val = player.get_frame()
                if not grabbed:
                    print("End of video")
                    break
                if cv2.waitKey(28) & 0xFF == ord("q"):
                    break
                cv2.imshow("Video", frame)
                if val != 'eof' and audio_frame is not None:
                    #audio
                    img, t = audio_frame
            video.release()
            cv2.destroyAllWindows()


        
        def main(win):
            high_score = max_score()
            self.locked_positions = {}
            grid = create_grid(self.locked_positions)

            change_piece = False
            run = True
            current_piece = get_shape()
            next_piece = get_shape()
            clock = pygame.time.Clock()
            fall_time = 0
            self.fall_speed = 0.25
            level_time = 0
            score = 0

            while run:
                grid = create_grid(self.locked_positions)
                fall_time += clock.get_rawtime()
                level_time += clock.get_rawtime()
                clock.tick()
                #gggg
                # if not check_losing1(self.locked_positions):
                #     regularMusic()
                #     if self.play == 1:
                #         self.play_obj.stop()
                # else:
                #     self.play_obj2.stop()
                #     PTA()
                # if check_losing1(self.locked_positions):
                #     PTA()
                
                # create spr
                # spr = PhotoImage(file="sprites/mikan/mikan_sad.png")
                # w= Label (self,
                #     image = spr, 
                #         )
                # w.photo = spr # saving the image as a property is required for "saving" the image. It's odd.
                # # grid the image
                # w.grid(row = 5, column = 1)

                if level_time/1000 > 5:
                    level_time = 0
                    if self.fall_speed > 0.12:
                        self.fall_speed -= 0.005

                if fall_time/1000 > self.fall_speed:
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
                        # make both the arrows and WASD available
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            current_piece.x -= 1
                            if not(valid_space(current_piece, grid)):
                                current_piece.x += 1
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            current_piece.x += 1
                            if not(valid_space(current_piece, grid)):
                                current_piece.x -= 1
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            current_piece.y += 1
                            if not(valid_space(current_piece, grid)):
                                current_piece.y -= 1
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            current_piece.rotation += 1
                            if not(valid_space(current_piece, grid)):
                                current_piece.rotation -= 1
                        if event.key == pygame.K_SPACE:
                            while valid_space(current_piece, grid):
                                current_piece.y += 1
                            if not(valid_space(current_piece, grid)):
                                current_piece.y -= 1
                            # while valid_space(current_piece, grid):
                            #     current_piece.y += 1
                            # # if not(valid_space(current_piece, grid)):
                            # #     current_piece.y -= 1
                        # for bug fixing
                        if event.key == pygame.K_r:
                            score += 10
                        
                        # deletes all blocks placed
                        if event.key == pygame.K_g:
                            inc = 0
                            for i in range(len(grid)-1, -1, -1):
                                row = grid[i]
                                inc += 1
                                ind = i
                                for j in range(len(row)):
                                    try:
                                        del self.locked_positions[(j, i)]
                                    except:
                                        continue
                            for key in sorted(list(self.locked_positions), key = lambda x: x[1])[::-1]:
                                x,y = key
                                if y < ind:
                                    newkey = (x,y + inc)
                                    self.locked_positions[newkey] = self.locked_positions.pop(key)

                shape_pos = convert_shape_format(current_piece)

                for i in range(len(shape_pos)):
                    x, y = shape_pos[i]
                    if y > -1:
                        grid[y][x] = current_piece.color

                if change_piece:
                    for pos in shape_pos:
                        # our piece is no longer moving
                        p = (pos[0], pos[1])
                        self.locked_positions[p] = current_piece.color
                    current_piece = next_piece
                    next_piece = get_shape()
                    change_piece = False
                    # not sure
                    score += clear_rows(grid, self.locked_positions) * 10

                draw_window(win, grid, score, high_score)
                draw_next_shape(next_piece, win)
                if check_losing3(self.locked_positions):
                    spr = pygame.image.load('sprites/'+self.character+'/scary.png')
                    spr_big = pygame.transform.rotozoom(spr, 0, 3.5)
                    # surface.blit(spr_big, (80,240))
                    win.blit(spr_big, (self.x2,170))
                pygame.display.update()

                if check_lost(self.locked_positions):
                    draw_text_middle2("YOU LOST", "TIME FOR PUNISHMENT", 65, (180, 0, 0), win)
                    pygame.display.update()
                    pygame.time.delay(4000)
                    if self.play2 != 0:
                        self.play_obj2.stop()
                        self.play2 = 0
                    if self.play != 0:
                        self.play_obj.stop()
                        self.play = 0
                    if self.character == "chiaki":
                        if random.randint(1, 4) == 4:
                            video_path="chaikii.mp4"
                            PlayVideo(video_path)
                    # draw_text_middle(win, "TIME FOR PUNISHMENT", 80, (255, 255, 255))
                    run = False
                    update_score(score)

        
        def main_menu(win):
            run = True
            while run:
                win.fill((0, 0, 0))
                # TODO: make it so the font for this is different
                # TODO: add a "return to game select" button
                if self.play != 0:
                    self.play_obj.stop()
                    self.play = 0
                if self.play2 != 0:
                    self.play_obj2.stop()
                    self.play2 = 0
                draw_text_middle('Press Any Key To Play', 60, (255, 255, 255), win)
                self.counter = self.idk
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        if self.play != 0:
                            self.play_obj.stop()
                            self.play = 0
                        if self.play2 != 0:
                            self.play_obj2.stop()
                            self.play2 = 0
                        run = False
                        self.callback()
                        # maybe bring it back to game select over here
                        # pygame.display.quit()
                    if event.type == pygame.KEYDOWN:
                        main(win)

            pygame.display.quit()
        
        win = pygame.display.set_mode((s_width, s_height))
        pygame.display.set_caption('Tetris')
        main_menu(win)  # start game