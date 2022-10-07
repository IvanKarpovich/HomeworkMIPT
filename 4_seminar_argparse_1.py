import sys
import json
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--name', type=str)
parser.add_argument('--country', type=str)
parser.add_argument('--petal-colour', choices=['R', 'W', 'Y', 'V', 'B'], type=str)
parser.add_argument('--stem-length', type=int)
parser.add_argument('--with-thorns', action='store_true')
parser.add_argument('--companion-plants', nargs='*', default=None, type=str)

args = parser.parse_args()

if __name__ == '__main__':

    flower_text_to_add = {
            'name':args.name,
            'country':args.country,
            'petal-colour':args.petal_colour,
            'stem-length':args.stem_length,
            'with-thorns':args.with_thorns,
            'companion-plants':args.companion_plants,

            }

    with open('journal.json', 'a') as f:
        json.dump(flower_text_to_add, f, indent=4)
