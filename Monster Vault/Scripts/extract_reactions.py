import json
import csv

monsters = json.loads(open("json_data/5e-SRD-Monsters.json").read())

for monster in monsters[:-1]:
	if "reactions" in monster.keys():
		# print(monster["reactions"])

		monster["reactions"] = [f'{monster["name"]} - {reaction["name"]}' for reaction in monster["reactions"]]
		# print(type(monster))
		print(monster["reactions"])
		# print(monster)
			# print([f'{monster["name"]} - {reaction["name"]}' for reaction in monster["reactions"]])

