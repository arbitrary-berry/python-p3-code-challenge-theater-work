from lib.audition import Audition


class Role:

    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append(self)

    def get_character_name(self):
        return self.character_name
    
    def set_character_name(self, character_name):
        self.character_name = character_name
        
    def character_name(self):
        if type(character_name) == str:
            return character_name
        else:
            raise Exception


Role("Hamlet")