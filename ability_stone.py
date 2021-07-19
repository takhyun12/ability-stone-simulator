import random
from typing import List, Union, Dict, Any
from collections import Counter


class Ability_Stone:
    def __init__(self, **kwargs: dict) -> None:
        """ Make a Stone Object """
        self.MAX_PROB = kwargs['MAX_PROB']
        self.MIN_PROB = kwargs['MIN_PROB']
        self.current_prob: float = kwargs['MAX_PROB']
        self.increase_ability_1 = list(['◇'] * kwargs['STONE_LEVEL'])
        self.increase_ability_2 = list(['◇'] * kwargs['STONE_LEVEL'])
        self.decrease_ability_1 = list(['◇'] * kwargs['STONE_LEVEL'])

    def crafting(self, selected_ability: int, crafting_result: bool) -> None:
        """
        Ability Point Crafting
        Status Code : (0: None, 1: Pass, 2: Fail)
        """
        # [1] Exception handle
        if selected_ability < 0 or selected_ability > 3:
            raise Exception('Invalid number request')

        # [2] Find Ability Table (O(1))
        ability_table: list = self.get_target_table(selected_ability=selected_ability)

        # [3] Crafting (O(10))
        for index in range(len(ability_table)):
            if ability_table[index] == '◇':
                ability_table[index] = '◆' if crafting_result else '✖'
                self.calc_prob(crafting_result)
                self.get_recommendation()

                break
        else:
            pass

    def get_target_table(self, selected_ability: int) -> list:
        """ Get target ability object """
        return self.increase_ability_1 if selected_ability == 1 else self.increase_ability_2 if selected_ability == 2 else self.decrease_ability_1

    def calc_prob(self, crafting_result: bool) -> None:
        """ Calc Probabilities based on user request """
        if crafting_result:
            if self.current_prob < self.MAX_PROB:  # Pass
                self.current_prob += 0.15
                self.current_prob = round(self.current_prob, 2)
        else:
            if self.current_prob > self.MIN_PROB:  # Fail
                self.current_prob -= 0.15
                self.current_prob = round(self.current_prob, 2)

    def get_recommendation(self) -> dict:
        """ This function is under development """
        return {'1': self.MAX_PROB, '2': 0.15, '3': 0.17}

    def show_status(self) -> None:
        """ Show Stone Status """
        print(f'Current_prob : {self.current_prob}')
        print(f'Increase Ability 1 : {self.increase_ability_1}')
        print(f'Increase Ability 2 : {self.increase_ability_2}')
        print(f'Decrease Ability 1 : {self.decrease_ability_1}')


if __name__ == '__main__':
    ability_stone = Ability_Stone(MAX_PROB=0.75, MIN_PROB=0.25, STONE_LEVEL=10)

    # Test
    for i in range(1, 4):
        for j in range(0, 10):
            r = bool(random.getrandbits(1))
            ability_stone.crafting(selected_ability=i, crafting_result=r)
            ability_stone.show_status()

    c1 = Counter(ability_stone.increase_ability_1)
    c2 = Counter(ability_stone.increase_ability_2)
    c3 = Counter(ability_stone.decrease_ability_1)

    print(c1)
    print(c2)
    print(c3)
