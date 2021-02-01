from character import Enemy
dave = Enemy("Dave", "He is a smelly zombie!")
dave.set_conversation("Braaaaains!")
dave.set_weakness("axe")

while True:
    dave.describe()
    command = input("> ")
    if command == "talk":
        while True:
            say = input("Talk to Dave > ")
            if say == "goodbye":
                break
            else:
                dave.talk()
    elif command == "fight":
        fight_with = input("What do you fight with? ")
        result = dave.fight(fight_with)
        if result == True:
            print("You have defeated Dave. There is nothing else to do.")
            break
        elif result == False:
            print("You are dead.")
            break
    else:
        print("You can't do that")