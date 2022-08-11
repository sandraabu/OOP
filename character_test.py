from character import Character
from character import Enemy
dave = Character("Dave", "A smelly zombie")




dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation('Hello there!')
dave.talk()
dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
