from fnmatch import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch(file, '*.txt'):
            print('Text files:', file)

        if fnmatch(file, '*.rb'):
            print('Ruby files:', file)

        if fnmatch(file, '*.yml'):
            print('Yaml files:', file)

        if fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print(second_base_players)