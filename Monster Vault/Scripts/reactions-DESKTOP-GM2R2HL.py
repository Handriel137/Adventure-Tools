import json
import csv
import ast

input_file = csv.DictReader(open("monsters.csv"))

with open('sampledata/reactions.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'name', 
        'desc',
        'attack_bonus', 
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in input_file:
        if row['reactions'] is not "":
            # print(row['reactions'])
            mon_reaction = ast.literal_eval(row['reactions'])
            # print(mon_reaction)
            # writer.writerow(mon_reaction)

            for item in mon_reaction:
                # print(type(item))
                # print(row["name"])
                # print(item["name"])
                item['name'] = row['name'] + ' - ' + item['name']
                print(item)
                writer.writerow(item)
            # print(item['name'], item['desc'])
            


    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # writer.writeheader()
    # for monster in monsters[:-1]:
        
    #     # if "reactions" in monster.keys():
    #     #     monster["reactions"] = set([f'{monster["name"]} - {reaction["name"]}' for reaction in monster["reactions"]])
            
    #     writer.writerow(monster)