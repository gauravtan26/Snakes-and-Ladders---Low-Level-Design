from Board import Board
from Group import Group
from Player import Player
from DiceService import DiceService

class SnakeAndLadderService:
    def __init__(self,size=100):
        self.board=Board(size)
        self.group=None
        self.dice_service=DiceService()

    def set_group(self,group:Group):
        self.group=group
    
    def set_snakes(self,snake_list):
        self.board.set_snakes(snake_list=snake_list)
    
    def set_ladders(self,ladders_list):
        self.board.set_ladders(ladders_list)
    
    def decide_move(self,dice_value,position):
        if dice_value+position>self.board.get_size():
            return position
    
        if self.board.get_snakes().get(dice_value+position) is not None:
            return self.board.get_snakes().get(dice_value+position).get_end()

        if self.board.get_ladders().get(dice_value+position) is not None:
            return self.board.get_ladders().get(dice_value+position).get_end()
        return dice_value+position


    def play(self):
        return self.dice_service.roll()

    def has_won_game(self,position):
        if position==self.board.get_size():
            return True
        else:
            return False
        
    def start_game(self):
        game_run=True
        while game_run:
            for player in self.group.players:
                
                dice_value=self.play()
                position=self.decide_move(dice_value,player.get_position())
                print(player.get_name()+" rolled a "+str(dice_value)+ " and moved from " +str(player.get_position())+" to "+str(position))
                player.set_position(position)
                if position ==self.board.get_size():
                    print(player.get_name() + " wins the game")
                    game_run=False
                    break
                