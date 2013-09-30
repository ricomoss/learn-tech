#!/usr/bin/python
import os


def wait():
    raw_input('\nPress Enter to continue...\n\n')
    os.system(['clear', 'cls'][os.name == 'nt'])


def review_loops():
    # Let's look at lists
    test_list = list()
    test_list.append('item 1')
    test_list.append('item 2')
    test_list.append('item 3')

    # Indexed from zero
    print test_list[0]
    print test_list[1]
    print test_list[2]
    wait()


def cover_tuples(LOCATION='here', TIME='now'):

    # Tuples are immutable sequences
    CHOICES = (LOCATION, TIME)

    for choice in CHOICES:
        print choice
    wait()

    # All container types can be embedded
    CHOICES = (
        (LOCATION, 'Here'),
        (TIME, 'Now'),
    )

    for choice in CHOICES:
        print choice[1]
    wait()

    # Avoid "magic numbers" - use constants instead
    CHOICE_VALUE = 1
    for choice in CHOICES:
        print choice[CHOICE_VALUE]
    wait()

    # See the whole tuple
    for choice in CHOICES:
        print choice
    wait()


def cover_dicts():

    # Dictionaries are arguably the most powerful container in Python
    test_dict = {
        'First Name': 'Rico',
        'Last Name': 'Cordova',
        'Eye Color': 'Brown',
        'Hair Color': 'Black',
    }
    for key, value in test_dict.items():
        print 'test_dict[{}] = {}'.format(key, value)
    wait()

    # Let's add a dictionary to our dictionary
    languages_dict = dict()
    languages_dict['Python'] = 'Favorite'
    languages_dict['Perl'] = 'So Ugly'
    languages_dict['PHP'] = 'Ewwww'
    languages_dict['Java'] = 'Ok'
    languages_dict['C++'] = 'Awesome'
    languages_dict['Ruby'] = 'Good Times'
    languages_dict['Objective C'] = 'Loathed'
    test_dict['Programming Languages'] = languages_dict
    for key, value in test_dict.items():
        print 'test_dict[{}] = {}'.format(key, value)
    wait()

    # Advanced topic:  We can check by types
    for key, value in test_dict.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                print '{}[{}] = {}'.format(key, sub_key, sub_value)
        else:
            print 'test_dict[{}] = {}'.format(key, value)
    wait()


# Create a dictionary from information in a file
# File structure:
#  ____________________
# | <first_name>       |
# | <last_name>        |
# | <eye_color>        |
# | <hair_color>       |
# | <favorite_animal>  |
# |____________________|
#
# Example:
#  ____________________
# | Rico               |
# | Cordova            |
# | Brown              |
# | Black              |
# | Cat                |
# |____________________|
def exercise():
    my_file = open('exercise_1.txt', 'r')
    keys = ['First Name', 'Last Name', 'Eye Color', 'Hair Color',
            'Favorite Animal']
    my_dict = dict()
    for key in keys:
        my_dict[key] = my_file.readline()
    print my_dict
    wait()

    # Let's get rid of the newlines
    for key in keys:
        my_dict[key] = my_file.readline().strip()
    print my_dict
    wait()


if __name__ == '__main__':
    
    wait()    
    
    # Review Lists
    review_loops()
    
    # Learn about tuples and arguments
    location = 'Salt Lake City'
    time = '6:00 pm'
    cover_tuples(location, time)
    
    # Learn about dictionaries
    cover_dicts()

    # Exercise
    exercise()
