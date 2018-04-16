from classes.game import person, bcolors

magic = [{"name": "Fire", "cost":10, "dmg": 60},
         {"name": "Thinder", "cost":12, "dmg": 80},
         {"name": "Bizzard", "cost":10, "dmg": 60}]


player = person(460,65,60, 34,magic)
enemy = person(1200, 65,45, 25, magic)
running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("==========================")
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for",dmg, "Points of damage. Enemy HP:", enemy.get_hp())

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ",enemy_dmg, "Plaer HP", player.get_hp())


'''
print(player,generate_spell_damage(0))
print(player,generate_spell_damage(1))


print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
'''
