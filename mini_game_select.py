from tkinter import *

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

        # create tetris interest button
        # self.tetris_bttn = Button(self, text = "Tetris", command = self.kill("Tetris"))
        self.tetris_bttn = Button(self, text = "Tetris", command = self.kill)
        self.tetris_bttn.grid(row = 8, column = 0, sticky = E)


    def kill(self):
        self.callback()
