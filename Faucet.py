""" This is going to be a dogecoin faucet """


# Database support
import sqlite3
# date / time calculations
import datetime
# URL fetching
import requests

# wallet processings
from block_io import BlockIo

__version__ = "0.1"


class Faucet:
    """ Faucet class
    
    Contains all methods neccessary to execute a faucet """

    _filename = "doge.db"
    def __init__(self):
        pass
        
    def add_payout_request(self,  address):
        """ add an address to the payout """
        # waiting: datetime, address
        pass
        
    def check_payout_request(self, address):
        """ Check if address is eligitable for a payout request"""
        
        # waiting: datetime, address
        pass
        
    def process_payouts(self, address):
        """ process the payout requests """
        
        # processed: datetime, payout, number_addresses, txid
        # processed_addresses: address, process_id (FK)
        pass
        
    def get_balance(self):
        """ Get faucet balance """
        # balance: datetime, amount
        pass
        
    @staticmethod
    def check_address_validity(address):
        """ check if address is valid """
        pass

if __name__ == '__main__':
    print "Not callable"
    Faucet.check_address_validity("x")
