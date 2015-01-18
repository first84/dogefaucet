""" Contains payment processors for executing payments """

from abc import ABCMeta, abstractmethod

class AbstractPaymentProcessor:
    """ Abstract class for executing faucet Payments

    Implement this at your own. Possible implementations include
    online wallets and RPC calls to running dogecoin wallets """
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute_payment(self, destination_address, amount):
        """ Execute a payment to one receiving single address
        
        return the transaction id or None """
        pass

    @abstractmethod
    def execute_multi_payment(self, destination_addresses, amounts):
        """ Execute a payment to multiple receiving addresses
        
        return the transaction id or None """
        pass
        
    @abstractmethod
    def get_transaction_status(self):
        """ Get the status of the transaction
        
        Indicate if transaction is already confirmed. Return
         - True if confirmed
         - False if unconfirmed
         - None if transaction doesn't exist (or raise exception?)"""
        pass
    
    
