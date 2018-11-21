import json
import csv
import ast

input_file = csv.DictReader(open("monsters.csv"))

with open('sampledata/actions.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'name', 
        'desc',
        'attack_bonus',
        'damage_dice',
        'damage_bonus', 
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in input_file:
        if row['actions'] is not "":
            # print(row['reactions'])
            mon_reaction = ast.literal_eval(row['actions'])
            # print(mon_reaction)
            # writer.writerow(mon_reaction)

            for item in mon_reaction:
                # print(row['name'])
                # print(item['name'])
                item['name'] = row['name'] + " - " + item['name']
                writer.writerow(item)
            # print(item['name'], item['desc'])