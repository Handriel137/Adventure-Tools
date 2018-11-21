import json
import csv

monsters = json.loads(open("json_data/5e-SRD-Monsters.json").read())
with open('sampledata/monsters.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'name', 
        'size', 
        'type', 
        'subtype', 
        'alignment', 
        'armor_class', 
        'hit_points', 
        'hit_dice', 
        'speed', 
        'strength', 
        'dexterity', 
        'constitution', 
        'intelligence', 
        'wisdom', 
        'charisma', 
        'wisdom_save', 
        'damage_vulnerabilities', 
        'damage_resistances', 
        'damage_immunities', 
        'condition_immunities', 
        'senses', 
        'languages', 
        'challenge_rating',
        'special_abilities',
        'actions',
        'constitution_save', 
        'perception', 
        'history', 
        'legendary_actions', 
        'intelligence_save',
        'religion',
        'medicine',
        'stealth',
        'dexterity_save',
        'charisma_save',
        'persuasion',
        'insight',
        'deception',
        'athletics',
        'arcana',
        'nature',
        'acrobatics',
        'strength_save',
        'reactions',
        'survival',
        'investigation',
        'intimidation',
        'performance',
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for monster in monsters[:-1]:
        # print(monster)
        if "special_abilities" in monster.keys():
            monster["special_abilities"] = list([f'{monster["name"]} - {sb["name"]}' for sb in monster["special_abilities"]])
        if "actions" in monster.keys():
            monster["actions"] = set([f'{monster["name"]} - {action["name"]}' for action in monster["actions"]])
        if "reactions" in monster.keys():
            monster["reactions"] = set([f'{monster["name"]} - {reaction["name"]}' for reaction in monster["reactions"]])
                  
            
        writer.writerow(monster)