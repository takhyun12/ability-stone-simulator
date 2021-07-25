from ability_stone import Ability_Stone
import os
from google.cloud import pubsub_v1
from collections import Counter
from datetime import datetime

TOPIC_PATH = 'projects/ability-stone-simulator/topics/logging-topic'
CREDENTIALS_PATH = 'Resource/private-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_PATH


class PubFunction:
    def logging(**self: dict) -> None:
        data = '{"name": "kkk", "age": "4444"}'
        data = data.encode('utf-8')
        logging_publisher.publish(TOPIC_PATH, data)
        attributes = {str(key): str(value) for key, value in self.items()}
        print(attributes)
        #logging_publisher.publish(TOPIC_PATH, data, **attributes)


if __name__ == '__main__':
    logging_publisher = pubsub_v1.PublisherClient()

    ability_stone = Ability_Stone(MAX_PROB=0.75, MIN_PROB=0.25, STONE_LEVEL=10)
    ability_stone.show_status()
    while True:
        try:
            selected_ability = int(input("돌을 선택하세요(1~3) : "))
            crafting_result = ability_stone.crafting()

            ability_stone.simulation(selected_ability=selected_ability, crafting_result=crafting_result)
            ability_stone.show_status()

            PubFunction.logging(time_stamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                selected_ability=selected_ability,
                                crafting_result=crafting_result,
                                current_prob=ability_stone.current_prob,
                                increase_ability_1=Counter(ability_stone.increase_ability_1),
                                increase_ability_2=Counter(ability_stone.increase_ability_2),
                                decrease_ability_1=Counter(ability_stone.decrease_ability_1))

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
