import json
import os
import argparse

from savefile import SaveFile
from general import GeneralData
from monster import Monster, MONSTER_TABLE
from battles import Battle
from inventory import Item, Weapon, INVENTORY_TABLE
from skills import Skill, SKILL_TABLE


def main():
    parser = argparse.ArgumentParser(description="DQMJ2 Savefile Editor")
    parser.add_argument('path', type=str, help='Path to the save file')
    parser.add_argument('--template', default="", type=str, help='Optional template .sav file, required if you want to load in a json file.')
    args = parser.parse_args()

    path = os.path.normpath(args.path)
    template = os.path.normpath(args.template)

    if path.endswith('.sav'):
        print(f'Exporting savefile to {None}.')
        file = SaveFile(path)

    elif path.endswith('.json'):
        if not template.endswith('.sav'):
            raise ValueError(f'For editing a savefile with json data, a savefile template is required to be loaded in first.')
        print(f'Importing json data to savefile {None}.')
        file_data = {}
        with open(path, 'r') as file:
            file_data = json.load(file)
        
    else:
        raise NameError(f'This editor can only handle .sav and .json files, not {path.split(".")[-1]}.')

if __name__ == "__main__":
    main()