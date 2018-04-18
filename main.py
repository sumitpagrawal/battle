from classes.game import person, bcolors
from classes.magic import Spell
from classes.inventory import Item


#Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")


#create While magic
cure = Spell("Cure", 25, 620, "White")
cura = Spell("Cura", 32, 1500, "White")


#Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack","Deals 500 damage", 500)

player_spells = [fire, thunder,blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity":5}, {"item": hipotion, "quantity":5},
                {"item": superpotion, "quantity":5},{"item": elixer, "quantity":5},
                {"item": hielixer, "quantity":5},{"item": grenade, "quantity":5}]

#Instantiate People
player1 = person("Valos", 3260,132, 300, 34, player_spells,player_items)
player2 = person("Nick ", 4160,188, 311, 34, player_spells,player_items)
player3 = person("Robot", 3089,174, 288, 34, player_spells,player_items)
enemy = person("Magus",11200, 701, 525, 25, [],[])

players = [player1, player2, player3]
running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("==========================")

    print("\n\n")
    print("NAME                      HP                                |MP")

    for player in players:
        player.get_stats()

    print("\n")

    for player in players:
        player.choose_action()
        choice = input("    Choose Action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for",dmg, "Points of damage.")

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic:")) -1

        if magic_choice == -1:
            continue


        spell = player.magic[magic_choice]
        magic_dmg =spell.generate_magic()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\n Not Enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "White":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "heals for" , str(magic_dmg), "MP", + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item:")) - 1

            if item_choice == -1:
                continue

        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            continue
        player.items[item_choice]["quantity"] -= 1


        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
        elif item.type == "elixr":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + "Fully Restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + "deals", str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ",enemy_dmg)

    print("----------------------------------------------")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win! " + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you! " + bcolors.ENDC)



















