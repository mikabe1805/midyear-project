import tkinter

from mini_game_select import Application
from tetris_main import Tetris

class manager (object):

    def __init__ (self):
        self.root = tkinter.Tk()
        self.current_screen = None

    def setup_first (self):
        '''
        This method is called to set up the Character Selection screen. 
        This also initializes the character_roster property.
        '''
        # Changes the window's title
        self.root.title ("mini game select")
        # Creates and displays a Character Selection screen
        self.current_screen = Application(master = self.root, 
                                                        callback_on_selected = self.onclose_character_selection
                                                        )
    
    def onclose_character_selection (self):
        
        # Destroys the Character Selection window
        self.current_screen.destroy()


        # if game == "Tetris":
            # Continue on - set up the Prepare To Battle screen!
        self.setup_tetris()

    def setup_tetris(self):
        # Changes the window's title
        self.root.title ("Tetris")

        # Creates and displays a Prepare To Battle screen
        self.current_screen = Tetris(master = self.root, character = 'nagito', callback_on_selected = self.onclose_tetris)

    def onclose_tetris (self):
        
        # Destroys the Character Selection window
        self.current_screen.destroy()


        # if game == "Tetris":
            # Continue on - set up the Prepare To Battle screen!
        self.setup_first()

def main():
    # Create the battle manager, which creates the tkinter window.
    battle = manager()
    # The program begins with the Character Selection screen!
    battle.setup_first()
    # Run the program!
    battle.root.mainloop()
 
main()