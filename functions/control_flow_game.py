# Make a 2 player Battle game, using Python!
#
# Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.
#
# If Player 2, let them pick the character/fighter they want. If CPU assign a character/fighter randomly.
#
# The two Pokemon need to fight.
#
# A winner must be declared via some sort of calculation.
#
# Bonus: Want to play again?
import random

list_of_fighters = {"Luke", "Ramon", "Shahrukh", "Mitchell"}
def player_character_1():
    while True:
        player_1 = input(f"Pick a character from {list_of_fighters}: ")
        if player_1 not in list_of_fighters:
            print("Not a valid character, Try again.\n")
            continue
        else:
            print(f"Player 1 has picked fighter {player_1}! Get ready to fight!\n")
        return player_1

def player_character_2():
    while True:
        player_2 = input(f"Pick a character from {list_of_fighters} or 'CPU' if you'd like to play alone: ")
        if player_2 == "CPU":
            player_2 = list_of_fighters.pop()
            print(f"Player 2 has picked fighter {player_2}! Get ready to fight!\n")
        elif player_2 not in list_of_fighters:
            print("Not a valid character, Try again.\n")
            continue
        else:
            print(f"Player 2 has picked fighter {player_2}! Get ready to fight!\n")
        return player_2

def attack(attacker,player_1,player_2, player_1_health=100, player_2_health=100):
    attack_damage = random.randrange(1, 25)
    if attacker == player_1:
        player_2_health -= attack_damage
        print(f"{player_1} has attacked {player_2} with a damage of {attack_damage}\n")
        return player_2_health
    elif attacker == player_2:
        player_1_health -= attack_damage
        print(f"{player_2} has attacked {player_1} with a damage of {attack_damage}\n")
        return player_1_health


def fight(player_1, player_2):
    player_1_hp = 100
    player_2_hp = 100
    while True:
        player_1_hp_after_attack = attack(player_2,player_1,player_2, player_1_hp, player_2_hp)
        player_2_hp_after_attack = attack(player_1,player_1,player_2, player_1_hp, player_2_hp)
        player_1_hp = player_1_hp_after_attack
        print(f"{player_1} hp is now {player_1_hp}")
        player_2_hp = player_2_hp_after_attack
        print(f"{player_2} hp is now {player_2_hp}")
        if player_1_hp <= 0 :
            print(f"{player_2} has landed a fatal blow! {player_1} has been killed.\n")
            winner = player_2
            return winner
        elif player_2_hp <= 0:
            print(f"{player_1} has landed a fatal blow! {player_2} has been killed.\n")
            winner = player_1
            return winner
        else:
            continue



def sparta_royale():
    print("Welcome to Sparta Royale, pick your character and get ready to fight!")
    player_1 = player_character_1()
    player_2 = player_character_2()
    winner = fight(player_1, player_2)
    print(f"The winner is {winner}! they're the true spartan!\nGAME OVER!")

sparta_royale()
