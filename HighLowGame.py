from game_data import data
import random

def check_answer(answer, entity_a_followers, entity_b_followers):
    if entity_a_followers > entity_b_followers and answer.lower() == 'a':
        return True
    else:
        return False

def get_entities():
    get_index = random.randint(0, len(data)-1)
    get_another_index = random.randint(0, len(data)-1)
    while get_index == get_another_index:
        get_another_index = random.randint(0, len(data)-1)

    return get_index, get_another_index

while True:
    entity_a, entity_b = get_entities()

    print(f"Compare A: {data[entity_a]['name']}, a {data[entity_a]['description']}, from {data[entity_a]['country']}")
    print(f"Against B: {data[entity_b]['name']}, a {data[entity_b]['description']}, from {data[entity_b]['country']}")

    answer = input("Who has more followers? Type A or B")
    result = check_answer(answer, data[entity_a]['follower_count'], data[entity_b]['follower_count'])

    if result:
        print("Right answer")
    else:
        print("Wrong answer")
        break

