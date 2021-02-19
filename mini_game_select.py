from tkinter import *
import pygame

class Application(Frame):
    """ GUI application which calculates interest. """
    def __init__(self, master, callback_on_selected):
        """ Initialize the frame. """
        super().__init__(master)
        self.callback = callback_on_selected
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

        # create . button
        self.tetris_bttn = Button(self, text = ".", command = self.cheat)
        self.tetris_bttn.grid(row = 10, column = 0, sticky = W)


    def tetris(self):
        self.character_index = "Tetris"
        self.callback(self.character_index)

    def breakout(self):
        self.character_index = "Breakout"
        self.callback(self.character_index)
    
    def cheat(self):
        self.character_index = "cheat"
        self.callback(self.character_index)
