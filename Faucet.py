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
    Faucet.check_address_validity("x")
