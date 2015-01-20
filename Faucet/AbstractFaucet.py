from abc import ABCMeta, abstractmethod

# 2015/01/20: Just found out that abc doesn't enforce method arguments.

class AbstractFaucet:
    """Abstract faucet

    Various faucets are possible, e.g. instant-payout-faucets and
    delayed-payout-faucets, even some kind of "lottery" faucet. Your imagination
    is the limit """
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def request_payout(self):
        """ Request a payout """
        pass

    @abstractmethod
    def process_payouts(self):
        """ Execute / process a payout """
        pass
    
    @abstractmethod
    def get_balance(self):
        """ Get available "cash" """
        pass
