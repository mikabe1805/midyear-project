from tkinter import *
import pygame

class Application(Frame):
    """ GUI application which calculates interest. """
    def __init__(self, master, callback_on_selected, returnn):
        """ Initialize the frame. """
        super().__init__(master)
        self.base = master
        self.callback = callback_on_selected
        self.returnn = returnn
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        self.character_index = StringVar()
        self.character_index.set(None)

        # create tetris button
        self.tetris_bttn = Button(self, text = "Tetris", command = self.tetris)
        # self.tetris_bttn = Button(self, text = "Tetris", command = self.kill)
        self.tetris_bttn.grid(row = 8, column = 0, sticky = W)

        # create breakout button
        self.tetris_bttn = Button(self, text = "Breakout", command = self.breakout)
        self.tetris_bttn.grid(row = 9, column = 0, sticky = W)

        self.tetris_bttn = Button(self, text = "Pong", command = self.pong)
        self.tetris_bttn.grid(row = 10, column = 0, sticky = W)
        
        self.tetris_bttn = Button(self, text = "Space Invaders", command = self.spaceinvaders)
        self.tetris_bttn.grid(row = 11, column = 0, sticky = W)

        # #This button can close the window
        # self.button_1 = Button(self.base, text ="I close the Window", command = self.base.destroy)
        # #Exteral paddign for the buttons
        # self.button_1.grid(row = 11, column = 0, sticky = W)

        # create . button
        self.tetris_bttn = Button(self, text = ".", command = self.cheat)
        self.tetris_bttn.grid(row = 12, column = 0, sticky = W)

        # empty label for spacing
        Label(self, text = "").grid(row = 13, column = 0)

        # empty label for spacing
        Label(self, text = "").grid(row = 14, column = 0)

        # empty label for spacing
        Label(self, text = "").grid(row = 15, column = 0)

        # create back to character select button
        self.tetris_bttn = Button(self, text = "back to character select", fg = "white", bg = "grey", command = self.returnn)
        self.tetris_bttn.grid(row = 15, column = 2, sticky = W)


    def tetris(self):
        self.character_index = "Tetris"
        self.callback(self.character_index)
        pygame.quit()
        # self.base.destroy()


    def breakout(self):
        self.character_index = "Breakout"
        self.callback(self.character_index)
        pygame.quit()
    
    def pong(self):
        self.character_index = "Pong"
        self.callback(self.character_index)
        pygame.quit()

    def spaceinvaders(self):
        self.character_index = "Space Invaders"
        self.callback(self.character_index)
        pygame.quit()
    
    def cheat(self):
        self.character_index = "cheat"
        self.callback(self.character_index)
        pygame.quit()
