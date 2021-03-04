from tkinter import *

class Screen_CharacterSelection (Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
        self.roster = roster
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        self.character_index = StringVar()
        self.character_index.set(None)

        # empty label for spacing
        Label(self, text = "").grid(row = 1, column = 3)

        # create char radio buttons
        row = 2
        for char in self.roster.character_list:
            # create radio button and name
            if char.name == "junko enoshima":
                Radiobutton(self, text = "junko", variable = self.character_index, value = row-2).grid(row = row, column = 1, sticky = W)
            else:
                Radiobutton(self, text = char.name, variable = self.character_index, value = row-2).grid(row = row, column = 1, sticky = W)

            # create an image of the character
            imageSmall = PhotoImage(file="sprites/" + char.name + "/lil.png")
            w= Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall
            # grid the image
            w.grid(row = row, column = 2)

            row += 1

        # create character selected button!
        Button(self, text = "READY", fg = "white", bg = "grey", command = self.selected_clicked).grid(row = row, column = 4, columnspan = 2, sticky = E)

    def selected_clicked(self):
        self.callback_on_selected(self.character_index.get())         