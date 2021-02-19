from pygame_functions import *
from tkinter import *
import pygame as pg


class cheat(Frame):
    """ GUI application which calculates interest. """
    def __init__(self, master, callback_on_selected):
        """ Initialize the frame. """
        super().__init__(master)
        self.callback = callback_on_selected
        self.grid()
        self.cheat()

    def cheat(self):
        screenSize(320, 200)

        cheatBox = makeTextBox(10, 80, 300, 0, "", 0, 24)
        showTextBox(cheatBox)
        entry = textBoxInput(cheatBox)
        self.callback(entry)