import os
import json
from collections import Counter
from datetime import datetime
from google.cloud import pubsub_v1
from ability_stone import Ability_Stone

TOPIC_PATH = 'projects/ability-stone-simulator/topics/logging-topic'
CREDENTIALS_PATH = 'Resource/pubsub_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_PATH


class PubFunction:
    def send_craft_log(**self: dict) -> None:
        json_data = json.dumps(self, indent=4, ensure_ascii=False)
        data = json_data.encode('utf-8')
        publisher.publish(TOPIC_PATH, data)


if __name__ == '__main__':
    publisher = pubsub_v1.PublisherClient()

    ability_stone = Ability_Stone(MAX_PROB=0.75, MIN_PROB=0.25, STONE_LEVEL=10)
    ability_stone.show_status()
    while True:
        try:
            selected_ability = int(input("세공하고자 하는 능력을 선택하세요(1~3) : "))
            crafting_result = ability_stone.crafting()

            ability_stone.simulation(selected_ability=selected_ability, crafting_result=crafting_result)
            ability_stone.show_status()

            c1 = Counter(ability_stone.increase_ability_1)
            c2 = Counter(ability_stone.increase_ability_2)
            c3 = Counter(ability_stone.decrease_ability_1)

            PubFunction.send_craft_log(time_stamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                       selected_ability=str(selected_ability),
                                       crafting_result=str(crafting_result),
                                       current_prob=str(ability_stone.current_prob),
                                       increase_ability_1=str(sorted(c1.items())),
                                       increase_ability_2=str(sorted(c2.items())),
                                       decrease_ability_1=str(sorted(c3.items())))

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
