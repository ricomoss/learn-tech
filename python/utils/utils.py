import os


def wait():
    raw_input('\n\n\nPress Enter to continue...\n\n')
    os.system(['clear', 'cls'][os.name == 'nt'])

