from my_classes import AddressBook


def create_address_book():
    """
    Instantiate and populate an AddressBook object
    """
    return AddressBook({
        'first_name': 'Henry',
        'last_name': 'Ferguson',
        'phone': '1234567890',
        'email': 'henry_ferguson11882@gmail.com',
        'birthday': {
            'day': '12',
            'month': '11',
            'year': '1984',
        },
        'address': {
            'address1': '123 Bomb St.',
            'address2': 'Apt. 213A',
            'city': 'Denver',
            'state': 'Colorado',
            'postal_code': '80224',
            'country': 'USA',
        },
    })


def add_content1(ab1):
    """
    Add content to ab1
    """
    ab1.add_content({
        'first_name': 'Jeff',
        'last_name': 'Ferguson',
        'phone': '5555555555',
        'email': 'jeff_ferguson7272@gmail.com',
        'birthday': {
            'day': '3',
            'month': '6',
            'year': '2011',
        },
        'address': {
            'address1': '123 Bomb St.',
            'address2': 'Apt. 213A',
            'city': 'Denver',
            'state': 'Colorado',
            'postal_code': '80224',
            'country': 'USA',
        },
    })
    return ab1


def add_content2(ab2):
    """
    Add content to ab1
    """
    ab2.add_content({
        'first_name': 'Martha',
        'last_name': 'Ferguson',
        'phone': '1234567890',
        'email': 'martha_ferguson665@gmail.com',
        'birthday': {
            'day': '22',
            'month': '2',
            'year': '1987',
        },
        'address': {
            'address1': '321 Awesome St.',
            'address2': 'Apt. 332B',
            'city': 'Denver',
            'state': 'Colorado',
            'postal_code': '80203',
            'country': 'USA',
        },
    })
    return ab2


def add_address_books(ab1, ab2):
    return ab1 + ab2


def create_address_books():
    ab1 = create_address_book()
    ab1 = add_content1(ab1)
    ab2 = create_address_book()
    ab2 = add_content2(ab2)
    return ab1, ab2

