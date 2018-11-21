import json
import csv
import ast

monsters = csv.DictReader(open('sampledata/monsters.csv'))
actions = csv.DictReader(open('sampledata/actions.csv'))



for row in monsters:
    actions = ast.literal_eval(row['actions'])
    print(type(actions))