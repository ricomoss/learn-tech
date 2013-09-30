#!/usr/bin/python
from __future__ import unicode_literals
import os


def wait():
    raw_input('\nPress Enter to continue...\n\n')
    os.system(['clear', 'cls'][os.name == 'nt'])


# Create a class to handle items in a wallet
class BaseWalletHandler(object):
    def __init__(self):
        self.items = {
            'Driver\'s License': False,
            'Credit Card': False,
            'Cash': False,
            'Change': False,
            'Insurance Card': False,
            'ICE Info': False,
            'Pictures': False,
        }

    def add_item(self, item):
        if item in self.items.keys():
            self.items[item] = True

    def remove_item(self, item):
        if item in self.items.keys():
            self.items[item] = False

    def show_items(self):
        for key, value in self.items.items():
            if value is True:
                print key


# Can more refactoring happen to clean this up more?
class WalletHandler(BaseWalletHandler):
    def __init__(self):
        super(WalletHandler, self).__init__()

    def add_item(self, item):
        super(WalletHandler, self).add_item(item)
        if item not in self.items.keys():
            self.items[item] = True


def exercise():
    wallet_handler = BaseWalletHandler()
    wallet_handler.add_item('Driver\'s License')
    wallet_handler.add_item('ICE Info')
    wallet_handler.add_item('Credit Card')
    wallet_handler.add_item('Business Card')
    wallet_handler.show_items()
    wait()

    wallet_handler = WalletHandler()
    wallet_handler.add_item('Driver\'s License')
    wallet_handler.add_item('ICE Info')
    wallet_handler.add_item('Credit Card')
    wallet_handler.add_item('Business Card')
    wallet_handler.show_items()
    wait()


if __name__=='__main__':
    exercise()
