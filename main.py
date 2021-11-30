import art
import random
import game_data
print(art.logo)

random.shuffle(game_data.dataz)
name = game_data.dataz[0]
print(name)


random.shuffle(game_data.dataz)
print(game_data.dataz)
