from Snake import Snake
from Ladder import Ladder

class Board:
    __size=0
    def __init__(self,size=100):
        self.__snakes={}
        self.__ladders={}
        self.__size=size
    def get_size(self):
        return self.__size

    def get_snakes(self):
        return self.__snakes
    
    def get_ladders(self):
        return self.__ladders

    def set_snakes(self,snake_list):
        for snake_corrdinates in snake_list:
            self.__snakes[snake_corrdinates[0]]=Snake(snake_corrdinates[0],snake_corrdinates[1])

    def set_ladders(self,ladder_list):
        for ladder in ladder_list:
            self.__ladders[ladder[0]]=Ladder(ladder[0],ladder[1])


