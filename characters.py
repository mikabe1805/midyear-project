class Character (object):
    
    def __init__ (self, name, sprite_num):
        self.name = name
        self.sprite_num = sprite_num    
        
class CharacterRoster (object):
    def __init__ (self, file_name):
        
        self.character_list = []

        text_file = open(file_name,"r")
        
        for line in text_file:
            line = line.strip()
            my_fields = line.split(":",2)
            character = Character (my_fields[0], int(my_fields[1]))
            self.character_list.append(character)
        
    
    def get_number_of_characters (self):
        ''' Returns the number of Characters in the roster. '''
        return len(self.character_list)

