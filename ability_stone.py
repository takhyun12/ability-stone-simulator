from typing import List, Union, Dict, Any
from random import *


class Ability_Stone:
    def __init__(self, **kwargs: dict) -> None:
        """ Make a Stone Object """
        self.MAX_PROB = kwargs['MAX_PROB']
        self.MIN_PROB = kwargs['MIN_PROB']
        self.current_prob: float = self.MAX_PROB
        self.increase_ability_1 = list([0] * kwargs['STONE_LEVEL'])
        self.increase_ability_2 = list([0] * kwargs['STONE_LEVEL'])
        self.decrease_ability_1 = list([0] * kwargs['STONE_LEVEL'])

    def crafting(self, selected_number: int) -> None:
        """
        Ability Point Crafting
        status code : (0:None, 1:Pass, 2:Fail)
        """
        # [1] Find Ability Table (O(1))
        if selected_number == 1:
            ability_table = self.increase_ability_1
        elif selected_number == 2:
            ability_table = self.increase_ability_2
        elif selected_number == 3:
            ability_table = self.decrease_ability_1
        else:
            raise Exception('Invalid number request')

        # [2] Crafting (O(10))
        for index in range(len(ability_table)):
            if ability_table[index] == 0:
                # Put Calc code here!
                self.current_prob = round(self.calc_prob(), 2)
                ability_table[index] = 1
                break

    def calc_prob(self) -> float:
        """ This function is under development."""
        return uniform(self.MIN_PROB, self.MAX_PROB)

    def show_status(self) -> None:
        """ Show Stone Status """
        print(f'current_prob : {self.current_prob}')
        print(f'Increase Ability 1 : {self.increase_ability_1}')
        print(f'Increase Ability 2 : {self.increase_ability_2}')
        print(f'Decrease Ability 1 : {self.decrease_ability_1}')


if __name__ == '__main__':
    ability_stone = Ability_Stone(MAX_PROB=0.75, MIN_PROB=0.25, STONE_LEVEL=10)
    ability_stone.show_status()

    # Test
    print('----')
    for i in range(0, 12):
        ability_stone.crafting(selected_number=1)

    for i in range(0, 2):
        ability_stone.crafting(selected_number=3)

    for i in range(0, 4):
        ability_stone.crafting(selected_number=2)

    ability_stone.show_status()

