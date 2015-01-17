""" This is going to be a dogecoin faucet """

# Database support
import sqlite3
# date / time calculations
import datetime
# URL fetching
import requests
# logging!
import logging

# wallet processings
from block_io import BlockIo

logging.basicConfig(level=logging.INFO)

__version__ = "0.1"

class Faucet:
    """ Faucet class
    
    Contains all methods neccessary to execute a faucet """

    # database file name
    _filename = "doge.db"
    def __init__(self):
        """ Create a new Faucet """
        
        self._logger = logging.getLogger(__name__)
        self._logger.info("Creating class")
        
        # initialite connections
        self._connection = sqlite3.connect(self._filename)
        self._connection.row_factory = sqlite3.Row
        self._logger.info(self._connection.isolation_level)
        
        # set error messag to empty
        self.message = ""
        pass

    def __del__(self):
        """ Destructor, close connections, clean up, etc. """
        self._logger.info("Deleting")
        self._connection.close()

    def __enter__(self):
        """ Gets autmatically called on the beginning of a with statement """
        return self
        pass

    def __exit__(self, type, value, traceback):
        """ Gets autmatically called on the end of a with statement """
        self._logger.info("Exiting")
        self._connection.close()
        pass
        
        
    # todo: Lock, to avoid double-adding from multiple conections ?
    def add_payout_request(self,  address, force=False):
        """ add an address to the payout 
        
        Returns True if payout was added, otherwise false """
        # waiting: datetime, address
        pass
        
    def check_payout_request(self, address):
        """ Check if address is eligible for a payout request
        
        Returns True if payout request is okay, otherwise False"""
        
        # waiting: datetime, address
        cu = self._connection.execute("SELECT * FROM waiting WHERE address=?", (address, ));
        ro = cu.fetchone()
        if not ro:
            return True
        else:
            self.message = "Address %s was already added at %s" % (ro["address"], ro["datetime"])
            return False
    
    # TODO    
    def process_payouts(self, address):
        """ (TODO) process the payout requests """
        
        # processed: datetime, payout, number_addresses, txid
        # processed_addresses: address, process_id (FK)
        pass
        
    # TODO
    def get_balance(self):
        """ (TODO) Get faucet balance """
        # balance: datetime, amount
        pass

    #TODO
    @staticmethod
    def check_address_validity(address):
        """ (TODO) check if address is valid """
        pass

if __name__ == '__main__':
    print "Not callable"
    with Faucet() as fau:
        pass
