""" Contains a block.io payment processor """

from block_io import BlockIo
import blockioconfig
apiversion = 2 # API version

from AbstractPaymentProcessor import AbstractPaymentProcessor

class BlockIoPaymentProcessor(AbstractPaymentProcessor):
    """ Class for executing faucet payments on block.io """
    
    _block_io = BlockIo(blockioconfig.apikey, blockioconfig.secretpin, 
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
    
    
