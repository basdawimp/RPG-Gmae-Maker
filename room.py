class Room():
    #Set class variables
    number_of_room = 0

    #define instant attributes
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.linked_room_names = {}
        self.items_present = {}
        self.present_item_names = []
        self.characters_present = {}
        self.present_character_names = []
        Room.number_of_room = Room.number_of_room + 1
        pass

    #define methods for room name manipulaiton
    def set_name(self, room_name):
        self.name = room_name
        pass
    def get_name(self):
        return self.name
    def room(self):
        print(self.name)
        pass

    #define methods for room description manipulaiton
    def set_description(self, room_description):
        self.description = room_description
        pass
    def get_description(self):
        return self.description

    #define a funciton that reversed the direction. i.e. north becomes south, etc.
    def reverse_direction(self, direction):
        if direction == "north":
            return "south"
        elif direction == "east":
            return "west"
        elif direction == "south":
            return "north"
        else:
            return "east"

    #define a method to link rooms together
    def link_rooms(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        room_to_link.linked_rooms[self.reverse_direction(direction)] = self
        self.linked_room_names[direction] = room_to_link.name
        room_to_link.linked_room_names[self.reverse_direction(direction)] = self.name
    def get_linked_rooms(self):
        return self.linked_rooms
    def get_linked_room_names(self):
        return self.linked_room_names


    #define method for putting an item into a room
    def place_item(self, items):
        for item in items:
            item.set_location(self)
    def get_items(self):
        return self.items_present
    def get_item_names(self):
        return self.present_item_names

    #define method for putting characters in a room
    def set_characters(self, characters):
        for character in characters:
            character.set_location(self)
    def get_characters(self):
        return self.characters_present
    def get_character_names(self):
        return self.present_character_names

    #Print the full room details
    def get_details(self):
        items = self.present_item_names
        inhabitant = self.present_character_names
        print(self.name)
        print("-------------------------")
        print(self.description)
        if items == []:
            print("You seen no items in this room")
        else:
            for item in items:
                print("You see a " + item)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        print()
        if inhabitant == []:
            print("There is no one here")
        else:
            for entity in inhabitant:
                self.characters_present[entity].describe()
        pass

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("you can't do that way")
            return self
    pass

