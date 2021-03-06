class Character (object):
    
    def __init__ (self, name, sprite_num, x, y, x2):
        self.name = name
        self.sprite_num = sprite_num    
        self.x = x
        self.y = y
        self.x2 = x2
        
class CharacterRoster (object):
    def __init__ (self, file_name):
        
        self.character_list = []

        text_file = open(file_name,"r")
        
        for line in text_file:
            line = line.strip()
            my_fields = line.split(":",5)
            character = Character (my_fields[0], int(my_fields[1]), int(my_fields[2]), int(my_fields[3]), int(my_fields[4]))
            self.character_list.append(character)
        
    def get_character (self, i):
        ''' 
        Gets and returns the "ith" Character from the list, then removes the 
        character from the list.  (Removal so prevents the user and computer from 
        using the same character).
        '''
        ch = self.character_list[i]
        return ch
    
    def get_number_of_characters (self):
        ''' Returns the number of Characters in the roster. '''
        return len(self.character_list)

