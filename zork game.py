import random
import time
from PIL import Image
partyHP = 0
goblinHP = 35
hunterHP = 100
bossHP = 200
enemyAttack = 0
chance = 0
win = 0

def attackroll():
    attack = random.randrange(5, 31)
    crit_chance = random.random()

    if crit_chance < 0.2:
        crit_multiplier = 2
        print("Critical hit!")
    else:
        crit_multiplier = 1

    damage = attack * crit_multiplier
    return damage

def heal():
    heal_bonus = random.randint(5, 15)
    print("Defensive stance activated, healing.")
    return heal_bonus

def enemyAttackRoll(player_num):
    attack = random.randrange(1, 16)
    crit_multiplier = 1 
    if player_num > 2:
        crit_multiplier = 1.5 
    damage = attack * crit_multiplier
    return damage

numPlayers = int(input('Welcome to the game, please select the number of players (1-4): '))
players = range(1, numPlayers + 1)

for player_num in players:
    partyHP += 100

while partyHP > 0 and win == 0:
    print("Your party walks into a dark and dingy cavern, a lowly goblin stumbles from the darkness brandishing a rusted dagger, what do you do?")
    im = Image.open("C:\\Users\\toddp\\OneDrive\\Documents\\Work\\Year 2\\zork\\goblin.png")
    im.show()
    while goblinHP > 0 and partyHP > 0:
        for player_num in players:
            choice1 = input(f'Player {player_num}, do you want to Attack, Heal, or Run? ')

            if choice1.lower() == "attack":
                damage = attackroll()
                goblinHP -= damage
                print(f'Player {player_num} did {damage} damage. The enemy has {goblinHP} HP left.')
                time.sleep(1)  
                if goblinHP <= 0:
                    break

                if goblinHP > 0:
                    enemyAttack = enemyAttackRoll(player_num)
                    print(f'The goblin fights back and deals {enemyAttack} damage.')
                    time.sleep(1)
                    partyHP -= enemyAttack
                    print(f'Your party has {partyHP} HP left.')
                    time.sleep(1)
            elif choice1.lower() == "heal":
                heal_bonus = heal()
                partyHP += heal_bonus
                print(f'Player {player_num} healed and replenished {heal_bonus} hp. Your party has {partyHP} HP left.')
                time.sleep(1)
                
                if goblinHP > 0:
                    enemyAttack = enemyAttackRoll(player_num)
                    print(f'The goblin fights back and deals {enemyAttack} damage.')
                    time.sleep(1)
                    partyHP -= enemyAttack
                    print(f'Your party has {partyHP} HP left.')
                    time.sleep(1)
            elif choice1.lower() == "run":
                print("You only just arrived! Where are you going?")
                partyHP = 0
            else:
                print("Invalid choice. Please enter 'attack', 'defend', or 'run'.")

    if partyHP > 0:
        print("Your party successfully deals with the goblin and can move forward.")
        time.sleep(1)
        choice2 = input("There is a hidden passage to the left and a dimly lit hallway in front of you, which do you choose, Left or Forward? ")
        time.sleep(1)
        if choice2.lower() == 'left':
            print('Your party starts creeping down the hidden passage as you hear something snap under your feet. Your party is endlessly falling down a bottomless pit.')
            partyHP = 0
        elif choice2.lower() == 'forward':
            print("There is a loud thud and the ground shakes, rocks hit the floor, and emerging from the shadows is an elite hunter searching for their next trophy.")
            im = Image.open("C:\\Users\\toddp\\OneDrive\\Documents\\Work\\Year 2\\zork\\hunter.png")
            im.show()
            time.sleep(1)

            choice3 = input("What do you do, sneak past or aim for the eyes? Type sneak or attack ")
            time.sleep(1)
            if choice3.lower() == 'sneak':
                print('Your party takes their chances at sneaking past.')
                time.sleep(1)
                if player_num == 1:
                    print("You sneak through successfully.")
                elif player_num == 2:
                    chance = random.randrange(1, 5)
                    if chance > 3:
                        print("You sneak through successfully.")
                    else:
                        print("Your party is noticed and is dealt a heavy blow but you manage to get away.")
                        time.sleep(1)
                        partyHP -= 100
                        print(f'Your party loses 100 hp. You are now at {partyHP} hp')
                        hunterHP = 0
                elif player_num >= 3:
                    print("Your party is too large to sneak past. You all die.") 
                    time.sleep(1)
                    partyHP = 0
            elif choice3.lower() == 'attack':
                print("Your party decides to attack the hunter. He is roughly human-sized but has a big hammer.")
                time.sleep(1)
                while hunterHP > 0 and partyHP > 0:
                    for player_num in players:
                        choice1 = input(f'Player {player_num}, do you want to Attack, Heal, or Run? ')

                        if choice1.lower() == "attack":
                            damage = attackroll()
                            hunterHP -= damage
                            print(f'Player {player_num} did {damage} damage. The enemy has {hunterHP} HP left.')
                            time.sleep(1)
                            if hunterHP <= 0:
                                break

                            if hunterHP > 0:
                                enemyAttack = enemyAttackRoll(player_num)
                                print(f'The hunter swings his hammer and deals {enemyAttack + 10} damage.')
                                time.sleep(1)
                                partyHP -= enemyAttack
                                print(f'Your party has {partyHP} HP left.')
                                time.sleep(1)
                        elif choice1.lower() == "heal":
                            heal_bonus = heal()
                            partyHP += heal_bonus
                            print(f'Player {player_num} healed and replenished {heal_bonus} hp. Your party has {partyHP} HP left.')
                            time.sleep(1)
                            if hunterHP > 0:
                                enemyAttack = enemyAttackRoll(player_num)
                                print(f'The hunter swings his hammer and deals {enemyAttack + 10} damage.')
                                time.sleep(1)
                                partyHP -= enemyAttack
                                print(f'Your party has {partyHP} HP left.')
                                time.sleep(1)
                        elif choice1.lower() == "run":
                            print("You can't escape from the hunter!")
                            time.sleep(1)
                            enemyAttack = enemyAttackRoll(player_num)
                            print(f'The hunter swings his hammer and deals {enemyAttack + 10} damage.')
                            time.sleep(1)
                            partyHP -= enemyAttack
                            print(f'Your party has {partyHP} HP left.')
                            time.sleep(1)
                        else:
                            print("Invalid choice. Please enter 'attack', 'heal', or 'run'.")
                
                if partyHP > 0:
                    choice4 = input("The cave opens up to a giant throne room with the skeleton queen sitting on a pile of skulls of previous travelers. She notices you immediately and is charging, give up or fight? ")
                    im = Image.open("C:\\Users\\toddp\\OneDrive\\Documents\\Work\\Year 2\\zork\\boss.png")
                    im.show()
                    time.sleep(1)
                    if choice4.lower() == 'give up':
                        print("You run like cowards out of the cave never to return after what you have seen.")
                        time.sleep(1)
                        partyHP = 0
                    elif choice4.lower() == 'fight':
                        time.sleep(1)
                        while bossHP > 0 and partyHP > 0:
                            for player_num in players:
                                choice5 = input(f'Player {player_num}, do you want to Attack, Heal, or Run? ')

                                if choice5.lower() == "attack":
                                    damage = attackroll()
                                    bossHP -= damage
                                    print(f'Player {player_num} did {damage} damage. The boss has {bossHP} HP left.')
                                    time.sleep(1)
                                    if bossHP <= 0:
                                        break

                                    if bossHP > 0:
                                        enemyAttack = enemyAttackRoll(player_num)
                                        print(f'The boss throws her bone spear towards your party and deals {enemyAttack + 15} damage.')
                                        time.sleep(1)
                                        partyHP -= enemyAttack
                                        print(f'Your party has {partyHP} HP left.')
                                        time.sleep(1)
                                elif choice5.lower() == "heal":
                                    heal_bonus = heal()
                                    partyHP += heal_bonus
                                    print(f'Player {player_num} healed and replenished {heal_bonus} hp. Your party has {partyHP} HP left.')
                                    time.sleep(1)
                                    if bossHP > 0:
                                        enemyAttack = enemyAttackRoll(player_num)
                                        print(f'The boss throws her bone spear towards your party and deals {enemyAttack + 15} damage.')
                                        time.sleep(1)
                                        partyHP -= enemyAttack
                                        print(f'Your party has {partyHP} HP left.')
                                        time.sleep(1)
                                elif choice5.lower() == "run":
                                    print("You can't escape from the queen.")
                                    time.sleep(1)
                                    enemyAttack = enemyAttackRoll(player_num)
                                    print(f'The boss throws her bone spear towards your party and deals {enemyAttack + 15} damage.')
                                    time.sleep(1)
                                    partyHP -= enemyAttack
                                    print(f'Your party has {partyHP} HP left.')
                                    time.sleep(1)
                                else:
                                    print("Invalid choice. Please enter 'attack', 'heal', or 'run'")
                        if bossHP <= 0:
                            win = 1

if win == 1:
    print('Congratulations, you have won the game!')
else:
    print("Your party failed. Shame.")
