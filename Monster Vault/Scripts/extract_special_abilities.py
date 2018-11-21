import json
import csv

monsters = json.loads(open("json_data/5e-SRD-Monsters.json").read())

for monster in monsters[:-1]:
	if "special_abilities" in monster.keys():
		# print(monster["reactions"])

		monster["special_abilities"] = [f'{monster["name"]} - {special_ability["name"]}' for special_ability in monster["special_abilities"]]
			# print(reaction
		print(monster["special_abilities"])
		# print(monster)
			# print([f'{monster["name"]} - {reaction["name"]}' for reaction in monster["reactions"]])

