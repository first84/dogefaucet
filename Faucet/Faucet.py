""" This is going to be a dogecoin faucet """

# Database support
import sqlite3
# date / time calculations
import datetime
# URL fetching
import requests
# logging!
import logging

import random
import string

logging.basicConfig(level=logging.INFO)

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
        
        # TODO: Is it "safe" to store a connection as instance 
        # attribute? would it be better to do a try/catch every time?
        # or a with statement, for that matter?
        self._connection = sqlite3.connect(self._filename)
        self._connection.row_factory = sqlite3.Row
        
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
        
        self._logger.info("Adding payment request for %s", address)
        is_ok = True
        if not force:
            is_ok = self.check_payout_request(address)
        else:
            self._logger.info("Force-Adding payment request for %s", address)
        
        if is_ok:
            self._logger.info("Inserting payment request for %s", address)
            self._connection.execute("INSERT INTO waiting (datetime, address) VALUES (?, ?)", 
                                       (datetime.datetime.utcnow().strftime("%d.%m.%y %H:%M:%S"), 
                                        address))
            self._connection.commit()
        return is_ok
     
        
    def check_payout_request(self, address):
        """ Check if address is eligible for a payout request
        
        Returns True if payout request is okay, otherwise False"""
        
        self._logger.info("Checking payment request for %s", address)
        # waiting: datetime, address
        cu = self._connection.execute("SELECT * FROM waiting WHERE address=?", (address, ));
        ro = cu.fetchone()
        if not ro:
            self._logger.info("Address is not yet in database")
            return True
        else:
            self.message = "Address %s was already added at %s" % (ro["address"], ro["datetime"])
            self._logger.info(self.message)
            return False
    
    # TODO    
    def process_payouts(self, address):
        """ (TODO) process the payout requests """
        
        # processed: datetime, payout, number_addresses, txid
        # processed_addresses: address, process_id (FK)

        # 1) Get all addresses from waiting, store them (GROUP BY address is a great way to avoid dupes!?)
        # 2) Delete results from 1) from waiting (executemany?)
        # 3) Check for duplicate addresses, remove them
        # 4) Create transmission on block.io with all the waiting addresses
        # 5) Add transaction to processed, get id
        # 6) Insert all waiting addresses with FK into processed_addresses (executemany!)

        # This has to be executed as a whole transaction somehow. What if something goes wrong along the way?
        # e.g. transaction on block.io failing?

        raise NotImplementedError("Not implemented yet")
        
    # TODO
    def get_balance(self):
        """ (TODO) Get faucet balance """
        # balance: datetime, amount
        raise NotImplementedError("Not implemented yet")

    #TODO
    @staticmethod
    def check_address_validity(address):
        """ (TODO) check if address is valid """
        raise NotImplementedError("Not implemented yet")

if __name__ == '__main__':
    # test code
    with Faucet() as fau:
        fau.check_payout_request("X")
        x = fau.check_payout_request("DDuMLYg7PA7QVxqFp8qUiB46CdmAmcBC2s")
        if x:
            fau.add_payout_request("DDuMLYg7PA7QVxqFp8qUiB46CdmAmcBC2s")
            fau.check_payout_request("DDuMLYg7PA7QVxqFp8qUiB46CdmAmcBC2s")
        
        randomaddress = "D"+''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(33))
        x = fau.check_payout_request(randomaddress)
        if x:
            fau.add_payout_request(randomaddress)
            fau.check_payout_request(randomaddress)
        pass
