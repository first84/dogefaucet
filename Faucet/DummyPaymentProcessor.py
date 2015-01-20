""" Contains a logging payment processor """

import logging
import random
logging.basicConfig(level=logging.INFO)

from AbstractPaymentProcessor import AbstractPaymentProcessor

class DummyLoggingPaymentProcessor (AbstractPaymentProcessor):
    """ Payment processor that does nothing, just logs """

    def __init__(self):
        self._logger = logging.getLogger(__name__)
    
    def execute_payment(self, destination_address, amount):
        """ Execute a payment to one receiving single address
        
        return the transaction id or None """
        raise NotImplementedError("Not implemented yet")

    def execute_multi_payment(self, destination_addresses, amounts):
        """ Execute a payment to multiple receiving addresses
        
        return the transaction id or None """
        raise NotImplementedError("Not implemented yet")
        
    def get_transaction_status(self):
        """ Get the status of the transaction
        
        Indicate if transaction is already confirmed. Return
         - True if confirmed
         - False if unconfirmed
         - None if transaction doesn't exist """
        raise NotImplementedError("Not implemented yet")

    def get_available_balance(self):
        amount = random.randint(0,1500)
        self._logger.info("Balance is %d", amount)
        return amount
    

if __name__ == '__main__':
    c = DummyLoggingPaymentProcessor()
    c.get_available_balance()
