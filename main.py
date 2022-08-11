from room import Room
from character import Enemy, Friend


kitchen = Room('kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")

dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")

# kitchen.describe()
# ballroom.describe()
# dining_hall.describe()

kitchen.link_room(dining_hall, "south")   
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

#dining_hall.get_details()

current_room = kitchen

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

caroline = Enemy('Caroline', 'A supervillan')
caroline.set_conversation('Arrrrrr .....')
caroline.set_weakness('chocolate cake')
kitchen.set_character(caroline)

# charlie = Enemy('Charlie', 'Ugly monster')
# charlie.set_conversation('Mirror, mirror...who is the prettiest in the world?')
# charlie.set_weakness('hats')
# ballroom.set_character(charlie)

joe = Friend('Joe', 'Friendly chap')
joe.set_conversation('How are you doing?')
ballroom.set_character(joe)

dead = False
while dead ==False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:                    
        inhabitant.describe()

    command = input(">")
    directions = ['north', 'south', 'east', 'west']
    if command in directions:
        current_room = current_room.move(command)
    elif command == 'talk':
        if inhabitant != None:
            inhabitant.talk()

    elif command == 'fight':
        if inhabitant != None and isinstance(inhabitant, Enemy):
            print('How you are going to fight?')
            weapon = input()
            if inhabitant.fight(weapon) == True:
                print('You won!')
                current_room.set_character(None)
            else:
                print('Battle lost!')
                print('The end')
                dead = True
        else:
            print(' No one to fight with')

    elif command == 'steal':
        if inhabitant != None:
            if isinstance(inhabitant, Enemy):
                inhabitant.steal()
                print('What did you steal now?')
                print('Naughty, give it back!')
                
            else:
                print("We're good!")

        else:
            print('No burglary today')

    elif command == 'hug':
        if inhabitant !=None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you ...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")

    elif command == 'dance':
        if inhabitant !=None:
            if isinstance(inhabitant, Enemy):
                print("i won't dance with someone like you!")
            else:
                inhabitant.dance()
        else:
            print("No dance today then :/")

    elif command == "sing":
        if inhabitant !=None:
            if isinstance(inhabitant, Enemy):
                print("Stay quite!")
            else:
                inhabitant.sing()
        else:
            print("ok, let's sing another day")

    

    
               


