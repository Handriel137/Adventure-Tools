import json
import csv
import ast

input_file = csv.DictReader(open("monsters.csv"))

with open('sampledata/legendary_actions.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'name', 
        'desc',
        'attack_bonus',
        'damage_dice',
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in input_file:
        if row['legendary_actions'] is not "":
            # print(row['reactions'])
            mon_legendary_actions = ast.literal_eval(row['legendary_actions'])
            # print(mon_actions)
            # writer.writerow(mon_actions)

            for item in mon_legendary_actions:
                # print(type(item))
                # print(item)
                item['name'] = row['name'] + " - " + item['name']
                writer.writerow(item)
            # print(item['name'], item['desc'])