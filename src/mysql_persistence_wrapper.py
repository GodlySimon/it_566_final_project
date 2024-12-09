"""Implements a MySQL Persistence Wrapper"""

from persistence_wrapper_interface import PersistenceWrapperInterface
from mysql import connector

class MySQLPersistenceWrapper(PersistenceWrapperInterface):
    """Implements MySQL Persistance Wrapper"""

    def __init__(self):
        """Initializes """
        # Constants
        self.SELECT_ALL_INVENTORIES = 'SELECT id, name, description FROM inventories'
        self.INSERT_INVENTORY =  'INSERT INTO inventories (id, name, description, date) VALUES(%s,%s, %s, %s)'
        self.INSERT_ITEM =  'INSERT INTO items (id,inventory_id, item, count) VALUES(%s,%s, %s, %s)'
        #self.STATIC_INSERT= """INSERT INTO inventories(id, name, description, date)"""
        self.INSERT = 'INSERT INTO items (inventory_id, item, count) VALUES(%s, %s, %s)'
        self.SELECT_ALL_ITEMS_FOR_INVENTORY_ID = 'SELECT id, inventory_id, item, count FROM items WHERE inventory_id = %s'

        # Database Configuration Constants
        self.DB_CONFIG = {}
        self.DB_CONFIG['database'] = 'home_inventory'
        self.DB_CONFIG['user'] = 'home_inventory_user'
        self.DB_CONFIG['host'] = '127.0.0.1'
        self.DB_CONFIG['port'] = 8889 

        # Database Connection
        self._db_connection = self._initialize_database_connection(self.DB_CONFIG)


    def get_all_inventories(self):
        """Returns a list of all rows in the inventories table"""
        cursor = None
        try:
            cursor = self._db_connection.cursor()
            cursor.execute(self.SELECT_ALL_INVENTORIES)
            results = cursor.fetchall()
        except Exception as e:
            print(f'Exception in persistance wrapper: {e}')
        return results


    def get_items_for_inventory(self, inventory_id):
        """Returns a list of all items for given inventory id"""
        cursor = None
        try:
            cursor = self._db_connection.cursor()
            cursor.execute(self.SELECT_ALL_ITEMS_FOR_INVENTORY_ID, ([inventory_id]))
            results = cursor.fetchall()
        except Exception as e:
            print(f'Exception in persistance wrapper: {e}')
        return results


    def create_inventory(self, name: str, description: str, date: str):
        """Insert new row into inventories table."""
        cursor = None
        
        try :
            cursor = self._db_connection.cursor()
            cursor.execute('select MAX(id)+1 from inventories')
            result = cursor.fetchone()
            values = (result[0] + 1 ,name,description,date)
            cursor.execute(self.INSERT_INVENTORY, values)
            self._db_connection.commit()
        except Exception as e:
            print(f'Exception in Persistance wrapper: {e}')
        

    def create_item(self,item_id: int, inventory_id: int, item: str, count: int):
        """Insert new row into items table for given inventory id"""
        cursor = None
        
        try:
            cursor = self._db_connection.cursor()
            cursor.execute('select MAX(id)+1 from items')
            result = cursor.fetchone()
            values = (result[0] + 1, inventory_id, item ,count)
            cursor.execute(self.INSERT_ITEM, values)
            self._db_connection.commit()
        except Exception as e :
            print(f'Exception is Persistance Wrapper: {e}')
        
        
    def _initialize_database_connection(self, config):
        """Initializes and returns database connection pool."""
        cnx = None
        try:
            cnx = connector.connect(pool_name = 'dbpool', pool_size=10, **config)
        except Exception as e:
            print(e)
        return cnx




