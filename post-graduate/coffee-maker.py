'''
TITLE: Coffee Maker

AUTHOR: Azeem Mirza <https://azeemmirza.co>

LINK: https://classroom.google.com/u/1/c/NjcxOTU0MDE5MjI4/a/NjgyMjg2MzkxNDU1/details

DESCRIPTION: Create a Coffee class and a CoffeeMaker class. The Coffee class should have the following attributes:

DATE: 2024-06-02
'''

# Coffee class
class Coffee:
    def __init__(self, water: float = 0, coffee: float = 0):
        # Constants
        self._MUG_VOLUME = 200 # in milliliters
        self._COFFEE_DENSITY = 0.32 # in grams/ml

        # Variables
        self._water = 0
        self._coffee = 0

        if water > 0:
            self.add_water(water)
        
        if coffee > 0:
            self.add_coffee_beans(coffee)


    # to add water
    def add_water(self, amount):
        current_volume = self._MUG_VOLUME

        if self._water + amount > current_volume:
            print(f"Cannot add more than {current_volume}ml of water.")
            return
        
        self._water += amount
        self._MUG_VOLUME -= amount

        print(f"Added {amount}ml of water. Current water level: {self._water}ml")


    # to add beans
    def add_coffee_beans(self, amount):
        current_volume = self._MUG_VOLUME
        amount_in_ml = amount / self._COFFEE_DENSITY

        if self._coffee + amount_in_ml > current_volume:
            print(f"Cannot add more than {current_volume * self._COFFEE_DENSITY}g of coffee.")
            return
        
        self._coffee += amount
        self._MUG_VOLUME -= amount_in_ml

        print(f"Added {amount}g of coffee beans. Current coffee beans: {self._coffee}g")
    
    def get_water(self):
        return self._water
    
    def get_coffee(self):
        return self._coffee
        




# Coffee maker factory
class CoffeeMaker:
    def __init__(self):
        self._coffee = None

    def make_coffee(self, water: float = 0, coffee: float = 0):
        if water == 0 or coffee == 0:
            print("Please provide both water and coffee beans.")
            return
        
        self._coffee = Coffee(water, coffee)

        if self._coffee.get_water() == 0 or self._coffee.get_coffee() == 0:
            print("No coffee has been made yet. Only water or coffee is added.")
            return
        
        print("Coffee is ready!")

    def display_status(self):
        if self._coffee is None:
            print("\nNo coffee has been made yet.")
            return

        print("\nCoffee Maker Status:")
        print(f"Water level: {self._coffee.get_water()}ml")
        print(f"Coffee beans: {self._coffee.get_coffee()}g")


# Main function
def main():
    # USE CASE 01: Success
    print("\nUSE CASE 01: Success")
    coffee_maker = CoffeeMaker()
    coffee_maker.make_coffee(100, 30)
    coffee_maker.display_status()

    # USE CASE 02: Max Water no COFFEE
    print("\nUSE CASE 02: Max Water no COFFEE")
    coffee_maker.make_coffee(200, 30)
    coffee_maker.display_status()


if __name__ == "__main__":
    main()