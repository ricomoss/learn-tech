#!/usr/bin/python
from __future__ import unicode_literals
import os

from general_classes import ClassifiedObject, Object
from specific_classes import Creature


def wait():
    raw_input('\nPress Enter to continue...\n\n')
    os.system(['clear', 'cls'][os.name == 'nt'])


def create_an_object():
    my_object_properties = {
        'name': 'creature',
    }

    object = Object()
    object.set_properties(my_object_properties)
    object.print_properties()
    wait()


def create_a_creature():
    my_creature_properties = {
        'name': 'Michael Hollowburton',
        'mass': '225 kg',
        'classification': 'animal',
    }
    creature = ClassifiedObject()
    creature.set_properties(my_creature_properties)
    creature.print_properties()
    wait()


def create_a_lion():
    properties = {
        'name': 'Michael Hollowburton',
        'mass': '225 kg',
        'classification': 'animal',
    }
    taxonomy = {
        'Domain': 'Eukaryote',
        'Kingdom': 'Animalia',
        'Phylum': 'Chordata',
        'Class': 'Mammalia',
        'Order': 'Carnivora',
        'Family': 'Felidae',
        'Genus': 'Panthera',
        'Species': 'Panthera leo',
    }
    lion1 = Creature()
    lion1.set_properties(properties)
    lion1.set_taxonomy(taxonomy)
    lion1.print_properties()
    wait()

    lion1.print_taxonomy()
    wait()

    lion1.print_all_properties()
    wait()

    # Let's see the power of instantiation
    lion2 = Creature()
    properties['name'] = 'Emily McCarrol'
    properties['mass'] = '175 kg'
    lion2.set_properties(properties)
    lion2.set_taxonomy(taxonomy)
    lion2.print_all_properties()
    wait()


if __name__ == '__main__':
    wait()
    # How to instantiate and use classes
    create_an_object()
    create_a_creature()
    create_a_lion()
