from Player import Player

class Group:
    def __init__(self):
        self.players=[]
    

    def add_player(self,name) -> Player:
        player=Player(name)
        self.players.append(player)
        return player
    

    