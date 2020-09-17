
from random import randint

class Die:
    def __init__(self,sides = 6):
        self.sides = sides


    def roll_die(self):
        print(randint(1,self.sides))

for i  in range(10):
    die_value = int(input())
    die = Die(die_value)
    die.roll_die()