from ability_stone import Ability_Stone

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
