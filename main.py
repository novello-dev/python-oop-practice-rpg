# ------------ imports ------------
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword

# ------------ setup ------------
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)

enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

input("Pressione Enter para começar...")

# ------------ game loop ------------
while hero.health > 0 and enemy.health > 0:
    os.system("cls" if os.name == "nt" else "clear")

    hero.attack(enemy)

    if enemy.health > 0:
        enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()

os.system("cls" if os.name == "nt" else "clear")

hero.health_bar.draw()
enemy.health_bar.draw()

if hero.health <= 0:
    print("Enemy venceu!")
else:
    print("Hero venceu!")
