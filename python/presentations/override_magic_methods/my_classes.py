from copy import deepcopy

from utils import add_dictionaries, format_phone, sub_dictionaries


class AddressBook(object):
    """
    Simple address book with helpful methods.
    """
    def __init__(self, content=None):
        """
        Initialize internal dictionary and pre-populate
        """
        self.content = dict()
        if isinstance(content, dict):
            if content.get(1):
                self.content = deepcopy(content)
            else:
                self.content[1] = deepcopy(content)

    def add_content(self, content):
        """
        Add address content
        """
        index = self.count() + 1
        self.content[index] = deepcopy(content)

    def count(self):
        """
        Return the length of the dictionary
        """
        return len(self.content)

    def __repr__(self):
        """
        What should be the result of eval(AddressBook)
        """
        return '<Address Book: Contains {} Entries>'.format(self.count())

    def __str__(self):
        """
        Visually pleasing output of a print statement
        """
        output = ''
        for value in self.content.values():
            output += '{} {}: {}\n'.format(
                value['first_name'], value['last_name'],
                format_phone(value['phone']))
        return output

    def __add__(self, other):
        """
        Add two address book instances together
        OR
        Add a dictionary to the existing address book
        """
        if isinstance(other, AddressBook):
            return AddressBook(add_dictionaries(self.content, other.content))
        elif isinstance(other, dict):
            self.add_content(other)
            return AddressBook(self.content)
        err_msg = "unsupported operand type(s) for +: '{}' and '{}'"
        raise TypeError(err_msg.format(type(self), type(other)))

    def __sub__(self, other):
        """
        Remove any intersected information from two address book instances
        OR
        Remove any intersected information from the existing address book
        """
        if isinstance(other, AddressBook):
            return AddressBook(sub_dictionaries(self.content, other.content))
        elif isinstance(other, dict):
            return AddressBook(sub_dictionaries(self.content, other))
        err_msg = "unsupported operand type(s) for -: '{}' and '{}'"
        raise TypeError(err_msg.format(type(self), type(other)))

    def __contains__(self, name):
        """
        Check if the address book contains an entry for the given name
        """
        for val in self.content.values():
            first_name = val.get('first_name', '').lower()
            last_name = val.get('last_name', '').lower()
            full_name = '{} {}'.format(first_name, last_name)
            if name.lower() in (first_name, last_name, full_name):
                return True
        return False

    def __iter__(self):
        """
        Define the iterator to return the internal dictionaries
        """
        for value in self.content.values():
            yield value

    def __enter__(self):
        """
        Define the setup for a "with" statement
        """
        names = list()
        for value in self.content.values():
            names.append(
                '{} {}'.format(value['first_name'], value['last_name']))
        return names

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Define tear down and suppress exceptions for "with" statement
        """
        if exc_type is None:
            return True
        return isinstance(exc_val, IndexError)

    def __del__(self):
        """
        Do any necessary cleanup here
        """
        print('AddressBook has been deleted.')

    def __lt__(self, other):
        """
        Compare the number of entries in the address book with either
        another address book or a number.
        """
        if isinstance(other, (int, float)):
            return self.count() < other
        elif isinstance(other, AddressBook):
            return self.count() < other.count()
        err_msg = 'unorderable types: {} < {}'
        raise TypeError(err_msg.format(type(self), type(other)))

    def __le__(self, other):
        """
        Compare the number of entries in the address book with either
        another address book or a number.
        """
        if isinstance(other, (int, float)):
            return self.count() <= other
        if isinstance(other, AddressBook):
            return self.count() <= other.count()
        err_msg = 'unorderable types: {} <= {}'
        raise TypeError(err_msg.format(type(self), type(other)))

    def __gt__(self, other):
        """
        Compare the number of entries in the address book with either
        another address book or a number.
        """
        if isinstance(other, (int, float)):
            return self.count() > other
        elif isinstance(other, AddressBook):
            return self.count() > other.count()
        err_msg = 'unorderable types: {} < {}'
        raise TypeError(err_msg.format(type(self), type(other)))

    def __ge__(self, other):
        """
        Compare the number of entries in the address book with either
        another address book or a number.
        """
        if isinstance(other, (int, float)):
            return self.count() >= other
        elif isinstance(other, AddressBook):
            return self.count() >= other.count()
        err_msg = 'unorderable types: {} < {}'
        raise TypeError(err_msg.format(type(self), type(other)))

    def __eq__(self, other):
        """
        Compare the number of entries in the address book with either
        another address book or a number.
        """
        if isinstance(other, (int, float)):
            return self.count() == other
        elif isinstance(other, AddressBook):
            return self.count() == other.count()
        err_msg = 'unorderable types: {} < {}'
        raise TypeError(err_msg.format(type(self), type(other)))

    def __ne__(self, other):
        """
        Compare the number of entries in the address book with either
        another address book or a number.
        """
        if isinstance(other, (int, float)):
            return self.count() != other
        elif isinstance(other, AddressBook):
            return self.count() != other.count()
        err_msg = 'unorderable types: {} < {}'
        raise TypeError(err_msg.format(type(self), type(other)))

