from DiceService import DiceService

class Player:
    def __init__(self,name,position=0):
        self.__name=name
        self.__position=position
    
    def get_position(self):
        return self.__position

    def set_position(self,position):
        self.__position=position
    def get_name(self):
        return self.__name




    