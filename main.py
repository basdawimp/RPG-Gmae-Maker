from room import Room
from item import Item
from character import Enemy
from rpginfo import RPGInfo

#Create Game
spooky_castle = RPGInfo("The Spooky Castle")
RPGInfo.author = "Me"

#Creat the rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

#Create items
ball = Item("ball")
candle = Item("candle")
knife = Item("knife")

#Create character
dave = Enemy("Dave", "He is a smelly zombie!")
dave.set_conversation("Braaaaains!")
dave.set_weakness("candle")

#Set room descriptions
kitchen.set_description("A dank and dirty place, buzzing with flies")
ballroom.set_description("An oppulant ballroom with a cristal chandolure")
dining_hall.set_description("There is a table laid for 6, but the food is rotten")

#Set item description
ball.set_description("A football")
candle.set_description("This candle is melted almost to a stump")
knife.set_description("A sharp knife. Carefull, you could do some damage with this")

#Set room links
kitchen.link_rooms(dining_hall,"south")
ballroom.link_rooms(dining_hall, "east")

#Put items in rooms
ball.set_location(ballroom)
kitchen.place_item([knife, candle])

#put characters in rooms
dave.set_location(ballroom)

#Set current 
alive = True
current_room = kitchen

#Play
spooky_castle.welcome()
RPGInfo.info()
while alive == True:
    print()
    current_room.get_details()
    items = current_room.get_items()
    inhabitants = current_room.get_characters()
    command = input("> ")
    if command == "end":
        break
    elif command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitants == []:
            print("There is no one to talk to here.")
        else:
            talk_to = input("Who do you talk to? ")
            if talk_to not in current_room.present_character_names:
                print("They are not here.")
            else:
                while True:
                    say = input("Talk to " + talk_to + "> ")
                    if say == "goodbye":
                        break
                    else:
                        inhabitants[talk_to].talk()
    elif command == "fight":
        if inhabitants == {}:
            print("There is no one to fight here.")
        else:
            fighting = input("Who do you pick a fight with? ")
            if fighting not in current_room.present_character_names:
                print("They are not here.")
            else:
                fight_with = input("What do you fight with? ")
                alive = inhabitants[fighting].fight(fight_with)
                if alive == True:
                    print("You have defeated " + fighting + ".")
                    del inhabitants[fighting]
                    current_room.present_character_names.remove(fighting)
                elif alive == False:
                    print("You are dead.")
    else:
        print("You can't do that.")
RPGInfo.credits()