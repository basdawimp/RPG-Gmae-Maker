class Item():
    #define attributes
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.location = None
    
    #define methods for item name manipulaiton
    def set_name(self, item_name):
        self.name = item_name
        pass
    def get_name(self):
        return self.name

    #define methods for item description manipulaiton
    def set_description(self, item_description):
        self.description = item_description
        pass
    def get_description(self):
        return self.description

    #define methods for item location manipulation
    def set_location(self, location):
        self.location = location.name
        location.items_present[self.name] = self
        location.present_item_names.append(self.name)
        pass
    def get_location(self):
        return self.location

    #define method that prints item description, without further details
    def describe(self):
        print(self.get_description())

    #define method that prints item details
    def get_details(self):
        print(self.get_name())
        print("-------------------------")
        print(self.get_description())

    pass