import tkinter

from mini_game_select import Application
from tetris_main import Tetris
from breakout_main import Breakout
from character_select import Screen_CharacterSelection
from characters import CharacterRoster

class manager (object):

    def __init__ (self):
        self.root = tkinter.Tk()
        self.current_screen = None
    
    def setup_first (self):
        # Changes the window's title
        self.root.title ("Select your character :)")
        # Reads battle_characters.txt to create a CharacterRoster.
        self.character_roster = CharacterRoster ("character_stuff.txt")
        # Creates and displays a Character Selection screen
        self.current_screen = Screen_CharacterSelection(master = self.root, 
                                                        roster = self.character_roster, 
                                                        callback_on_selected = self.onclose_character_selection
                                                        )

    def onclose_character_selection (self, selected_char_index):
           
        selected_char_index = int (selected_char_index)

        # Gets the player's chosen Character
        self.char = self.character_roster.get_character(selected_char_index)
        
        # Destroys the Character Selection window
        self.current_screen.destroy()

        # Continue on - set up the Prepare To Battle screen!
        self.setup_second()

    def setup_second (self):
        '''
        This method is called to set up the Character Selection screen. 
        This also initializes the character_roster property.
        '''
        # Changes the window's title
        self.root.title ("mini game select")
        # Creates and displays a Character Selection screen
        self.current_screen = Application(master = self.root, 
                                                        callback_on_selected = self.onclose_game_selection
                                                        )
    
    def onclose_game_selection (self, game):
        # Destroys the Character Selection window
        self.current_screen.destroy()


        if game == "Tetris":
            # Continue on - set up the Prepare To Battle screen!
            # self.setup_tetris()
            # Changes the window's title
            self.root.title ("Tetris")
            # Creates and displays a Prepare To Battle screen
            self.current_screen = Tetris(master = self.root, character = self.char.name, limit = self.char.sprite_num, callback_on_selected = self.onclose_tetris)

        elif game == "Breakout":
            # self.setup_breakout()
            # Changes the window's title
            self.root.title ("Breakout")
            # Creates and displays a Prepare To Battle screen
            self.current_screen = Breakout(master = self.root, character = self.char.name, callback_on_selected = self.onclose_tetris)

    # def setup_tetris(self):
    #     # Changes the window's title
    #     self.root.title ("Tetris")

    #     # Creates and displays a Prepare To Battle screen
    #     self.current_screen = Tetris(master = self.root, character = 'nagito', callback_on_selected = self.onclose_tetris)

    # def setup_breakout(self):
    #     # Changes the window's title
    #     self.root.title ("Breakout")

    #     # Creates and displays a Prepare To Battle screen
    #     self.current_screen = Breakout(master = self.root, character = 'nagito', callback_on_selected = self.onclose_tetris)

    def onclose_tetris (self):
        
        # Destroys the Character Selection window
        self.current_screen.destroy()


        # if game == "Tetris":
            # Continue on - set up the Prepare To Battle screen!
        self.setup_second()

def main():
    # Create the battle manager, which creates the tkinter window.
    battle = manager()
    # The program begins with the Character Selection screen!
    battle.setup_first()
    # Run the program!
    battle.root.mainloop()
 
main()