
import requests, json, random

# Get the list of pokemon from the API
def fetch_all_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_names = []

    while url:
        response = requests.get(url)
        data = json.loads(response.text)

        for pokemon in data['results']:
            pokemon_names.append(pokemon['name'])

        url = data['next']

    return pokemon_names

print("\nWelcome to Pokemon Showdown! Please wait whilst the game loads...")
print("\nLoading...")
real_pokemon_list = fetch_all_pokemon()
print("\nLoading done! Game is ready to begin! Please pick your Pokemon!")
# Ask the user to choose a pokemon
# print('Enter your pokemon:')
# # for pokemon in pokemon_list:
#     # print(pokemon['name'])
#
# # Get the user's choice
# choice = input().lower()


while True:
        player_1 = input(f'\nFor player 1:\nEnter your pokemon:\n').lower()
        if player_1 not in real_pokemon_list:
            print("Not a valid pokemon, Try again.\n")
            continue
        else:
            print(f"Player 1 has picked pokemon {player_1.capitalize()}! Get ready for battle!\n")

        # Get the player_1 pokemon data
        url_1 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_1)
        response_1 = requests.get(url_1)
        pokemon_data = json.loads(response_1.text)

        # to get ability
        abilities_1 = pokemon_data['abilities'][0]
        ability_1 = abilities_1['ability']

        # to format height and weight properly
        height_1 = int(pokemon_data['height'])
        weight_1 = int(pokemon_data['weight'])

        height_formatted_1 = height_1 / 10
        weight_formatted_1 = weight_1 / 10

        move_list = []

        for move_data in pokemon_data['moves']:
            move_name = move_data['move']['name']
            move_list.append(move_name)

        # print(f"Moves List:{move_list}")
        available_moves = random.sample(move_list, 5)

        # Print the pokemon's data
        print('Name: {}'.format(pokemon_data['name'].capitalize()))
        print('Weight: {}'.format(weight_formatted_1) + "(kgs)")
        print('Height: {}'.format(height_formatted_1) + "(m)")
        print('Ability: {}'.format(ability_1['name']))
        break



while True:
        player_2 = input(f'\nFor player 2:\nEnter CPU if playing alone or enter your pokemon:\n ').lower()
        if player_2 == "cpu":
            player_2 = real_pokemon_list.pop()
            print(f"Player 2 has picked fighter {player_2.capitalize()}! Get ready to fight!\n")
        elif player_2 not in real_pokemon_list:
            print("Not a valid character, Try again.\n")
            continue
        else:
            print(f"Player 2 has picked pokemon {player_2.capitalize()}! Get ready for battle!\n")

    # Get the player_2 pokemon data
        url_2 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_2)
        response_2 = requests.get(url_2)
        pokemon_data_2 = json.loads(response_2.text)

        # to get ability
        abilities_2 = pokemon_data_2['abilities'][0]
        ability_2 = abilities_2['ability']

        # to format height and weight properly
        height_2 = int(pokemon_data_2['height'])
        weight_2 = int(pokemon_data_2['weight'])

        height_formatted_2 = height_2 / 10
        weight_formatted_2 = weight_2 / 10

        move_list_2 = []

        for move_data_2 in pokemon_data_2['moves']:
            move_name_2 = move_data_2['move']['name']
            move_list_2.append(move_name_2)

        # print(f"Moves List:{move_list}")
        available_moves_2 = random.sample(move_list, 5)

        # Print the pokemon's data
        print('Name: {}'.format(pokemon_data_2['name'].capitalize()))
        print('Weight: {}'.format(weight_formatted_2) + "(kgs)")
        print('Height: {}'.format(height_formatted_2) + "(m)")
        print('Ability: {}'.format(ability_2['name']))
        break

def attack(attacker,player_1,player_2, player_1_health=100, player_2_health=100):
    if attacker == player_1:
        attack_damage = random.randrange(1, 25)
        while True:
            attack_move = input(f"Player 1 pick an attack for {player_1.capitalize()} from the following moves:\n{available_moves}\n: ")
            if attack_move in available_moves:
                break
            else:
                print("Not a valid move, pick again")
                continue
        player_2_health -= attack_damage
        print(f"{player_1.capitalize()} has attacked {player_2.capitalize()} with {attack_move}! causing a damage of {attack_damage}")
        return player_2_health
    elif attacker == player_2:
        attack_damage = random.randrange(5, 30)
        while True:
            attack_move_2 = input(f"Player 2 pick an attack for {player_2.capitalize()} from the following moves:\n{available_moves_2}\n: ")
            if attack_move_2 in available_moves_2:
                break
            else:
                print("Not a valid move, pick again\n")
                continue
        player_1_health -= attack_damage
        print(f"{player_2.capitalize()} has attacked {player_1.capitalize()} with {attack_move_2}! causing a damage of {attack_damage}")
        return player_1_health

player_1_hp = 100
player_2_hp = 100
print("\nBattle has started!\n")
while True:
        player_2_hp_after_attack = attack(player_1, player_1, player_2, player_1_hp, player_2_hp)
        player_2_hp = player_2_hp_after_attack
        print(f"{player_2.capitalize()} hp is now {player_2_hp}\n")
        if player_2_hp <= 0:
            print(f"{player_2.capitalize()} has landed a fatal blow! {player_1.capitalize()} has been defeated.\n")
            winner = player_2
            break
        player_1_hp_after_attack = attack(player_2, player_1, player_2, player_1_hp, player_2_hp)
        player_1_hp = player_1_hp_after_attack
        print(f"{player_1.capitalize()} hp is now {player_1_hp}\n")
        if player_1_hp <= 0:
            print(f"{player_1.capitalize()} has landed a fatal blow! {player_2.capitalize()} has been defeated.\n")
            winner = player_1
            break
        else:
            continue

print(f"The winner is {winner.capitalize()}!\nGAME OVER!")





