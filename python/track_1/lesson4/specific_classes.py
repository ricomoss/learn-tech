from __future__ import unicode_literals

from general_classes import ClassifiedObject, Taxonomy


class Creature(ClassifiedObject, Taxonomy):
    def __init__(self):
        self.properties = {
            'name': '',
            'mass': '',
            'classification': '',
        }

        self.taxonomy = {
            'Domain': '',
            'Kingdom': '',
            'Phylum': '',
            'Class': '',
            'Order': '',
            'Family': '',
            'Genus': '',
            'Species': '',
        }

    def print_all_properties(self):
        self.print_properties()
        self.print_taxonomy()
