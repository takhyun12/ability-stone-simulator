from ability_stone import Ability_Stone
from collections import Counter

if __name__ == '__main__':
    ability_stone = Ability_Stone(MAX_PROB=0.75, MIN_PROB=0.25, STONE_LEVEL=10)
    ability_stone.show_status()
    while True:
        try:
            ability_stone.simulation(selected_ability=int(input("돌을 선택하세요(1~3) : ")), crafting_result=ability_stone.crafting())
            ability_stone.show_status()
            if '◇' not in ability_stone.increase_ability_1 and '◇' not in ability_stone.increase_ability_2 and '◇' not in ability_stone.decrease_ability_1:
                break
        except Exception as ex:
            print(ex)
            print('')

    c1 = Counter(ability_stone.increase_ability_1)
    c2 = Counter(ability_stone.increase_ability_2)
    c3 = Counter(ability_stone.decrease_ability_1)

    print(sorted(c1.items(), key=lambda x: x[0]))
    print(sorted(c2.items(), key=lambda x: x[0]))
    print(sorted(c3.items(), key=lambda x: x[0]))
