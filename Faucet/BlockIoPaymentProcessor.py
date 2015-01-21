""" Contains a block.io payment processor """

import logging
import logging.config

from block_io import BlockIo
import blockioconfig
apiversion = 2 # API version

from AbstractPaymentProcessor import AbstractPaymentProcessor

import abc

class BlockIoPaymentProcessor(AbstractPaymentProcessor):
    """ Class for executing faucet payments on block.io """
    
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.info("Creating BlockIoPaymentProcessor instance")
        self._block_io = BlockIo(blockioconfig.apikey, blockioconfig.secretpin,
                                    apiversion)

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

    def get_available_balance(self, address=None):
        """ Get the available balance

        Keyword arguments:

        address -- Adress to get balance from. Valid address or None for total
                    balance"""
        reply=None
        if address:
            reply = self._block_io.get_address_balance(addresses=address)
        else:
            reply = self._block_io.get_balance()

        if reply["status"] == "success":
            # can this cause problems?
            return float(reply["data"]["available_balance"])
        else:
            # ???, maybe raise an exeption?
            raise Exception("Error querying block.io: %s", reply)

    
if __name__ == "__main__":
    b=BlockIoPaymentProcessor()
    rep = b.get_available_balance()
    print "%f" % (rep, )
