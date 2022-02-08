from tokenize import group

from sklearn.manifold import trustworthiness
from Player import Player
from Snake import Snake
from Board import Board
from Group import Group
from SnakenLaddersService import SnakeAndLadderService

if __name__=='__main__':
    snakes=[]
    n_snakes=int(input())
    for i in range(n_snakes):
        coord=input().split(" ")
        snakes.append((int(coord[0]),int(coord[1])))
    ladders=[]
    n_ladder=int(input())
    for i in range(n_ladder):
        coord=input().split(" ")
        ladders.append((int(coord[0]),int(coord[1])))
    n_players=int(input())
    group=Group() 
    for i in range(n_players):
        group.add_player(input())

    snake_and_ladder_service=SnakeAndLadderService()
    snake_and_ladder_service.set_group(group)
    snake_and_ladder_service.set_ladders(ladders_list=ladders)
    snake_and_ladder_service.set_snakes(snake_list=snakes)

    print("Start")
    snake_and_ladder_service.start_game()

     
        

