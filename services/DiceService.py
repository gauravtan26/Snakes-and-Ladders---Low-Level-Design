import random

class DiceService:
    def __init__(self,min=1,max=6):
        self.min=min
        self.max=max

    def roll(self):
        return random.randint(self.min,self.max)

