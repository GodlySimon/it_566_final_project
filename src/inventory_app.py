"""Implements inventory application presentation layer (U/I) features."""

from business_logic import BusinessLogic
from prettytable import PrettyTable
import os
from datetime import datetime

class InventoryApp():
    """Implements household inventory control features."""

    def __init__(self):
        """Initialize object."""
        # Constants
        self.NEW_INVENTORY='1'
        self.LIST_INVENTORIES='2'
        self.SELECT_INVENTORY='3'
        self.LIST_INVENTORY_ITEMS='4'
        self.ADD_ITEMS='5'
        self.EXIT='6'
        # Fields
        self.menu_choice = 1
        self.keep_going = True
        self.business_logic = BusinessLogic()
        self.active_inventory_id = 0

    def clear_screen(self):
        """Clears the screen. It's either Unix-like or Windows."""
        try:
            os.system('clear')
        except Exception:
            os.system('cls')

    def display_menu(self):
        """Display menu."""
        print('\t\t\tHousehold Inventory Application')
        print()
        print('\t\t1. New Inventory')
        print('\t\t2. List Inventories')
        print('\t\t3. Select Inventory')
        print('\t\t4. List Inventory Items')
        print('\t\t5. Add Items')
        print('\t\t6. Exit')
        print()

    def process_menu_choice(self):
        """Process menu choice and execute corrensponding methods."""
        self.menu_choice = input('Please enter menu item number: ')
        if __debug__: 
            print(f'You entered: {self.menu_choice}')
        match self.menu_choice:
            case self.NEW_INVENTORY:
                self.new_inventory()
            case self.LIST_INVENTORIES:
                self.list_inventories()
            case self.SELECT_INVENTORY:
                self.select_inventory()
            case self.LIST_INVENTORY_ITEMS:
                self.list_inventory_items()
            case self.ADD_ITEMS:
                self.add_items()
            case self.EXIT:
                if __debug__:
                    print('Goodbye!')
                self.keep_going = False
                self.clear_screen
            case _:
                print('Invalid Menu Choice!')

    def new_inventory(self):
        """Create new inventory."""     
        self.clear_screen()
        if __debug__:
name = input("Enter a Product Name :  ")
        description = input("Enter the Product Description : ")
        today = datetime.now()
        self.business_logic.create_new_inventory(name,description,today)
        input(f'One row inserted successfully')
 Old one was  
input('\n\nThis method is not yet implemented. Press any key to continue: ')   Also added at line 131 #input('\n\vThis method is not yet implemented. Press any key to continue: ')
        name = input("Enter Item Name :  ")
        count = input("Enter the Count of Item : ")
        inventory_id = input("Please to insert the Product Id:")
        self.business_logic.create_new_item(inventory_id,name,count)
        input(f'One row inserted successfully')

        input(f'One row inserted successfully')
        input('\n\nPress any key to continue...')


    def list_inventories(self):
        """List inventories."""
        self.clear_screen()
        if __debug__:
            print('list_inventories() method called...')
        self.print_inventory_list(self._get_inventories())
        input('\n\nPress any key to continue...')
            

    def _get_inventories(self):
        """Utility method that calls business logic layer to get all inventory records."""
        return self.business_logic.get_all_inventories()


        
    def select_inventory(self):
        """Selects an existing inventory"""
        self.clear_screen()
        if __debug__:
            print('select_inventory() method called.')

        inventory_list = None
        try:
            inventory_list = self._get_inventories()
            keep_going = True
            while keep_going:
                self.print_inventory_list(inv_list=inventory_list)
                self.active_inventory_id = int(input('\n\nSelect inventory id from list: '))
                response = input(f'You entered {str(self.active_inventory_id)}. Is this correct? (y/n) ')
                if response.capitalize() == 'Y':
                    keep_going = False
        except Exception as e:
            print(f'Exception in select_inventory() method: {e}')
            
    def list_inventory_items(self):
        """List inventory items for inventory id contained in self.active_inventory_id field."""
        self.clear_screen()
        if __debug__:
            print('list_inventory_items() method called...')
        items_list = self.business_logic.get_items_for_inventory_id(self.active_inventory_id)
        self.print_items_list(items_list)
        input('\n\nPress any key to continue...')
        

    def add_items(self):
        """Add items to inventory."""
        if __debug__:
            print('add_items() method called...')
        #input('\n\vThis method is not yet implemented. Press any key to continue: ')
        name = input("Enter Item Name :  ")
        count = input("Enter the Count of Item : ")
        inventory_id = input("Please to insert the Product Id:")
        self.business_logic.create_new_item(inventory_id,name,count)
        input(f'One row inserted successfully')

    def start_application(self):
        """Start the applications."""
        while self.keep_going:
            self.clear_screen()
            self.display_menu()
            self.process_menu_choice()
            
                    
    def print_inventory_list(self, inv_list):
        t = PrettyTable(['ID', 'Name', 'Description'])
        for row in inv_list:
            t.add_row([row[0], row[1], row[2]])
        print(t)

    def print_items_list(self, items_list):
        t = PrettyTable(['ID', 'Inventory ID', 'Item', 'Count'])
        for row in items_list:
            t.add_row([row[0], row[1], row[2], row[3]])
        print(t)
